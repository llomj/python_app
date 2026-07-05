#!/usr/bin/env python3
"""
AI-powered breakdown generator using qwen2.5-coder:1.5b via Ollama.
Replaces template breakdowns with problem-specific step-by-step guides.

Usage:
  python3 scripts/generate_ai_breakdowns.py            # test run (first 5)
  python3 scripts/generate_ai_breakdowns.py --all       # all 1981 exercises
  python3 scripts/generate_ai_breakdowns.py --dry-run   # count only, no changes
"""
import json, re, sys, time, subprocess

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'
OLLAMA_MODEL = 'llama3.2:3b'
OLLAMA_API = 'http://localhost:11434/api/chat'

FALLBACK = (
    "1. Read the problem carefully — identify what input the function takes, "
    "what output it should produce, and any special requirements mentioned.\n"
    "2. Decide which Python tools fit: built-in functions (sum, max, min, len), "
    "loops, conditionals, list/dict/string methods, or a combination.\n"
    "3. Write one step at a time: start with the function signature, then add "
    "logic for the expected output, checking intermediate values as you go.\n"
    "4. Test with the examples given. Pay attention to edge cases "
    "(empty input, negatives, type mismatches)."
)


def is_ollama_ready():
    try:
        r = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}',
             'http://localhost:11434/api/tags'],
            capture_output=True, text=True, timeout=5)
        return r.stdout.strip() == '200'
    except Exception:
        return False


def extract_exercise_blocks(lines):
    start_idx = 0
    for i, line in enumerate(lines):
        if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
            start_idx = i + 1
            break

    blocks = []
    in_ex = False
    depth = 0
    cur = []
    for i in range(start_idx, len(lines)):
        ob = lines[i].count('{')
        cb = lines[i].count('}')
        if '{' in lines[i] and not in_ex:
            in_ex = True
            depth = ob - cb
            cur = [(lines[i], i)]
        elif in_ex:
            cur.append((lines[i], i))
            depth += ob - cb
            if depth <= 0:
                blocks.append(cur)
                cur = []
                in_ex = False
    return blocks


def extract_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(
        r'"' + field + r'":\s*"((?:[^"\\]|\\.)*)"',
        full)
    if m:
        return m.group(1)
    m = re.search(r'"' + field + r'":\s*(\d+)', full)
    if m:
        return m.group(1)
    return ''


def extract_id(block):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"id":\s*(\d+)', full)
    return int(m.group(1)) if m else 0


def find_field_line(lines, block, field_name):
    """Find the exact line index of a field in an exercise block."""
    for _, lineno in block:
        if lineno < len(lines) and field_name in lines[lineno]:
            return lineno
    return None


def generate_breakdown(desc, problem_id, title):
    prompt = (
        f"You are a Python tutor writing a 'guide' for a student.\n\n"
        f"Problem {problem_id}: {title}\n"
        f"Description: {desc}\n\n"
        f"Write exactly 5-7 numbered steps that GUIDE the student to solve this EXACT problem themselves.\n"
        f"STRICT RULES:\n"
        f"- Each step MUST be 1-2 specific, concrete sentences.\n"
        f"- NEVER write any Python code. NOT EVEN ONE LINE.\n"
        f"- NEVER say 'Write the code', 'Implement the function', or 'Here is how' — that's giving the answer.\n"
        f"- EVERY step must name a specific function, method, or technique the student should use.\n"
        f"- Add a brief [definition in brackets] after the first technical term in each step.\n"
        f"- Call out the specific trick or pitfall of THIS exact problem.\n"
        f"- End with: test with the examples given.\n\n"
        f"Return ONLY the numbered lines:\n"
        f"1. First guide step.\n"
        f"2. Second guide step.\n"
        f"3. Third guide step."
    )

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.15, "num_predict": 1200}
    })

    try:
        r = subprocess.run(
            ['curl', '-s', '-X', 'POST', OLLAMA_API, '-d', payload],
            capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            return ''

        data = json.loads(r.stdout)
        content = data.get('message', {}).get('content', '')
        if not content:
            return ''

        # Clean: remove code fences, markdown bold
        content = re.sub(r'```[\s\S]*?```', '', content)
        content = content.replace('**', '').replace('__', '')

        lines = []
        for line in content.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            if re.match(r'^\d+[\.\)]\s', line):
                clean = re.sub(r'^\d+[\.\)]\s*', '', line)
                if clean and len(clean) > 10 and '`def ' not in clean:
                    lines.append(clean)

        if len(lines) >= 3:
            return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(lines))
        return ''
    except Exception as e:
        print(f'    Error: {e}')
        return ''


def main():
    do_all = '--all' in sys.argv
    dry_run = '--dry-run' in sys.argv

    print(f'Reading {EXERCISES_FILE}...')
    with open(EXERCISES_FILE, 'r') as f:
        lines = f.read().split('\n')

    blocks = extract_exercise_blocks(lines)
    print(f'Found {len(blocks)} exercise blocks.')

    existing_count = sum(1 for b in blocks if find_field_line(lines, b, '"breakdown":') is not None)
    print(f'Exercises with existing "breakdown" field: {existing_count}')

    if dry_run:
        return

    if not is_ollama_ready():
        print('ERROR: Ollama is not running on localhost:11434')
        sys.exit(1)

    print(f'Using model: {OLLAMA_MODEL}')
    batch = blocks if do_all else blocks[:5]
    print(f'Generating breakdowns for {len(batch)} exercises...')

    # Collect edits as (line_to_insert_before, new_text, line_to_remove)
    edits = []

    for block in batch:
        desc = extract_field(block, 'description')
        desc = desc.replace('\\n', ' ').replace('\\"', '"').replace('\\t', ' ')
        pid = extract_id(block)
        title = extract_field(block, 'title') or ''
        print(f'  [{pid}] {title[:60]}...', end=' ', flush=True)

        if not desc:
            print('SKIP (no description)')
            continue

        hint_lineno = find_field_line(lines, block, '"hint":')
        if hint_lineno is None:
            print('SKIP (no hint field)')
            continue

        brk_lineno = find_field_line(lines, block, '"breakdown":')

        breakdown = generate_breakdown(desc, pid, title)
        if not breakdown:
            print('FALLBACK')
            breakdown = FALLBACK

        esc = breakdown.replace('\\', '\\\\').replace('"', '\\"')
        edits.append((hint_lineno, f'            "breakdown": "{esc}",\n', brk_lineno))
        n_steps = len(breakdown.split('\n'))
        print(f'OK ({n_steps} steps)')

        time.sleep(0.3)

    if not edits:
        print('No results.')
        return

    # Apply edits bottom-to-top to preserve line numbers
    edits.sort(key=lambda x: x[0], reverse=True)
    new_lines = lines[:]
    for insert_at, text, remove_at in edits:
        # Remove old breakdown line (singular — the entire JSON value is on one line)
        if remove_at is not None:
            # Ensure we only remove the exact breakdown line
            if remove_at < len(new_lines) and '"breakdown":' in new_lines[remove_at]:
                new_lines.pop(remove_at)
                # Adjust insert_at if it was after the removed line
                if insert_at > remove_at:
                    insert_at -= 1
        # Insert new breakdown before hint
        new_lines.insert(insert_at, text)

    suffix = '_test'
    out_file = EXERCISES_FILE
    if not do_all:
        out_file = EXERCISES_FILE.replace('.ts', '_test.ts')

    with open(out_file, 'w') as f:
        f.write('\n'.join(new_lines))

    print(f'\nDone. Wrote {len(edits)} breakdowns to {out_file}')
    if not do_all:
        print(f'Review {out_file}, then run with --all to process all {len(blocks)} exercises.')


if __name__ == '__main__':
    main()

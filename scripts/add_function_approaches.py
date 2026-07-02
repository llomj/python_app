#!/usr/bin/env python3
"""
Add function approach to exercises missing it, clean up empty sections.
Preserves all existing content — only adds and cleans.
"""
import json, os, re, time, urllib.request

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'
PROGRESS_FILE = '/Users/moll/Desktop/python_app/scripts/.func_approach_progress.json'
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5-coder:1.5b"
MAX_RETRIES = 2
DELAY_BETWEEN = 0.2

EXAMPLES = """Example 1:
# Using function approach
def is_within_range(numbers, min_val, max_val):
    return all(min_val <= x <= max_val for x in numbers)

nums = [5, 6, 7]
print(is_within_range(nums, 1, 10))

Example 2:
# Using function approach
def find_longest_key(**kwargs):
    return max(kwargs, key=len)

print(find_longest_key(apple=5, banana=3, cherry=8))

Example 3:
# Using function approach
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for ch in text.lower() if ch in vowels)

print(count_vowels('Jonathan'))"""


def gen_function_approach(desc, icode, eid):
    prompt = f"""{EXAMPLES}

Write ONLY the function approach for THIS problem. Start with exactly "# Using function approach". Include the function def, example call, and print(). No other sections.

Problem #{eid}: {desc[:400]}
Starter code: {icode[:200]}"""

    payload = json.dumps({"model": MODEL, "messages": [
        {"role": "system", "content": "You are a Python tutor. Write correct Python code only."},
        {"role": "user", "content": prompt}
    ], "stream": False, "options": {"temperature": 0.1, "num_predict": 512}}).encode()

    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        r = json.loads(resp.read())
        return r["message"]["content"].strip()


def clean_solution(text):
    """Remove empty headings and broken stub sections."""
    lines = text.split('\n')
    result = []
    skip_next = False
    for i, line in enumerate(lines):
        # Skip empty headings (heading followed by blank then another heading)
        if re.match(r'^#\s+\w+\s+approach\s*$', line):
            # Check if next non-empty line is also a heading or empty
            next_lines = lines[i+1:i+3]
            next_content = [l for l in next_lines if l.strip()]
            if not next_content or re.match(r'^#\s+\w+\s+approach\s*$', next_content[0]):
                continue  # Skip this empty heading
        # Skip lines that are just "pass" or "..." (stubs)
        if line.strip() in ('pass', '...', 'fn()', ''):
            continue
        result.append(line)
    return '\n'.join(result)


def read_blocks(content):
    lines = content.split('\n')
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


def get_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"(?:\\.|[^"\\])*"', full)
    if m:
        raw = m.group(0)
        val = re.search(r'":\s*"(.*)"$', raw)
        if val:
            return val.group(1)
    return ''


def get_id(block):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"id":\s*(\d+)', full)
    return int(m.group(1)) if m else 0


def main():
    with open(EXERCISES_FILE, 'r') as f:
        content = f.read()

    blocks = read_blocks(content)
    lines = content.split('\n')
    print(f'Read {len(blocks)} blocks.')

    # Count
    need_func = 0
    need_cleanup = 0
    for block in blocks:
        sol = get_field(block, 'solution')
        if not sol: continue
        text = sol.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
        if 'function approach' not in text.lower():
            need_func += 1
        # Check for empty headings
        if re.search(r'^#\s+\w+\s+approach\s*$', text, re.M):
            # Check if followed by another heading
            lines_t = text.split('\n')
            for i, l in enumerate(lines_t):
                if re.match(r'^#\s+\w+\s+approach\s*$', l):
                    next_lines = lines_t[i+1:i+3]
                    next_c = [x for x in next_lines if x.strip()]
                    if not next_c or re.match(r'^#\s+\w+\s+approach\s*$', (next_c[0] if next_c else '')):
                        need_cleanup += 1
                        break

    print(f'Need function approach: {need_func}')
    print(f'Need cleanup: {need_cleanup}')

    # Resume from progress
    already_done = set()
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            already_done = set(json.load(f).get('done_ids', []))
        print(f'Resuming: {len(already_done)} done')

    # Process each block
    total = len(blocks)
    start_time = time.time()
    edits = []
    generated = 0

    for idx, block in enumerate(blocks):
        eid = get_id(block)
        if eid in already_done:
            continue

        sol_raw = get_field(block, 'solution')
        if not sol_raw:
            continue

        text = sol_raw.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
        orig_text = text
        has_func = 'function approach' in text.lower()

        # Clean up
        text = clean_solution(text)

        # Add function approach if missing
        if not has_func:
            desc = get_field(block, 'description').replace('\\n', ' ').replace('"', "'")
            icode = get_field(block, 'initialCode').replace('\\n', ' ').replace('"', "'")
            if not desc:
                continue

            print(f'[{idx+1}/{total}] #{eid} generating function approach... ', end='', flush=True)
            ok = False
            for attempt in range(MAX_RETRIES + 1):
                try:
                    new_code = gen_function_approach(desc, icode, eid)
                    new_code = re.sub(r'```\w*\n?', '', new_code).strip()
                    if len(new_code) > 20:
                        text = new_code + '\n\n' + text
                        ok = True
                        break
                except:
                    time.sleep(DELAY_BETWEEN * 5)
            if not ok:
                print('SKIP')
                continue
            generated += 1
            print('OK')
        elif text == orig_text:
            continue  # No changes

        # Find solution line
        sol_lineno = None
        for bl, lineno in block:
            if '"solution":' in bl:
                sol_lineno = lineno
                break
        if sol_lineno is None:
            continue

        # Re-escape
        escaped = text.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
        indent = lines[sol_lineno][:len(lines[sol_lineno]) - len(lines[sol_lineno].lstrip())]
        edits.append((sol_lineno, f'{indent}"solution": "{escaped}",'))

        # Save progress
        already_done.add(eid)
        if generated % 20 == 0 and generated > 0:
            with open(PROGRESS_FILE, 'w') as f:
                json.dump({'done_ids': list(already_done)}, f)

        time.sleep(DELAY_BETWEEN)

    # Apply edits
    if edits:
        edits.sort(key=lambda x: x[0], reverse=True)
        for lineno, new_line in edits:
            lines[lineno] = new_line
        with open(EXERCISES_FILE, 'w') as f:
            f.write('\n'.join(lines))
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)

    elapsed = time.time() - start_time
    print(f'\nDone! Generated: {generated}, Time: {elapsed/60:.1f}m')


if __name__ == '__main__':
    main()

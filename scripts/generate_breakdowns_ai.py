#!/usr/bin/env python3
"""
AI breakdown generator — uses qwen2.5-coder:1.5b (via Ollama)
to produce problem-specific step-by-step guidance for every exercise.

Runs once offline; output saved as static JSON in exercises.ts.
1.5B model = 986MB, safe for 8GB Mac.
"""
import json, os, re, time, urllib.request

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5-coder:1.5b"
EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'
PROGRESS_FILE = '/Users/moll/Desktop/python_app/scripts/.breakdown_progress.json'
MAX_RETRIES = 2
DELAY_BETWEEN = 0.2
TEST_LIMIT = 0

SYSTEM_MSG = """You are a Python tutor. Write numbered steps that explain how to solve a coding problem. Each step names the exact function, parameter, class, or concept from the problem with a [bracket definition]. Describe what to do without writing any code. Never include Python code at all."""

FEW_SHOT_STEPS = """EXAMPLE steps for kwargs problem:
1. Use `max(kwargs, key=len)` — `max()` [built-in: returns the largest item] with `key=len` [compares items by their length] to find the longest key name.
2. `kwargs` [special parameter that collects keyword arguments into a dict] gives you all the named arguments passed by the caller.
3. Return the result of `max(kwargs, key=len)` directly — it gives the key with the longest name.

EXAMPLE steps for Rectangle with @property:
1. Define the `Rectangle` class with `__init__` storing `self.width` and `self.height` — instance attributes [data on each object].
2. Add `@property` to a method named `area` — decorator [makes a method act like an attribute] so `rect.area` works.
3. In the getter, return `self.width * self.height` to compute area.
4. Add `@area.deleter` above another method named `area` — this runs when `del rect.area` is called.
5. In the deleter, set `self.width = 0` and `self.height = 0`."""


def call_ollama(desc, icode, eid):
    prompt = f"""{FEW_SHOT_STEPS}

Now write steps for THIS problem. Mention specific function/class/parameter names from the problem. Give a [bracket definition] for each technical term. Do NOT include any code. Do NOT add features not in the problem.

Problem #{eid}: {desc[:400]}
Starter code: {icode[:200]}

Output only numbered lines starting from 1:
1."""

    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_MSG},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 1024}
    }).encode()

    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    with urllib.request.urlopen(req, timeout=180) as resp:
        result = json.loads(resp.read())
        content = result["message"]["content"]
        tin = result.get("prompt_eval_count", 0)
        tout = result.get("eval_count", 0)
        return content.strip(), tin, tout


def parse_breakdown(text):
    # Strip code blocks entirely
    text = re.sub(r'```[\s\S]*?```', '', text)
    lines = text.strip().split('\n')
    steps = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip lines that are pure code or markdown fences
        if line.startswith(("```", "Here", "Output", "---", "**")):
            continue
        # Skip lines containing inline code assignments
        if re.match(r'^(self\.|def |class |return |print )', line):
            continue
        cleaned = re.sub(r'^\d+[\.\)]\s*', '', line).strip()
        if not cleaned:
            continue
        steps.append(cleaned)
    return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps)) if steps else ''


def has_problem_specific_terms(text, desc):
    """Verify the breakdown mentions at least one function/class name from the problem."""
    backtick_terms = re.findall(r'`(\w+)`', desc)
    code_terms = re.findall(r'def (\w+)', desc) + re.findall(r'class (\w+)', desc)
    expected = set(t.lower() for t in backtick_terms + code_terms if len(t) > 1)
    if not expected:
        return True  # skip check if we can't extract any terms
    text_lower = text.lower()
    found = sum(1 for term in expected if term in text_lower)
    return found >= max(1, len(expected) // 2)


def read_exercises(path):
    with open(path, 'r') as f:
        content = f.read()
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
    return lines, blocks


def get_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"(?:\\.|[^"\\])*"', full)
    if m:
        raw = m.group(0)
        val = re.search(r'":\s*"(.*)"$', raw)
        if val:
            return val.group(1).replace('\\n', '\n').replace('\\"', '"').replace('\\t', ' ')
    return ''


def get_id(block):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"id":\s*(\d+)', full)
    return int(m.group(1)) if m else 0


def apply_edits(lines, edits):
    edits.sort(key=lambda x: x[0], reverse=True)
    for insert_after, text, remove_at in edits:
        if remove_at is not None:
            if remove_at < len(lines) and '"breakdown":' in lines[remove_at]:
                lines.pop(remove_at)
                if insert_after > remove_at:
                    insert_after -= 1
        lines.insert(insert_after + 1, text + '\n')
    return lines


def main():
    lines, blocks = read_exercises(EXERCISES_FILE)
    print(f'Read {len(blocks)} exercises.')

    todo = []
    for block in blocks:
        eid = get_id(block)
        desc = get_field(block, 'description').replace('\\n', ' ').replace('"', "'")
        icode = get_field(block, 'initialCode').replace('\\n', ' ').replace('"', "'")
        if not desc:
            continue
        todo.append((eid, desc, icode, block))

    if TEST_LIMIT:
        todo = todo[:TEST_LIMIT]
        print(f'TEST MODE: {TEST_LIMIT} exercises')

    total = len(todo)
    print(f'Processing {total} exercises...')

    pending = []
    generated = 0
    skipped = 0
    total_in = 0
    total_out = 0
    start_time = time.time()

    already_done = set()
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE) as f:
                already_done = set(json.load(f).get('done_ids', []))
            print(f'Resuming: {len(already_done)} already done')
        except:
            pass

    for idx, (eid, desc, icode, block) in enumerate(todo):
        if eid in already_done:
            generated += 1
            continue

        elapsed = time.time() - start_time
        rate = (idx + 1) / elapsed if elapsed > 0 else 0
        remaining = (total - idx - 1) / rate if rate > 0 else 0
        print(f'[{idx+1}/{total}] #{eid} ({elapsed/60:.0f}m, ~{remaining/60:.0f}m left)... ', end='', flush=True)

        text = ''
        success = False
        for attempt in range(MAX_RETRIES + 1):
            try:
                raw, tin, tout = call_ollama(desc, icode, eid)
                total_in += tin
                total_out += tout
                text = parse_breakdown(raw)
                if text and len(text) > 30 and has_problem_specific_terms(text, desc):
                    success = True
                    break
                print(f'(weak) ', end='', flush=True)
            except Exception as ex:
                print(f'(err) ', end='', flush=True)
                time.sleep(DELAY_BETWEEN * 5)

        if not success:
            print('SKIP')
            skipped += 1
            continue

        esc = text.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
        bd_text = f'            "breakdown": "{esc}",'

        hint_lineno = None
        brk_lineno = None
        for bl, lineno in block:
            if '"hint":' in bl:
                hint_lineno = lineno
            if '"breakdown":' in bl:
                brk_lineno = lineno

        if hint_lineno is None:
            print('no hint, SKIP')
            skipped += 1
            continue

        pending.append((hint_lineno, bd_text, brk_lineno))
        already_done.add(eid)
        generated += 1
        print(f'OK ({len(text)}c)')
        time.sleep(DELAY_BETWEEN)

        if generated % 20 == 0:
            with open(PROGRESS_FILE, 'w') as f:
                json.dump({'done_ids': list(already_done)}, f)

    if pending:
        print(f'Applying {len(pending)} edits...')
        lines, _ = read_exercises(EXERCISES_FILE)
        lines = apply_edits(lines, pending)
        with open(EXERCISES_FILE, 'w') as f:
            f.write('\n'.join(lines))
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)

    elapsed = time.time() - start_time
    print(f'\n{"="*60}')
    print(f'Done! Generated: {generated}, Skipped: {skipped}')
    print(f'Time: {elapsed/60:.1f}m, Tokens: {total_in} in, {total_out} out')


if __name__ == '__main__':
    main()

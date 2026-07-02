#!/usr/bin/env python3
"""Add blank line between solution approach sections."""
import re

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

with open(EXERCISES_FILE, 'r') as f:
    content = f.read()

lines = content.split('\n')

start_idx = 0
for i, line in enumerate(lines):
    if 'Exercise[] = [' in line:
        start_idx = i + 1
        break

fixed = 0
for i in range(start_idx, len(lines)):
    line = lines[i]
    if '"solution":' not in line:
        continue

    m = re.search(r'"solution":\s*"(?:\\.|[^"\\])*"', line)
    if not m: continue

    full_match = m.group(0)
    inner_m = re.search(r'":\s*"(.*)"$', full_match)
    if not inner_m: continue

    sol_raw = inner_m.group(1)
    sol_text = sol_raw.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')

    # Normalize: reduce 3+ newlines to 2 (single blank line)
    new_text = re.sub(r'\n{3,}', r'\n\n', sol_text)
    # Add blank line before approach headings where missing
    new_text = re.sub(r'(?<!\n)\n(#[^\n]*approach)', r'\n\n\1', new_text)

    if new_text == sol_text:
        continue

    escaped = new_text.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
    indent = line[:len(line) - len(line.lstrip())]
    lines[i] = f'{indent}"solution": "{escaped}",'
    fixed += 1

with open(EXERCISES_FILE, 'w') as f:
    f.write('\n'.join(lines))

print(f'Fixed {fixed} solutions with spacing.')

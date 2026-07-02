#!/usr/bin/env python3
"""
Quick fix: remove fn() placeholder lines from solutions.
No AI needed — simple text cleanup.
"""
import re

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

with open(EXERCISES_FILE, 'r') as f:
    content = f.read()

lines = content.split('\n')

# Find start of exercises array
start_idx = 0
for i, line in enumerate(lines):
    if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
        start_idx = i + 1
        break

fixed = 0
for i in range(start_idx, len(lines)):
    line = lines[i]
    if '"solution":' not in line:
        continue
    
    # Extract the solution value (unescape it for manipulation)
    m = re.search(r'"solution":\s*"(?:\\.|[^"\\])*"', line)
    if not m:
        continue
    
    full_match = m.group(0)
    # Get the inner value
    inner_m = re.search(r'":\s*"(.*)"$', full_match)
    if not inner_m:
        continue
    
    sol_raw = inner_m.group(1)
    # Unescape for text manipulation
    sol_text = sol_raw.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
    
    if 'fn(' not in sol_text:
        continue  # No placeholders, skip
    
    # Remove lines containing fn(
    new_lines = [l for l in sol_text.split('\n') if 'fn(' not in l]
    new_text = '\n'.join(new_lines).strip()
    
    if not new_text:
        continue
    
    # Re-escape for JSON
    escaped = new_text.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
    
    # Build new line
    # Preserve indentation
    indent = line[:len(line) - len(line.lstrip())]
    new_line = f'{indent}"solution": "{escaped}",'
    
    lines[i] = new_line
    fixed += 1
    print(f'Line {i}: fixed')

print(f'\nFixed {fixed} solutions with fn() placeholders.')

with open(EXERCISES_FILE, 'w') as f:
    f.write('\n'.join(lines))

print('Done.')

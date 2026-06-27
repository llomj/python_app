#!/usr/bin/env python3
"""Insert '# Using function approach' label before the first def/class in each solution."""

import re
import sys
from pathlib import Path

TS_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/Users/moll/Desktop/python_app/exercises.ts')
DRY_RUN = '--dry-run' in sys.argv
LABEL = '# Using function approach'


def unescape_ts(s):
    return (s.replace('\\\\', '\\')
             .replace('\\"', '"')
             .replace("\\'", "'")
             .replace('\\n', '\n'))


def escape_ts(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('\n', '\\n')
    s = s.replace('"', "'")
    return s


def find_solution_end(text, start_pos):
    i = start_pos
    while i < len(text):
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
        elif text[i] == '"' and i + 1 < len(text) and text[i + 1] == ',':
            return i
        else:
            i += 1
    return -1


def find_first_code_start(lines):
    """Find index of first non-blank, non-comment, non-import line."""
    in_import_block = False
    for i, l in enumerate(lines):
        stripped = l.strip()
        if not stripped:
            continue
        if stripped.startswith('import ') or stripped.startswith('from '):
            in_import_block = True
            continue
        if in_import_block and (stripped.startswith('import ') or stripped.startswith('from ')):
            continue
        if in_import_block and not stripped.startswith('#'):
            # We've passed the import block — this is where code starts
            return i
        if stripped.startswith('#'):
            continue
        # This is a non-import, non-comment line (def, class, for, variable, etc.)
        return i
    return -1


def has_label_already(code):
    return LABEL in code


def process():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    id_matches = list(re.finditer(r'"id": (\d+),', content))
    modified = 0
    already_labeled = 0
    skipped = 0
    offset = 0

    for idx, idm in enumerate(id_matches):
        pid = int(idm.group(1))
        prob_pos = idm.start() + offset
        next_pos = (id_matches[idx + 1].start() if idx + 1 < len(id_matches) else len(content)) + offset
        chunk = content[prob_pos:next_pos]

        sol_field = '"solution": "'
        sol_pos = chunk.find(sol_field)
        if sol_pos == -1:
            skipped += 1
            continue

        val_start = prob_pos + sol_pos + len(sol_field)
        close_quote = find_solution_end(content, val_start)
        if close_quote == -1:
            skipped += 1
            continue

        sol_raw = content[val_start:close_quote]
        code = unescape_ts(sol_raw)

        if has_label_already(code):
            already_labeled += 1
            continue

        lines = code.split('\n')
        code_start = find_first_code_start(lines)
        if code_start == -1 or code_start >= len(lines):
            skipped += 1
            continue

        # Insert the label before code_start
        label_line = LABEL
        lines.insert(code_start, label_line)
        new_code = '\n'.join(lines)

        new_sol_raw = escape_ts(new_code)

        if '"' in new_sol_raw:
            skipped += 1
            continue

        if not DRY_RUN:
            content = content[:val_start] + new_sol_raw + content[close_quote:]
            offset += len(new_sol_raw) - len(sol_raw)
        modified += 1

    if not DRY_RUN:
        with open(TS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

    total = len(id_matches)
    print(f'Total problems: {total}')
    print(f'Modified (label inserted): {modified}')
    print(f'Already labeled: {already_labeled}')
    print(f'Skipped: {skipped}')
    print(f'Mode: {"DRY RUN" if DRY_RUN else "APPLIED"}')


if __name__ == '__main__':
    process()

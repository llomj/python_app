#!/usr/bin/env python3
"""Translate .py solution files to French using Ollama.
Processes comment text and docstrings, keeping code intact."""

import re, os, json, sys, time, shutil

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen2.5-coder:1.5b"
BATCH_SIZE = 5  # How many comment lines to translate in one API call

def translate_with_ollama(texts):
    """Translate a batch of non-code lines using Ollama."""
    if not texts:
        return texts
    
    # Join with separators
    joined = "\n---SEP---\n".join(texts)
    
    prompt = f"""Translate ALL of the following English text into French. 
Only translate natural language - keep ANY code, variable names, function names, operators, 
punctuation, and special characters exactly as-is. 
Keep ALL Python code inside backticks unchanged.
Keep line breaks, spacing, and structure.

For each input line, output the French translation.

INPUT:
{joined}

OUTPUT:"""
    
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": 4096}
        }, timeout=120)
        
        result = response.json().get("response", "")
        
        # Split back by separator
        translated = result.split("---SEP---")
        # Pad if needed
        while len(translated) < len(texts):
            translated.append(texts[len(translated)])
        
        return [t.strip() if t.strip() else texts[i] for i, t in enumerate(translated)]
    except Exception as e:
        print(f"  API error: {e}")
        return texts


def translate_file(input_path, output_path, max_lines=None):
    """Process a single file."""
    import requests  # import here
    
    with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    lines = content.split('\n')
    if max_lines:
        lines = lines[:max_lines]
    
    total = len(lines)
    output_lines = []
    in_docstring = False
    buffer = []  # (original_idx, text, line_type)
    
    COMMENT = 'comment'
    DOCSTRING = 'docstring'
    CODE = 'code'
    
    # Phase 1: Classify each line
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Docstring tracking
        if '"""' in stripped:
            qc = stripped.count('"""')
            if qc == 1:
                in_docstring = not in_docstring
                buffer.append((i, line, CODE if not in_docstring else DOCSTRING))
                continue
            elif qc >= 2:
                # Full docstring on one line - translate content
                match = re.match(r'(\s*""")(.*?)(""".*)', line, re.DOTALL)
                if match:
                    indent, content_text, rest = match.group(1), match.group(2), match.group(3)
                    if content_text.strip():
                        buffer.append((i, line, DOCSTRING))
                        continue
                buffer.append((i, line, CODE))
                continue
        if "'''" in stripped:
            qc = stripped.count("'''")
            if qc == 1:
                in_docstring = not in_docstring
                buffer.append((i, line, CODE if not in_docstring else DOCSTRING))
                continue
        
        if in_docstring:
            buffer.append((i, line, DOCSTRING))
            continue
        
        # Comment line
        if stripped.startswith('#'):
            buffer.append((i, line, COMMENT))
            continue
        
        # Inline comment
        if '#' in line:
            # Check if # is in a string
            in_str = False
            sc = None
            ci = -1
            for j, ch in enumerate(line):
                if ch in '"\'' and (j == 0 or line[j-1] != '\\'):
                    if not in_str:
                        in_str = True
                        sc = ch
                    elif ch == sc:
                        in_str = False
                        sc = None
                elif ch == '#' and not in_str:
                    ci = j
                    break
            if ci >= 0:
                before = line[:ci]
                comment = line[ci:]
                buffer.append((i, before, 'code_before'))
                buffer.append((i, comment, COMMENT))
                continue
        
        buffer.append((i, line, CODE))
    
    # Phase 2: Translate comment/docstring lines in batches
    to_translate = [(idx, line) for idx, line, lt in buffer if lt in (COMMENT, DOCSTRING)]
    
    translated_map = {}
    
    for batch_start in range(0, len(to_translate), BATCH_SIZE):
        batch = to_translate[batch_start:batch_start + BATCH_SIZE]
        texts = [t[1] for t in batch]
        
        translated = translate_with_ollama(texts)
        
        for (orig_idx, _), trans in zip(batch, translated):
            translated_map[orig_idx] = trans
        
        if (batch_start // BATCH_SIZE) % 5 == 0:
            print(f"  Translated {min(batch_start + BATCH_SIZE, len(to_translate))}/{len(to_translate)}")
        time.sleep(0.5)  # Rate limit
    
    # Phase 3: Reassemble
    for idx, line, lt in buffer:
        if lt in (COMMENT, DOCSTRING):
            output_lines.append(translated_map.get(idx, line))
        else:
            output_lines.append(line)
    
    result = '\n'.join(output_lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    return total


def main():
    base = '/Users/moll/Desktop/python_app'
    
    # Start with just the requirements file for testing
    files = [
        ('level1_500_requirements.py', 'level1_500_requirements_fr.py'),
    ]
    
    for src, dst in files:
        inpath = f'{base}/{src}'
        outpath = f'{base}/{dst}'
        
        if not os.path.exists(inpath):
            print(f"SKIP: {src} not found")
            continue
        
        print(f"Processing: {src} -> {dst}")
        lines = translate_file(inpath, outpath, max_lines=200)  # Just first 200 for testing
        print(f"  Done: {lines} lines\n")

if __name__ == '__main__':
    main()

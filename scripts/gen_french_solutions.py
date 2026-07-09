#!/usr/bin/env python3
"""Generate French solution/requirements/syntax files.
Translates headers, section titles, and docstrings.
Keeps extensive educational comment body in English initially,
but critical UI-visible text is French."""

import re, json, os, shutil

BASE = '/Users/moll/Desktop/python_app'

# Load French exercise descriptions
with open(f'{BASE}/services/exercisesFr.ts') as f:
    fr_content = f.read()

match = re.search(r'EXERCISES_FR: Record<number, string> = \{([\s\S]*?)\};', fr_content)
EXERCISES_FR = {}
for line in match.group(1).strip().split('\n'):
    line = line.strip().rstrip(',')
    if not line: continue
    m = re.match(r'(\d+):\s*(.*)', line)
    if m:
        try:
            EXERCISES_FR[int(m.group(1))] = json.loads(m.group(2))
        except:
            pass

# Header/section title translations (comprehensive)
SECTION_TITLES = {
    "PROBLEM EXPLANATION:": "EXPLICATION DU PROBLÈME :",
    "Problem Explanation:": "Explication du Problème :",
    "PROBLEM EXPLANATION": "EXPLICATION DU PROBLÈME",
    "SOLUTION EXPLANATION:": "EXPLICATION DE LA SOLUTION :",
    "Solution Explanation:": "Explication de la Solution :",
    "SOLUTION EXPLANATION": "EXPLICATION DE LA SOLUTION",
    "ALTERNATIVE SOLUTION EXPLANATION:": "EXPLICATION DE LA SOLUTION ALTERNATIVE :",
    "ALTERNATIVE SOLUTION EXPLANATION": "EXPLICATION DE LA SOLUTION ALTERNATIVE",
    "Key Requirements:": "Prérequis Clés :",
    "Key Requirements": "Prérequis Clés",
    "Example Input/Output:": "Exemple d'Entrée/Sortie :",
    "Example Input/Output": "Exemple d'Entrée/Sortie",
    "TEST CASE:": "CAS DE TEST :",
    "Test Case:": "Cas de Test :",
    "TEST CASES:": "CAS DE TEST :",
    "Test Cases:": "Cas de Test :",
    "EXPECTED OUTPUT:": "SORTIE ATTENDUE :",
    "Expected Output:": "Sortie Attendue :",
    "OUTPUT:": "SORTIE :",
    "OUTPUT": "SORTIE",
    "Overall Program Workflow Summary": "Résumé du Flux Global du Programme",
    "OVERALL PROGRAM WORKFLOW SUMMARY": "RÉSUMÉ DU FLUX GLOBAL DU PROGRAMME",
    "Program Flow:": "Flux du Programme :",
    "PROGRAM FLOW:": "FLUX DU PROGRAMME :",
    "Learning Path:": "Parcours d'Apprentissage :",
    "LEARNING PATH:": "PARCOURS D'APPRENTISSAGE :",
    "NOTE:": "REMARQUE :",
    "Note:": "Remarque :",
    "NOTES:": "REMARQUES :",
    "Notes:": "Remarques :",
    "TIP:": "ASTUCE :",
    "Tip:": "Astuce :",
    "TIPS:": "ASTUCES :",
    "Tips:": "Astuces :",
    "WARNING:": "ATTENTION :",
    "Warning:": "Attention :",
    "HINT:": "INDICE :",
    "Hint:": "Indice :",
    "HINTS:": "INDICES :",
    "Hints:": "Indices :",
    "Parameters:": "Paramètres :",
    "Returns:": "Retourne :",
    "Return Value:": "Valeur de Retour :",
    "Return type:": "Type de Retour :",
    "Time Complexity:": "Complexité Temporelle :",
    "Space Complexity:": "Complexité Spatiale :",
    "Raises:": "Lève :",
    "Input:": "Entrée :",
    "Output:": "Sortie :",
    # Syntax file specific
    "Syntax Analysis": "Analyse Syntaxique",
    "Execution Flow": "Flux d'Exécution",
    "Code Breakdown": "Analyse du Code",
    "Line-by-line Analysis": "Analyse Ligne par Ligne",
    "Program Logic": "Logique du Programme",
    "Code Logic": "Logique du Code",
    "Overall Logic": "Logique Globale",
    "Function Logic": "Logique de la Fonction",
    "Summary": "Résumé",
    "Workflow": "Flux de Travail",
    "Overview": "Aperçu",
    "Detailed Explanation": "Explication Détaillée",
    "Concept Explanation": "Explication du Concept",
    "Code Explanation": "Explication du Code",
    "Program Explanation": "Explication du Programme",
    "RESULT": "RÉSULTAT",
    "Result": "Résultat",
    "Analysis": "Analyse",
    "Description": "Description",
    "Purpose": "Objectif",
}

# Phrase translations for common educational text
PHRASES = [
    (r'This problem asks us to create a function', 'Ce problème nous demande de créer une fonction'),
    (r'This problem asks us to write a function', 'Ce problème nous demande d\'écrire une fonction'),
    (r'This problem requires us to create a function', 'Ce problème nous demande de créer une fonction'),
    (r'This problem requires us to write a function', 'Ce problème nous demande d\'écrire une fonction'),
    (r'The function should accept', 'La fonction doit accepter'),
    (r'The function should take', 'La fonction doit prendre'),
    (r'The function takes', 'La fonction prend'),
    (r'The function should return', 'La fonction doit retourner'),
    (r'This is a fundamental', 'C\'est une opération fondamentale'),
    (r'This is a basic', 'C\'est une opération de base'),
    (r'a common', 'une opération courante'),
    (r'that demonstrates', 'qui démontre'),
    (r'and return statements', 'et les instructions de retour'),
    (r'function definition', 'la définition de fonction'),
    (r'function parameters', 'les paramètres de fonction'),
    (r'Should work with', 'Doit fonctionner avec'),
    (r'both integers and floating-point numbers', 'les entiers et les nombres à virgule flottante'),
    (r'both integers', 'les entiers'),
    (r'and floating-point numbers', 'et les nombres à virgule flottante'),
    (r'can be any numeric type', 'peuvent être de tout type numérique'),
    (r'can be of any type', 'peuvent être de tout type'),
    (r'numeric parameter', 'paramètre numérique'),
    (r'numeric parameters', 'paramètres numériques'),
    (r'in Python', 'en Python'),
    
    # Solution explanation patterns
    (r'This is a concise one-liner solution', 'C\'est une solution concise en une ligne'),
    (r'This solution directly', 'Cette solution'),
    (r'The function takes two parameters', 'La fonction prend deux paramètres'),
    (r'This approach is memory-efficient', 'Cette approche est économe en mémoire'),
    (r'as it doesn\'t store intermediate values', 'car elle ne stocke pas de valeurs intermédiaires'),
    (r'This solution uses an intermediate variable', 'Cette solution utilise une variable intermédiaire'),
    (r'to store the result before returning', 'pour stocker le résultat avant de le retourner'),
    (r'While functionally identical to the previous solution', 'Bien que fonctionnellement identique à la solution précédente'),
    (r'this approach can be more readable for beginners', 'cette approche peut être plus lisible pour les débutants'),
    (r'and allows for easier debugging', 'et permet un débogage plus facile'),
    (r'The same logic but', 'La même logique mais'),
    (r'Same test case as above', 'Même cas de test que ci-dessus'),
    (r'demonstrating that both solutions produce the same output', 'démontrant que les deux solutions produisent la même sortie'),
    (r'demonstrates the function', 'démontre la fonction'),
    (r'The expected result is', 'Le résultat attendu est'),
    (r'which will be printed to the console', 'qui sera affiché dans la console'),
    (r'This demonstrates', 'Cela démontre'),
    (r'This example shows', 'Cet exemple montre'),
    (r'This test case', 'Ce cas de test'),
    
    # Workflow / summary phrases
    (r'This file contains multiple Python exercises', 'Ce fichier contient plusieurs exercices Python'),
    (r'and solutions demonstrating:', 'et solutions démontrant :'),
    (r'Function definitions:', 'Définitions de fonctions :'),
    (r'Creating reusable code blocks with def keyword', 'Création de blocs de code réutilisables avec le mot-clé def'),
    (r'Data types:', 'Types de données :'),
    (r'Working with strings, lists, numbers, and other Python types', 'Travail avec les chaînes, listes, nombres et autres types Python'),
    (r'Control structures:', 'Structures de contrôle :'),
    (r'Using if/elif/else for decisions, for/while for loops', 'Utilisation de if/elif/else pour les décisions, for/while pour les boucles'),
    (r'Built-in functions:', 'Fonctions intégrées :'),
    (r'Utilizing Python\'s built-in functions like len\(\), sum\(\), max\(\), min\(\)', 'Utilisation des fonctions intégrées de Python comme len(), sum(), max(), min()'),
    (r'String methods:', 'Méthodes de chaînes :'),
    (r'Manipulating text with .upper\(\), .lower\(\), .strip\(\), etc\.', 'Manipulation du texte avec .upper(), .lower(), .strip(), etc.'),
    (r'List operations:', 'Opérations sur les listes :'),
    (r'Creating, accessing, and modifying lists', 'Création, accès et modification de listes'),
    (r'Object-oriented concepts:', 'Concepts orientés objet :'),
    (r'Classes, inheritance, and methods', 'Classes, héritage et méthodes'),
    (r'Algorithm implementation:', 'Implémentation d\'algorithmes :'),
    (r'Manual implementations of common algorithms', 'Implémentations manuelles d\'algorithmes courants'),
    (r'Each exercise defines one or more functions', 'Chaque exercice définit une ou plusieurs fonctions'),
    (r'to solve a specific problem', 'pour résoudre un problème spécifique'),
    (r'Functions are tested with example inputs', 'Les fonctions sont testées avec des exemples d\'entrées'),
    (r'using print\(\) statements', 'à l\'aide d\'instructions print()'),
    (r'Some exercises show multiple solution approaches', 'Certains exercices montrent plusieurs approches de solution'),
    (r'The code progresses from basic operations to more complex problems', 'Le code progresse des opérations de base aux problèmes plus complexes'),
    (r'Start with simple arithmetic operations', 'Commencez par des opérations arithmétiques simples'),
    (r'Progress to list operations', 'Passez aux opérations sur les listes'),
    (r'Learn string manipulation', 'Apprenez la manipulation de chaînes'),
    (r'Explore control flow \(conditionals, loops\)', 'Explorez le flux de contrôle (conditions, boucles)'),
    (r'Explore control flow', 'Explorez le flux de contrôle'),
    (r'Advance to more complex algorithms and data structures', 'Avancez vers des algorithmes et structures de données plus complexes'),
]


def translate_headers_and_docstrings(content, file_type='requirements'):
    """Translate all section headers, docstrings, and UI-visible text."""
    lines = content.split('\n')
    output_lines = []
    in_docstring = False
    docstring_parts = []
    in_docstring_start = -1
    collecting_docstring = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        
        # === SECTION HEADERS ===
        if stripped.startswith('#'):
            # Check each header translation
            translated = stripped
            for en_title, fr_title in SECTION_TITLES.items():
                if en_title in translated:
                    translated = translated.replace(en_title, fr_title)
                    break
            
            # Apply phrase translations
            for pattern, replacement in PHRASES:
                try:
                    translated = re.sub(pattern, replacement, translated, flags=re.IGNORECASE)
                except:
                    pass
            
            output_lines.append(translated)
            i += 1
            continue
        
        # === DOCSTRING ===
        # Check for "Problem N:" docstring
        if re.match(r'""".*Problem\s+\d+:', stripped) or re.match(r"'''.*Problem\s+\d+:", stripped):
            # Extract the problem number
            m = re.search(r'Problem\s+(\d+):', stripped)
            if m:
                prob_num = int(m.group(1))
                fr_desc = EXERCISES_FR.get(prob_num, '')
                if fr_desc:
                    # Replace the English docstring with French
                    indent = line[:len(line) - len(line.lstrip())]
                    if stripped.startswith('"""'):
                        output_lines.append(f'{indent}"""')
                        output_lines.append(f'{indent}Problème {prob_num} :')
                        output_lines.append(f'{indent}{fr_desc}')
                        output_lines.append(f'{indent}"""')
                    else:
                        output_lines.append(f"{indent}'''")
                        output_lines.append(f'{indent}Problème {prob_num} :')
                        output_lines.append(f'{indent}{fr_desc}')
                        output_lines.append(f"{indent}'''")
                    i += 1
                    continue
        
        # Multi-line docstring translation
        if stripped.startswith('"""') or stripped.startswith("'''"):
            quote = stripped[:3]
            if not in_docstring:
                in_docstring = True
                docstring_parts = [line]
                in_docstring_start = i
                # Check if this single line completes the docstring
                rest = stripped[3:].strip()
                if quote in rest:
                    in_docstring = False
                    # Single line docstring
                    rest2 = rest[rest.index(quote)+3:].strip()
                    if rest2:
                        # Has content on same line
                        docstring_parts = [line]
                    output_lines.extend(docstring_parts)
                    docstring_parts = []
                i += 1
                continue
            else:
                # Closing docstring
                in_docstring = False
                # Try to translate the docstring content
                doctext = '\n'.join(docstring_parts[1:]) if len(docstring_parts) > 1 else docstring_parts[0][3:]
                if doctext.rstrip().endswith(quote):
                    doctext = doctext.rstrip()[:-3]
                
                # Check if this looks like a Problem N docstring
                m = re.search(r'Problem\s+(\d+):', doctext)
                if m:
                    prob_num = int(m.group(1))
                    fr_desc = EXERCISES_FR.get(prob_num, '')
                    if fr_desc:
                        indent = docstring_parts[0][:len(docstring_parts[0]) - len(docstring_parts[0].lstrip())]
                        output_lines.append(f'{indent}{quote}')
                        output_lines.append(f'{indent}Problème {prob_num} :')
                        output_lines.append(f'{indent}{fr_desc}')
                        output_lines.append(f'{indent}{quote}')
                        i += 1
                        docstring_parts = []
                        continue
                
                # Generic docstring: translate headers inside
                for j, dl in enumerate(docstring_parts):
                    for en_title, fr_title in SECTION_TITLES.items():
                        if en_title in dl:
                            docstring_parts[j] = dl.replace(en_title, fr_title)
                            break
                
                output_lines.extend(docstring_parts)
                docstring_parts = []
                i += 1
                continue
        
        if in_docstring:
            docstring_parts.append(line)
            i += 1
            continue
        
        # === INLINE COMMENTS ===
        if '#' in line:
            idx = line.index('#')
            before = line[:idx]
            comment = line[idx:]
            # Translate comment headers
            for en_title, fr_title in SECTION_TITLES.items():
                if en_title in comment:
                    comment = comment.replace(en_title, fr_title)
                    break
            output_lines.append(before + comment)
            i += 1
            continue
        
        # === CODE (passed through) ===
        output_lines.append(line)
        i += 1
    
    # Close any unclosed docstring
    if in_docstring and docstring_parts:
        output_lines.extend(docstring_parts)
    
    return '\n'.join(output_lines)


def process_all():
    """Process all solution files."""
    files = [
        # (source, output)
        ('level1_500_requirements.py', 'level1_500_requirements_fr.py'),
        ('level1_500_codelogic.py', 'level1_500_codelogic_fr.py'),
        ('level1_500_syntax.py', 'level1_500_syntax_fr.py'),
        ('level1_1000_requirements..py', 'level1_1000_requirements_fr.py'),
        ('level1_1000_codelogic.py', 'level1_1000_codelogic_fr.py'),
        ('level1_1000_syntax.py', 'level1_1000_syntax_fr.py'),
        ('level1_1500_requirements.py', 'level1_1500_requirements_fr.py'),
        ('level1_1500_codelogic.py', 'level1_1500_codelogic_fr.py'),
        ('level1_1500_syntax.py', 'level1_1500_syntax_fr.py'),
        ('level1_2000_requirements..py', 'level1_2000_requirements_fr.py'),
        ('level1_2000_codelogic.py', 'level1_2000_codelogic_fr.py'),
        ('level1_2000_syntax.py', 'level1_2000_syntax_fr.py'),
    ]
    
    total = 0
    for src, dst in files:
        inpath = f'{BASE}/{src}'
        outpath = f'{BASE}/{dst}'
        
        if not os.path.exists(inpath):
            print(f"SKIP (not found): {src}")
            continue
        
        print(f"Processing: {src} -> {dst}")
        with open(inpath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Determine file type for specific processing
        if '_codelogic' in src:
            ftype = 'codelogic'
        elif '_requirements' in src:
            ftype = 'requirements'
        else:
            ftype = 'syntax'
        
        result = translate_headers_and_docstrings(content, ftype)
        
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(result)
        
        lines = len(result.split('\n'))
        total += lines
        print(f"  Wrote {lines} lines")
    
    # Copy to public/ and dist/
    for subdir in ['public', 'dist']:
        dest = f'{BASE}/{subdir}'
        if os.path.exists(dest):
            for src, dst in files:
                _, fname = dst, dst.split('/')[-1]
                fr_name = dst
                src_path = f'{BASE}/{fr_name}'
                dst_path = f'{dest}/{fr_name}'
                if os.path.exists(src_path):
                    shutil.copy2(src_path, dst_path)
            print(f"Copied French files to {subdir}/")
    
    print(f"\nTotal lines processed: {total}")
    print("Done!")


if __name__ == '__main__':
    process_all()

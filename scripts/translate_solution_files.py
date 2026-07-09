#!/usr/bin/env python3
"""Translate all solution/requirements/syntax .py files to French.
Creates _fr.py copies with translated comments/docstrings, keeping code intact."""

import re, os, glob, sys

def load_translation_dict():
    """Load comprehensive translation dictionary for educational code comments."""
    # Ordered by specificity (longest first) for correct matching
    replacements = [
        # === PROGRAM WORKFLOW / STRUCTURE ===
        (r'Overall Program Workflow Summary', "Résumé du Flux de Programme"),
        (r'OVERALL PROGRAM WORKFLOW SUMMARY', "RÉSUMÉ DU FLUX DE PROGRAMME"),
        (r'Program Flow:', "Flux du Programme :"),
        (r'PROGRAM FLOW:', "FLUX DU PROGRAMME :"),
        (r'Learning Path:', "Parcours d'Apprentissage :"),
        (r'LEARNING PATH:', "PARCOURS D'APPRENTISSAGE :"),
        (r'Overall Workflow:', "Flux de Travail Global :"),
        (r'OVERALL WORKFLOW:', "FLUX DE TRAVAIL GLOBAL :"),
        (r'Workflow Summary:', "Résumé du Flux :"),
        
        # === SECTION HEADERS ===
        (r'Problem \d+ \w+ Explanation:', lambda m: f"Explication du Problème {m.group(1)} :"),
        (r'^# Key Requirements:$', "# Prérequis Clés :"),
        (r'Key Requirements:', "Prérequis Clés :"),
        (r'^# Example Input/Output:$', "# Exemple d'Entrée/Sortie :"),
        (r'Example Input/Output:', "Exemple d'Entrée/Sortie :"),
        (r'^# SOLUTION EXPLANATION:$', "# EXPLICATION DE LA SOLUTION :"),
        (r'SOLUTION EXPLANATION:', "EXPLICATION DE LA SOLUTION :"),
        (r'^# ALTERNATIVE SOLUTION EXPLANATION:$', "# EXPLICATION DE LA SOLUTION ALTERNATIVE :"),
        (r'ALTERNATIVE SOLUTION EXPLANATION:', "EXPLICATION DE LA SOLUTION ALTERNATIVE :"),
        (r'^# TEST CASE:$', "# CAS DE TEST :"),
        (r'TEST CASE:', "Cas de Test :"),
        (r'^# TEST CASES:$', "# CAS DE TEST :"),
        (r'TEST CASES:', "Cas de Test :"),
        (r'^# EXPECTED OUTPUT:$', "# SORTIE ATTENDUE :"),
        (r'Expected Output:', "Sortie Attendue :"),
        (r'^# OUTPUT$', "# SORTIE"),
        (r'^# Expected:$', "# Attendu :"),
        (r'^# Output$', "# Sortie"),
        (r'^# Input$', "# Entrée"),
        (r'^# Output:$', "# Sortie :"),
        (r'^# Example:$', "# Exemple :"),
        (r'^# Examples:$', "# Exemples :"),
        (r'^# RESULT:$', "# RÉSULTAT :"),
        (r'^# RESULT$', "# RÉSULTAT"),
        (r'^# Note:$', "# Remarque :"),
        (r'^# Notes:$', "# Remarques :"),
        (r'^# Tip:$', "# Astuce :"),
        (r'^# Tips:$', "# Astuces :"),
        (r'^# Warning:$', "# Attention :"),
        (r'^# Hint:$', "# Indice :"),
        (r'^# Hints:$', "# Indices :"),
        
        # === FUNCTION SUB-HEADERS ===
        (r'Parameters:', "Paramètres :"),
        (r'Returns:', "Retourne :"),
        (r'Return Value:', "Valeur de Retour :"),
        (r'Return type:', "Type de Retour :"),
        (r'Yield:', "Produit :"),
        (r'Raises:', "Lève :"),
        (r'Time Complexity:', "Complexité Temporelle :"),
        (r'Space Complexity:', "Complexité Spatiale :"),
        (r'Input:', "Entrée :"),
        (r'Output:', "Sortie :"),
        
        # === PROBLEM EXPLANATION SENTENCES ===
        (r'This problem asks us to create a function', "Ce problème nous demande de créer une fonction"),
        (r'This problem requires us to write a function', "Ce problème nous demande d'écrire une fonction"),
        (r'The function should accept', "La fonction doit accepter"),
        (r'The function should take', "La fonction doit prendre"),
        (r'The function takes', "La fonction prend"),
        (r'The function should return', "La fonction doit retourner"),
        (r'This is a fundamental', "C'est une opération fondamentale"),
        (r'This is a common', "C'est une opération courante"),
        (r'This is a basic', "C'est une opération de base"),
        (r'that demonstrates', "qui démontre"),
        (r'function definition', "la définition de fonction"),
        (r'function parameters', "les paramètres de fonction"),
        (r'and return statements', "et les instructions de retour"),
        (r'in Python', "en Python"),
        (r'Should work with', "Doit fonctionner avec"),
        (r'both integers', "les entiers"),
        (r'and floating-point numbers', "et les nombres à virgule flottante"),
        (r'numeric type', "type numérique"),
        (r'numeric types', "types numériques"),
        (r'numeric parameter', "paramètre numérique"),
        (r'numeric parameters', "paramètres numériques"),
        
        # === TECH VOCABULARY ===
        (r'This function', "Cette fonction"),
        (r'This approach', "Cette approche"),
        (r'This solution', "Cette solution"),
        (r'This method', "Cette méthode"),
        (r'This algorithm', "Cet algorithme"),
        (r'This technique', "Cette technique"),
        (r'This version', "Cette version"),
        
        (r'average', "moyenne"),
        (r'length', "longueur"),
        (r'value', "valeur"),
        (r'values', "valeurs"),
        (r'parameter', "paramètre"),
        (r'parameters', "paramètres"),
        (r'argument', "argument"),
        (r'arguments', "arguments"),
        (r'variable', "variable"),
        (r'variables', "variables"),
        (r'function', "fonction"),
        (r'functions', "fonctions"),
        (r'method', "méthode"),
        (r'methods', "méthodes"),
        (r'string', "chaîne"),
        (r'strings', "chaînes"),
        (r'list', "liste"),
        (r'lists', "listes"),
        (r'dictionary', "dictionnaire"),
        (r'dictionaries', "dictionnaires"),
        (r'tuple', "tuple"),
        (r'tuples', "tuples"),
        (r'set', "ensemble"),
        (r'sets', "ensembles"),
        (r'object', "objet"),
        (r'objects', "objets"),
        (r'class', "classe"),
        (r'classes', "classes"),
        (r'instance', "instance"),
        (r'instances', "instances"),
        (r'attribute', "attribut"),
        (r'attributes', "attributs"),
        (r'property', "propriété"),
        (r'properties', "propriétés"),
        (r'element', "élément"),
        (r'elements', "éléments"),
        (r'item', "élément"),
        (r'items', "éléments"),
        (r'index', "indice"),
        (r'indices', "indices"),
        (r'key', "clé"),
        (r'keys', "clés"),
        (r'loop', "boucle"),
        (r'loops', "boucles"),
        (r'iteration', "itération"),
        (r'iterator', "itérateur"),
        (r'iterable', "itérable"),
        (r'condition', "condition"),
        (r'conditions', "conditions"),
        (r'comparison', "comparaison"),
        (r'expression', "expression"),
        (r'expressions', "expressions"),
        (r'statement', "instruction"),
        (r'statements', "instructions"),
        (r'operator', "opérateur"),
        (r'operators', "opérateurs"),
        (r'boolean', "booléen"),
        (r'integer', "entier"),
        (r'integers', "entiers"),
        (r'float', "flottant"),
        (r'floats', "flottants"),
        (r'character', "caractère"),
        (r'characters', "caractères"),
        (r'sequence', "séquence"),
        (r'sequences', "séquences"),
        (r'collection', "collection"),
        (r'collections', "collections"),
        (r'structure', "structure"),
        (r'structures', "structures"),
        (r'data type', "type de données"),
        (r'data', "données"),
        (r'output', "sortie"),
        (r'input', "entrée"),
        (r'result', "résultat"),
        (r'results', "résultats"),
        (r'error', "erreur"),
        (r'errors', "erreurs"),
        (r'exception', "exception"),
        (r'exceptions', "exceptions"),
        (r'pattern', "motif"),
        (r'patterns', "motifs"),
        (r'file', "fichier"),
        (r'files', "fichiers"),
        (r'folder', "dossier"),
        (r'path', "chemin"),
        (r'directory', "répertoire"),
        (r'module', "module"),
        (r'modules', "modules"),
        (r'package', "paquet"),
        (r'library', "bibliothèque"),
        (r'libraries', "bibliothèques"),
        (r'code', "code"),
        (r'algorithm', "algorithme"),
        (r'algorithms', "algorithmes"),
        (r'syntax', "syntaxe"),
        (r'logic', "logique"),
        (r'requirement', "prérequis"),
        (r'requirements', "prérequis"),
        (r'behavior', "comportement"),
        (r'behaviors', "comportements"),
        (r'operation', "opération"),
        (r'operations', "opérations"),
        (r'calculation', "calcul"),
        (r'calculations', "calculs"),
        (r'computation', "calcul"),
        (r'computations', "calculs"),
        (r'implementation', "implémentation"),
        (r'implementations', "implémentations"),
        (r'approach', "approche"),
        (r'approaches', "approches"),
        (r'solution', "solution"),
        (r'solutions', "solutions"),
        (r'test case', "cas de test"),
        (r'test cases', "cas de test"),
        (r'breakpoint', "point d'arrêt"),
        (r'debug', "déboguer"),
        (r'debugging', "débogage"),
        
        # === VERBS (3rd person, common in educational comments) ===
        (r'calculates', "calcule"),
        (r'computes', "calcule"),
        (r'extracts', "extrait"),
        (r'converts', "convertit"),
        (r'transforms', "transforme"),
        (r'creates', "crée"),
        (r'generates', "génère"),
        (r'produces', "produit"),
        (r'returns', "retourne"),
        (r'prints', "affiche"),
        (r'displays', "affiche"),
        (r'shows', "montre"),
        (r'checks', "vérifie"),
        (r'verifies', "vérifie"),
        (r'validates', "valide"),
        (r'determines', "détermine"),
        (r'evaluates', "évalue"),
        (r'tests', "teste"),
        (r'compares', "compare"),
        (r'matches', "correspond à"),
        (r'filters', "filtre"),
        (r'reduces', "réduit"),
        (r'maps', "mappe"),
        (r'sorts', "trie"),
        (r'reverses', "inverse"),
        (r'merges', "fusionne"),
        (r'joins', "assemble"),
        (r'splits', "divise"),
        (r'divides', "divise"),
        (r'multiplies', "multiplie"),
        (r'adds', "ajoute"),
        (r'appends', "ajoute"),
        (r'removes', "supprime"),
        (r'deletes', "supprime"),
        (r'inserts', "insère"),
        (r'updates', "met à jour"),
        (r'modifies', "modifie"),
        (r'stores', "stocke"),
        (r'represents', "représente"),
        (r'contains', "contient"),
        (r'holds', "contient"),
        (r'defines', "définit"),
        (r'declares', "déclare"),
        (r'initializes', "initialise"),
        (r'assigns', "assigne"),
        (r'performs', "effectue"),
        (r'executes', "exécute"),
        (r'runs', "exécute"),
        (r'processes', "traite"),
        (r'handles', "gère"),
        (r'manages', "gère"),
        (r'implements', "implémente"),
        (r'overrides', "remplace"),
        (r'inherits', "hérite"),
        (r'calls', "appelle"),
        (r'invokes', "invoque"),
        (r'passes', "passe"),
        (r'receives', "reçoit"),
        (r'accepts', "accepte"),
        (r'requires', "nécessite"),
        (r'uses', "utilise"),
        (r'applies', "applique"),
        (r'demonstrates', "démontre"),
        (r'illustrates', "illustre"),
        (r'represents', "représente"),
        (r'indicates', "indique"),
        (r'specifies', "spécifie"),
        (r'identifies', "identifie"),
        (r'counts', "compte"),
        (r'tracks', "suit"),
        (r'finds', "trouve"),
        (r'searches', "recherche"),
        (r'iterates', "itère"),
        (r'navigates', "navigue"),
        (r'traverses', "parcourt"),
        (r'assembles', "assemble"),
        (r'builds', "construit"),
        (r'constructs', "construit"),
        (r'formats', "formate"),
        (r'encodes', "encode"),
        (r'decodes', "décode"),
        (r'parses', "analyse"),
        (r'reads', "lit"),
        (r'writes', "écrit"),
        (r'opens', "ouvre"),
        (r'closes', "ferme"),
        
        # === VERB FORMS (infinitive, past) ===
        (r'to calculate', "pour calculer"),
        (r'to compute', "pour calculer"),
        (r'to check', "pour vérifier"),
        (r'to test', "pour tester"),
        (r'to create', "pour créer"),
        (r'to generate', "pour générer"),
        (r'to find', "pour trouver"),
        (r'to get', "pour obtenir"),
        (r'to set', "pour définir"),
        (r'to update', "pour mettre à jour"),
        (r'to modify', "pour modifier"),
        (r'to remove', "pour supprimer"),
        (r'to delete', "pour supprimer"),
        (r'to add', "pour ajouter"),
        (r'to insert', "pour insérer"),
        (r'to store', "pour stocker"),
        (r'to hold', "pour contenir"),
        (r'to represent', "pour représenter"),
        (r'to process', "pour traiter"),
        (r'to handle', "pour gérer"),
        (r'to implement', "pour implémenter"),
        (r'to convert', "pour convertir"),
        (r'to transform', "pour transformer"),
        (r'to iterate', "pour itérer"),
        (r'to loop', "pour boucler"),
        (r'to sort', "pour trier"),
        (r'to filter', "pour filtrer"),
        (r'to return', "pour retourner"),
        (r'to print', "pour afficher"),
        (r'to display', "pour afficher"),
        (r'to output', "pour produire"),
        (r'to compare', "pour comparer"),
        (r'to split', "pour diviser"),
        (r'to join', "pour assembler"),
        
        (r'used to', "utilisé pour"),
        (r'used for', "utilisé pour"),
        (r'can be used', "peut être utilisé"),
        (r'is used', "est utilisé"),
        (r'are used', "sont utilisés"),
        (r'is called', "est appelé"),
        (r'is known as', "est connu comme"),
        (r'is defined', "est défini"),
        (r'is declared', "est déclaré"),
        (r'is created', "est créé"),
        (r'is assigned', "est assigné"),
        (r'is initialized', "est initialisé"),
        (r'is passed', "est passé"),
        (r'is returned', "est retourné"),
        (r'is printed', "est affiché"),
        (r'is displayed', "est affiché"),
        (r'is stored', "est stocké"),
        (r'is executed', "est exécuté"),
        (r'is called with', "est appelé avec"),
        (r'is similar to', "est similaire à"),
        (r'is equivalent to', "est équivalent à"),
        (r'is the same as', "est le même que"),
        
        (r'called with', "appelé avec"),
        (r'passed to', "passé à"),
        (r'passed in', "passé en"),
        (r'passed as', "passé comme"),
        (r'assigned to', "assigné à"),
        (r'stored in', "stocké dans"),
        (r'stored as', "stocké comme"),
        
        # === ADJECTIVES ===
        (r'reusable', "réutilisable"),
        (r'efficient', "efficace"),
        (r'efficiently', "efficacement"),
        (r'conditional', "conditionnel"),
        (r'conditional logic', "logique conditionnelle"),
        (r'memory-efficient', "économe en mémoire"),
        (r'functionally identical', "fonctionnellement identique"),
        (r'readable', "lisible"),
        (r'concise', "concis"),
        (r'compact', "compact"),
        (r'explicit', "explicite"),
        (r'optional', "optionnel"),
        (r'required', "requis"),
        (r'necessary', "nécessaire"),
        (r'alternative', "alternatif"),
        (r'original', "original"),
        (r'modified', "modifié"),
        (r'temporary', "temporaire"),
        (r'permanent', "permanent"),
        (r'current', "actuel"),
        (r'previous', "précédent"),
        (r'following', "suivant"),
        (r'previous', "précédent"),
        (r'remaining', "restant"),
        (r'available', "disponible"),
        (r'specific', "spécifique"),
        (r'appropriate', "approprié"),
        (r'correct', "correct"),
        (r'incorrect', "incorrect"),
        (r'valid', "valide"),
        (r'invalid', "invalide"),
        (r'expected', "attendu"),
        (r'unexpected', "inattendu"),
        (r'common', "courant"),
        (r'common pitfalls', "pièges courants"),
        (r'best practices', "bonnes pratiques"),
        (r'typical', "typique"),
        
        # === PHRASAL / LONGER PATTERNS ===
        (r'This demonstrates', "Cela démontre"),
        (r'This shows', "Cela montre"),
        (r'This means', "Cela signifie"),
        (r'This is because', "C'est parce que"),
        (r'This is why', "C'est pourquoi"),
        (r'In other words', "En d'autres termes"),
        (r'In this case', "Dans ce cas"),
        (r'In this context', "Dans ce contexte"),
        (r'In this example', "Dans cet exemple"),
        (r'In practice', "En pratique"),
        (r'In general', "En général"),
        (r'In particular', "En particulier"),
        (r'At this point', "À ce stade"),
        (r'By default', "Par défaut"),
        (r'For instance', "Par exemple"),
        (r'For example', "Par exemple"),
        (r'For this reason', "Pour cette raison"),
        (r'On the other hand', "D'autre part"),
        (r'As a result', "En conséquence"),
        (r'As mentioned', "Comme mentionné"),
        (r'As shown', "Comme montré"),
        (r'As seen', "Comme vu"),
        (r'Note that', "Notez que"),
        (r'Note :', "Remarque :"),
        (r'Notice that', "Remarquez que"),
        (r'Keep in mind that', "Gardez à l'esprit que"),
        (r'It is important to', "Il est important de"),
        (r'It is worth noting', "Il convient de noter"),
        (r'One thing to note', "Une chose à noter"),
        (r'Make sure to', "Assurez-vous de"),
        (r'Be careful', "Soyez prudent"),
        (r'Be careful not to', "Attention à ne pas"),
        
        # === PHRASAL VERBS ===
        (r'carried out', "effectué"),
        (r'carries out', "effectue"),
        (r'sets up', "configure"),
        (r'set up', "configurer"),
        (r'breaks down', "décompose"),
        (r'broken down', "décomposé"),
        (r'builds upon', "construit sur"),
        (r'built upon', "construit sur"),
        (r'makes use of', "utilise"),
        (r'make use of', "utiliser"),
        (r'takes advantage of', "profite de"),
        (r'take advantage of', "profiter de"),
        (r'consists of', "se compose de"),
        (r'consist of', "se composer de"),
        (r'deals with', "traite de"),
        (r'refers to', "fait référence à"),
        (r'rely on', "dépendre de"),
        (r'relies on', "dépend de"),
        (r'depends on', "dépend de"),
        (r'results in', "aboutit à"),
        (r'leads to', "conduit à"),
        (r'points to', "pointe vers"),
        (r'corresponds to', "correspond à"),
        (r'contributes to', "contribue à"),
        (r'applies to', "s'applique à"),
        (r'belongs to', "appartient à"),
        (r'occurs when', "se produit quand"),
        (r'happens when', "arrive quand"),
        (r'works by', "fonctionne en"),
        (r'starts by', "commence par"),
        (r'ends with', "se termine par"),
        (r'begins with', "commence par"),
        (r'followed by', "suivi de"),
        (r'followed by', "suivi par"),
        
        # === COMMENT LABELS ===
        (r'# Calculate', "# Calcule"),
        (r'# Compute', "# Calcule"),
        (r'# Return', "# Retourne"),
        (r'# Returns', "# Retourne"),
        (r'# Print', "# Affiche"),
        (r'# Prints', "# Affiche"),
        (r'# Display', "# Affiche"),
        (r'# Check', "# Vérifie"),
        (r'# Test', "# Teste"),
        (r'# Create', "# Crée"),
        (r'# Generate', "# Génère"),
        (r'# Get', "# Obtient"),
        (r'# Set', "# Définit"),
        (r'# Update', "# Met à jour"),
        (r'# Modify', "# Modifie"),
        (r'# Add', "# Ajoute"),
        (r'# Append', "# Ajoute"),
        (r'# Remove', "# Supprime"),
        (r'# Delete', "# Supprime"),
        (r'# Store', "# Stocke"),
        (r'# Define', "# Définit"),
        (r'# Initialize', "# Initialise"),
        (r'# Assign', "# Assigne"),
        (r'# Convert', "# Convertit"),
        (r'# Loop', "# Boucle"),
        (r'# Iterate', "# Itère"),
        (r'# Sort', "# Trie"),
        (r'# Filter', "# Filtre"),
        (r'# Compare', "# Compare"),
        (r'# Extract', "# Extrait"),
        (r'# Merge', "# Fusionne"),
        (r'# Join', "# Assemble"),
        (r'# Split', "# Divise"),
        (r'# Parse', "# Analyse"),
        (r'# File', "# Fichier"),
        (r'# Open', "# Ouvre"),
        (r'# Close', "# Ferme"),
        (r'# Read', "# Lit"),
        (r'# Write', "# Écrit"),
        (r'# Call', "# Appelle"),
        (r'# Output:', "# Sortie :"),
        (r'# Output', "# Sortie"),
        (r'# Input:', "# Entrée :"),
        (r'# Input', "# Entrée"),
        
        # === NUMBER WORDS ===
        (r'two numbers', "deux nombres"),
        (r'three numbers', "trois nombres"),
        (r'first parameter', "premier paramètre"),
        (r'second parameter', "deuxième paramètre"),
        (r'third parameter', "troisième paramètre"),
        (r'first element', "premier élément"),
        (r'last element', "dernier élément"),
        (r'first item', "premier élément"),
        (r'last item', "dernier élément"),
        
        # === PREPOSITIONAL ===
        (r'in the list', "dans la liste"),
        (r'in the string', "dans la chaîne"),
        (r'in the dictionary', "dans le dictionnaire"),
        (r'in the array', "dans le tableau"),
        (r'in the file', "dans le fichier"),
        (r'in the output', "dans la sortie"),
        (r'in the input', "dans l'entrée"),
        (r'in the result', "dans le résultat"),
        (r'in the code', "dans le code"),
        (r'of the function', "de la fonction"),
        (r'of the program', "du programme"),
        (r'of the list', "de la liste"),
        (r'of the string', "de la chaîne"),
        (r'of the dictionary', "du dictionnaire"),
        (r'of the file', "du fichier"),
        (r'of the result', "du résultat"),
        (r'to the function', "à la fonction"),
        (r'to the list', "à la liste"),
        (r'to the string', "à la chaîne"),
        (r'to the dictionary', "au dictionnaire"),
        (r'to the file', "au fichier"),
        
        # === CONJUNCTIONS / FUNCTION WORDS ===
        (r'which means', "ce qui signifie"),
        (r'which allows', "ce qui permet"),
        (r'which makes', "ce qui rend"),
        (r'which ensures', "ce qui garantit"),
        (r'which also', "ce qui aussi"),
        
        # === ===== BORDER ====
        (r'^# (=+)$', r'# \1'),
    ]
    
    return replacements


def translate_text(text, replacements):
    """Apply replacements to text."""
    for pattern, replacement in replacements:
        if callable(replacement):
            text = re.sub(pattern, replacement, text)
        else:
            try:
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
            except:
                pass
    # Cleanup
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+,', ',', text)
    text = re.sub(r'\s+:', ':', text)
    return text


def translate_comment_line(line, replacements):
    """Translate a comment line (line starting with #)."""
    if not line.strip().startswith('#'):
        return line
    # Extract the # comment portion
    idx = line.index('#')
    indent = line[:idx]
    comment = line[idx:]
    # Translate the comment text
    translated = translate_text(comment, replacements)
    return indent + translated


def translate_docstring(text, replacements):
    """Translate docstring content (text between triple quotes)."""
    return translate_text(text, replacements)


def process_file(input_path, output_path):
    """Process a single .py file and write translated version."""
    with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    replacements = load_translation_dict()
    lines = content.split('\n')
    output_lines = []
    in_docstring = False
    docstring_char = '"""'
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for docstring start/end (triple quotes)
        if stripped.startswith('"""') or stripped.startswith("'''"):
            # Check if it's a single-line docstring
            if (stripped.startswith('"""') and stripped.count('"""') >= 2 and len(stripped) > 6) or \
               (stripped.startswith("'''") and stripped.count("'''") >= 2 and len(stripped) > 6):
                # Single-line docstring: translate the content inside quotes
                # Extract content between quotes
                if stripped.startswith('"""'):
                    match = re.match(r'(""")(.*?)(""")', stripped)
                else:
                    match = re.match(r"(''')(.*?)(''')", stripped)
                if match:
                    indent = line[:len(line) - len(line.lstrip())]
                    q1, content_text, q2 = match.group(1), match.group(2), match.group(3)
                    translated = translate_text(content_text, replacements)
                    output_lines.append(f"{indent}{q1}{translated}{q2}")
                    i += 1
                    continue
            
            if not in_docstring:
                in_docstring = True
                docstring_char = '"""' if stripped.startswith('"""') else "'''"
                # Translate the opening line content after the quotes
                rest = stripped[3:].strip()
                if rest and not rest.endswith('"""') and not rest.endswith("'''"):
                    indent = line[:len(line) - len(line.lstrip())]
                    translated_rest = translate_text(rest, replacements)
                    output_lines.append(f"{indent}{docstring_char}{translated_rest}")
                    i += 1
                    continue
                output_lines.append(line)
                i += 1
                continue
            else:
                # Closing docstring
                in_docstring = False
                # Translate content on closing line before the quotes
                rest = stripped[:-3].strip()
                if rest:
                    indent = line[:len(line) - len(line.lstrip())]
                    translated_rest = translate_text(rest, replacements)
                    output_lines.append(f"{indent}{translated_rest}{docstring_char}")
                    i += 1
                    continue
                output_lines.append(line)
                i += 1
                continue
        
        if in_docstring:
            # Translate content inside docstring
            translated = translate_text(line, replacements)
            output_lines.append(translated)
            i += 1
            continue
        
        # Regular comment line
        if stripped.startswith('#'):
            output_lines.append(translate_comment_line(line, replacements))
            i += 1
            continue
        
        # Regular code line - check for inline comments
        if '#' in line and not stripped.startswith('#') and not stripped.startswith('"') and not stripped.startswith("'"):
            # Check if # is inside a string
            in_string = False
            string_char = None
            hash_idx = -1
            
            for j, ch in enumerate(line):
                if ch in ('"', "'") and (j == 0 or line[j-1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_char = ch
                    elif ch == string_char:
                        in_string = False
                        string_char = None
                elif ch == '#' and not in_string:
                    hash_idx = j
                    break
            
            if hash_idx >= 0:
                before = line[:hash_idx]
                comment = line[hash_idx:]
                translated_comment = translate_text(comment, replacements)
                output_lines.append(before + translated_comment)
                i += 1
                continue
        
        output_lines.append(line)
        i += 1
    
    result = '\n'.join(output_lines)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    return len(output_lines)


def main():
    base_dir = '/Users/moll/Desktop/python_app'
    files = [
        'level1_500_codelogic.py',
        'level1_500_requirements.py',
        'level1_500_syntax.py',
        'level1_1000_codelogic.py',
        'level1_1000_requirements..py',
        'level1_1000_syntax.py',
        'level1_1500_codelogic.py',
        'level1_1500_requirements.py',
        'level1_1500_syntax.py',
        'level1_2000_codelogic.py',
        'level1_2000_requirements..py',
        'level1_2000_syntax.py',
    ]
    
    total_lines = 0
    for fname in files:
        input_path = f'{base_dir}/{fname}'
        if not os.path.exists(input_path):
            print(f"SKIP: {fname} not found")
            continue
        
        # Create _fr filename
        base, ext = os.path.splitext(fname)
        base = base.rstrip('.')
        output_name = f'{base}_fr.py'
        output_path = f'{base_dir}/{output_name}'
        
        print(f"Processing: {fname} -> {output_name}")
        lines = process_file(input_path, output_path)
        total_lines += lines
        print(f"  Lines: {lines}")
    
    print(f"\nTotal lines processed: {total_lines}")
    
    # Now copy the _fr.py files to public/ and dist/
    print("\nCopying to public/ and dist/...")
    for d in ['public', 'dist']:
        dest_dir = f'{base_dir}/{d}'
        if os.path.exists(dest_dir):
            for fname in files:
                base, ext = os.path.splitext(fname)
                base = base.rstrip('.')
                fr_name = f'{base}_fr.py'
                src = f'{base_dir}/{fr_name}'
                dst = f'{dest_dir}/{fr_name}'
                if os.path.exists(src):
                    import shutil
                    shutil.copy2(src, dst)
                    print(f"  Copied {fr_name} to {d}/")
    
    print("\nDone!")

if __name__ == '__main__':
    main()

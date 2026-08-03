#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const START_ID = 5708;
const PACK_SIZE = 50;
const specs = [];

const py = value => {
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (value === null) return 'None';
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(py).join(', ')}]`;
  if (typeof value === 'object') return `{${Object.entries(value).map(([key, item]) => `${py(key)}: ${py(item)}`).join(', ')}}`;
  return String(value);
};

const cases = (inputs, evaluate) => inputs.map(args => ({ args, expected: evaluate(...args) }));
const add = spec => specs.push({ ...spec, body: spec.body.trim(), level: 'Easy' });

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`count_step_${c}_while`, 'limit', `count positive multiples of ${c + 1} that do not exceed \`limit\``, `compte les multiples positifs de ${c + 1} qui ne dépassent pas \`limit\``, `value = ${c + 1}\n    count = 0\n    while value <= limit:\n        count += 1\n        value += ${c + 1}\n    return count`, cases([[10], [0], [17]], limit => Math.floor(Math.max(limit, 0) / (c + 1)))],
    [`sum_step_${c}_while`, 'limit', `sum positive multiples of ${c + 1} through \`limit\``, `additionne les multiples positifs de ${c + 1} jusqu’à \`limit\``, `value = ${c + 1}\n    total = 0\n    while value <= limit:\n        total += value\n        value += ${c + 1}\n    return total`, cases([[12], [1], [25]], limit => { let total = 0; for (let value = c + 1; value <= limit; value += c + 1) total += value; return total; })],
    [`build_sequence_${c}_while`, 'start, count', `build \`count\` values beginning at \`start\` and increasing by ${c}`, `construit \`count\` valeurs à partir de \`start\` avec un pas de ${c}`, `result = []\n    while len(result) < count:\n        result.append(start)\n        start += ${c}\n    return result`, cases([[2, 4], [-3, 3], [8, 0]], (start, count) => Array.from({ length: count }, (_, offset) => start + offset * c))],
    [`repeat_text_${c}_while`, 'text', `repeat \`text\` exactly ${c} times without using string multiplication`, `répète \`text\` exactement ${c} fois sans multiplication de chaîne`, `result = ""\n    count = 0\n    while count < ${c}:\n        result += text\n        count += 1\n    return result`, cases([['ab'], ['x'], ['']], text => text.repeat(c))],
    [`count_above_${c}_while`, 'values', `count list values greater than ${c}`, `compte les valeurs de liste supérieures à ${c}`, `index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > ${c}:\n            count += 1\n        index += 1\n    return count`, cases([[[0, 2, 5, 9]], [[c, c + 1]], [[]]], values => values.filter(value => value > c).length)],
    [`first_below_${c}_while`, 'values', `return the first index containing a value below ${c}, or -1`, `retourne le premier indice d’une valeur inférieure à ${c}, ou -1`, `index = 0\n    while index < len(values):\n        if values[index] < ${c}:\n            return index\n        index += 1\n    return -1`, cases([[[9, c - 1, 8]], [[c, c + 1]], [[c - 2]]], values => values.findIndex(value => value < c))],
    [`reach_target_${c}_while`, 'start, target', `add ${c} until \`start\` reaches or passes \`target\`, then return the result`, `ajoute ${c} jusqu’à ce que \`start\` atteigne ou dépasse \`target\`, puis retourne le résultat`, `while start < target:\n        start += ${c}\n    return start`, cases([[0, 11], [5, 5], [-2, 7]], (start, target) => { while (start < target) start += c; return start; })],
    [`take_prefix_${c}_while`, 'items', `return at most the first ${c} list items`, `retourne au maximum les ${c} premiers éléments de la liste`, `index = 0\n    result = []\n    while index < len(items) and index < ${c}:\n        result.append(items[index])\n        index += 1\n    return result`, cases([[[1, 2, 3, 4, 5, 6]], [['a']], [[]]], items => items.slice(0, c))],
    [`replace_negative_${c}_while`, 'values', `replace every negative list value with ${c}`, `remplace chaque valeur négative de la liste par ${c}`, `index = 0\n    result = []\n    while index < len(values):\n        result.append(${c} if values[index] < 0 else values[index])\n        index += 1\n    return result`, cases([[[-2, 0, 4, -1]], [[1, 2]], [[]]], values => values.map(value => value < 0 ? c : value))],
    [`running_total_${c}_while`, 'values', `return running totals that begin with an initial total of ${c}`, `retourne les totaux cumulés commençant avec un total initial de ${c}`, `index = 0\n    total = ${c}\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result`, cases([[[1, 2, 3]], [[-1, 4]], [[]]], values => { let total = c; return values.map(value => total += value); })],
  ];
  const [name, params, en, fr, body, testCases] = definitions[family];
  add({ concept: 'While Loop', name, params, en, fr, body, cases: testCases, nodes: [{ nodeType: 'While', minCount: 1 }], focus: 'the starting state, stopping condition, and state update' });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const numeric = [[-8], [c], [c + 6]];
  const definitions = [
    [`inside_${c}_boolean`, 'value', `return whether \`value\` is between ${-c} and ${c}, inclusive`, `retourne si \`value\` est compris entre ${-c} et ${c}, bornes incluses`, `return value >= ${-c} and value <= ${c}`, cases(numeric, value => value >= -c && value <= c), ['And']],
    [`outside_${c}_boolean`, 'value', `return whether \`value\` is below ${-c} or above ${c}`, `retourne si \`value\` est inférieur à ${-c} ou supérieur à ${c}`, `return value < ${-c} or value > ${c}`, cases(numeric, value => value < -c || value > c), ['Or']],
    [`positive_even_after_${c}`, 'value', `return whether \`value\` is both greater than ${c} and even`, `retourne si \`value\` est à la fois supérieur à ${c} et pair`, `return value > ${c} and value % 2 == 0`, cases([[c], [c + 1], [c + 4]], value => value > c && value % 2 === 0), ['And']],
    [`divisible_choice_${c}`, 'value', `return whether \`value\` is divisible by ${c + 1} or ${c + 2}`, `retourne si \`value\` est divisible par ${c + 1} ou ${c + 2}`, `return value % ${c + 1} == 0 or value % ${c + 2} == 0`, cases([[c + 1], [c + 2], [(c + 1) * (c + 2) + 1]], value => value % (c + 1) === 0 || value % (c + 2) === 0), ['Or']],
    [`not_outside_${c}`, 'value', `use \`not\` to return whether \`value\` stays within ${-c} and ${c}`, `utilise \`not\` pour retourner si \`value\` reste entre ${-c} et ${c}`, `return not (value < ${-c} or value > ${c})`, cases(numeric, value => !(value < -c || value > c)), ['Or']],
    [`text_starts_${c}_boolean`, 'text', `return whether text is non-empty and starts with ${py(String(c))}`, `retourne si le texte n’est pas vide et commence par ${py(String(c))}`, `return bool(text) and text.startswith(${py(String(c))})`, cases([[`${c}abc`], [''], [`x${c}`]], text => Boolean(text) && text.startsWith(String(c))), ['And']],
    [`valid_text_length_${c}`, 'text', `return whether the input is a string and has at least ${c} characters`, `retourne si l’entrée est une chaîne d’au moins ${c} caractères`, `return isinstance(text, str) and len(text) >= ${c}`, cases([['python'], ['x'], [42]], text => typeof text === 'string' && text.length >= c), ['And']],
    [`exactly_one_above_${c}`, 'left, right', `return whether exactly one value is greater than ${c}`, `retourne si exactement une valeur est supérieure à ${c}`, `return (left > ${c}) != (right > ${c})`, cases([[c + 1, c], [c + 2, c + 3], [c - 1, c]], (left, right) => (left > c) !== (right > c)), []],
    [`flags_ready_${c}`, 'first, second, blocked', `return whether both readiness flags are true and the blocked flag is false for check ${c}`, `retourne si les deux indicateurs sont vrais et l’indicateur bloqué est faux pour le contrôle ${c}`, 'return first and second and not blocked', cases([[true, true, false], [true, false, false], [true, true, true]], (first, second, blocked) => first && second && !blocked), ['And']],
    [`score_band_${c}`, 'score', `return whether \`score\` lies from ${c * 10} through ${c * 10 + 20}`, `retourne si \`score\` se situe de ${c * 10} à ${c * 10 + 20}`, `return score >= ${c * 10} and score <= ${c * 10 + 20}`, cases([[c * 10], [c * 10 + 21], [c * 10 + 10]], score => score >= c * 10 && score <= c * 10 + 20), ['And']],
  ];
  const [name, params, en, fr, body, testCases, boolOps] = definitions[family];
  add({ concept: 'Boolean Logic', name, params, en, fr, body, cases: testCases, boolOps, focus: 'the truth value of each comparison and the short-circuit order' });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`length_plus_${c}_builtin`, 'items', `use the built-in \`len()\` and add ${c} to the length`, `utilise la fonction intégrée \`len()\` et ajoute ${c} à la longueur`, `return len(items) + ${c}`, cases([[[1, 2, 3]], [[]], ['code']], items => items.length + c), 'len'],
    [`sum_plus_${c}_builtin`, 'values', `use the built-in \`sum()\` and add ${c} to the total`, `utilise la fonction intégrée \`sum()\` et ajoute ${c} au total`, `return sum(values) + ${c}`, cases([[[1, 2, 3]], [[-2, 5]], [[]]], values => values.reduce((a, b) => a + b, 0) + c), 'sum'],
    [`safe_max_${c}_builtin`, 'values', `use the built-in \`max()\` with default ${c} for an empty list`, `utilise la fonction intégrée \`max()\` avec ${c} par défaut pour une liste vide`, `return max(values, default=${c})`, cases([[[1, 8, 3]], [[]], [[-5, -2]]], values => values.length ? Math.max(...values) : c), 'max'],
    [`safe_min_${c}_builtin`, 'values', `use the built-in \`min()\` with default ${-c} for an empty list`, `utilise la fonction intégrée \`min()\` avec ${-c} par défaut pour une liste vide`, `return min(values, default=${-c})`, cases([[[1, 8, 3]], [[]], [[-5, -2]]], values => values.length ? Math.min(...values) : -c), 'min'],
    [`descending_marker_${c}_builtin`, 'values', `use the built-in \`sorted()\` to sort descending, then append ${c}`, `utilise la fonction intégrée \`sorted()\` pour trier en ordre décroissant, puis ajoute ${c}`, `return sorted(values, reverse=True) + [${c}]`, cases([[[3, 1, 2]], [[]], [[-1, 4]]], values => [...values].sort((a, b) => b - a).concat(c)), 'sorted'],
    [`round_to_${c}_builtin`, 'number', `use the built-in \`round()\` to keep ${c} decimal places`, `utilise la fonction intégrée \`round()\` pour conserver ${c} décimales`, `return round(number, ${c})`, cases([[3.1415926], [2.555555], [-1.234567]], number => Number(number.toFixed(c))), 'round'],
    [`distance_from_${c}_builtin`, 'value', `use the built-in \`abs()\` to measure distance from ${c}`, `utilise la fonction intégrée \`abs()\` pour mesurer la distance depuis ${c}`, `return abs(value - ${c})`, cases([[10], [-3], [c]], value => Math.abs(value - c)), 'abs'],
    [`any_above_${c}_builtin`, 'values', `use the built-in \`any()\` to test whether one value exceeds ${c}`, `utilise la fonction intégrée \`any()\` pour tester si une valeur dépasse ${c}`, `return any(value > ${c} for value in values)`, cases([[[0, c + 1]], [[c, c - 1]], [[]]], values => values.some(value => value > c)), 'any'],
    [`all_at_least_${c}_builtin`, 'values', `use the built-in \`all()\` to test whether every value is at least ${-c}`, `utilise la fonction intégrée \`all()\` pour tester si chaque valeur vaut au moins ${-c}`, `return all(value >= ${-c} for value in values)`, cases([[[0, 2]], [[-c - 1, 2]], [[]]], values => values.every(value => value >= -c)), 'all'],
    [`zip_with_marker_${c}_builtin`, 'keys, values', `use the built-ins \`zip()\` and \`dict()\`, then store marker ${c}`, `utilise les fonctions intégrées \`zip()\` et \`dict()\`, puis stocke le marqueur ${c}`, `result = dict(zip(keys, values))\n    result["marker"] = ${c}\n    return result`, cases([[['a', 'b'], [1, 2]], [['x'], [9]], [[], []]], (keys, values) => ({ ...Object.fromEntries(keys.map((key, i) => [key, values[i]])), marker: c })), 'zip'],
  ];
  const [name, params, en, fr, body, testCases, call] = definitions[family];
  add({ concept: 'Built-in', name, params, en, fr, body, cases: testCases, calls: [call], focus: 'the built-in signature, argument order, and returned type' });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`unique_count_plus_${c}_set`, 'values', `count unique values with a set, then add ${c}`, `compte les valeurs uniques avec un ensemble, puis ajoute ${c}`, `return len(set(values)) + ${c}`, cases([[[1, 1, 2]], [[]], [['a', 'b', 'a']]], values => new Set(values).size + c)],
    [`union_marker_${c}_set`, 'left, right', `return the sorted set union after adding marker ${c}`, `retourne l’union triée des ensembles après ajout du marqueur ${c}`, `return sorted(set(left).union(right, {${c}}))`, cases([[[1, 2], [2, 3]], [[], [4]], [[c], [c]]], (left, right) => [...new Set([...left, ...right, c])].sort((a, b) => a - b))],
    [`intersection_without_${c}_set`, 'left, right', `return the sorted set intersection after removing ${c}`, `retourne l’intersection triée des ensembles après retrait de ${c}`, `return sorted(set(left).intersection(right) - {${c}})`, cases([[[1, 2, 3], [2, 3]], [[c], [c]], [[], [1]]], (left, right) => [...new Set(left.filter(value => new Set(right).has(value) && value !== c))].sort((a, b) => a - b))],
    [`difference_marker_${c}_set`, 'left, right', `return the sorted set difference and include marker ${c}`, `retourne la différence triée des ensembles et inclut le marqueur ${c}`, `return sorted(set(left).difference(right).union({${c}}))`, cases([[[1, 2, 3], [2]], [[c], [c]], [[], []]], (left, right) => [...new Set([...left.filter(value => !new Set(right).has(value)), c])].sort((a, b) => a - b))],
    [`symmetric_size_${c}_set`, 'left, right', `return the symmetric-difference size plus ${c}`, `retourne la taille de la différence symétrique plus ${c}`, `return len(set(left).symmetric_difference(right)) + ${c}`, cases([[[1, 2], [2, 3]], [[], []], [[1], [2]]], (left, right) => [...new Set([...left, ...right])].filter(value => new Set(left).has(value) !== new Set(right).has(value)).length + c)],
    [`required_subset_${c}_set`, 'required, values', `test whether required values form a subset after ${c} is added`, `teste si les valeurs requises forment un sous-ensemble après ajout de ${c}`, `return set(required).issubset(set(values).union({${c}}))`, cases([[[1, c], [1]], [[9], [1, 2]], [[], []]], (required, values) => required.every(value => new Set([...values, c]).has(value)))],
    [`disjoint_except_${c}_set`, 'left, right', `test whether sets are disjoint after ignoring value ${c}`, `teste si les ensembles sont disjoints après avoir ignoré la valeur ${c}`, `return (set(left) - {${c}}).isdisjoint(set(right) - {${c}})`, cases([[[1, c], [2, c]], [[1, 2], [2, 3]], [[], [c]]], (left, right) => !left.some(value => value !== c && new Set(right.filter(item => item !== c)).has(value)))],
    [`unique_remainders_${c}_set`, 'values', `return sorted unique remainders modulo ${c + 2} using a set`, `retourne les restes uniques triés modulo ${c + 2} avec un ensemble`, `return sorted({value % ${c + 2} for value in values})`, cases([[[1, 2, 3, 4, 5]], [[]], [[-1, c + 2]]], values => [...new Set(values.map(value => ((value % (c + 2)) + c + 2) % (c + 2)))].sort((a, b) => a - b))],
    [`letter_set_without_${c}`, 'text', `return sorted unique characters except digit ${c}`, `retourne les caractères uniques triés sauf le chiffre ${c}`, `return sorted(set(text) - {${py(String(c))}})`, cases([[`a${c}ba`], [''], [`${c}${c}x`]], text => [...new Set([...text].filter(char => char !== String(c)))].sort())],
    [`set_values_at_least_${c}`, 'values', `return sorted unique values that are at least ${c}`, `retourne les valeurs uniques triées qui valent au moins ${c}`, `return sorted({value for value in values if value >= ${c}})`, cases([[[0, c, c + 1, c]], [[]], [[-2, 20]]], values => [...new Set(values.filter(value => value >= c))].sort((a, b) => a - b))],
  ];
  const [name, params, en, fr, body, testCases] = definitions[family];
  add({
    concept: 'Set', name, params, en, fr, body, cases: testCases,
    calls: family === 7 || family === 9 ? undefined : ['set'],
    nodes: family === 7 || family === 9 ? [{ nodeType: 'SetComp', minCount: 1 }] : undefined,
    focus: 'unique membership, the selected set operation, and deterministic sorted output',
  });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`square_plus_${c}_comprehension`, 'values', `return each value squared plus ${c} with a list comprehension`, `retourne chaque valeur au carré plus ${c} avec une compréhension de liste`, `return [value ** 2 + ${c} for value in values]`, cases([[[1, 2, 3]], [[-2, 0]], [[]]], values => values.map(value => value ** 2 + c)), 'ListComp'],
    [`divisible_${c}_comprehension`, 'values', `keep values divisible by ${c + 1} with a list comprehension`, `conserve les valeurs divisibles par ${c + 1} avec une compréhension de liste`, `return [value for value in values if value % ${c + 1} == 0]`, cases([[[1, 2, 3, 4, 6]], [[c + 1]], [[]]], values => values.filter(value => value % (c + 1) === 0)), 'ListComp'],
    [`mapping_plus_${c}_comprehension`, 'values', `map each value's text to that value plus ${c} with a dictionary comprehension`, `associe le texte de chaque valeur à cette valeur plus ${c} avec une compréhension de dictionnaire`, `return {str(value): value + ${c} for value in values}`, cases([[[1, 2]], [[-1, 0]], [[]]], values => Object.fromEntries(values.map(value => [String(value), value + c]))), 'DictComp'],
    [`remainder_${c}_comprehension`, 'values', `return sorted unique remainders modulo ${c + 2} with a set comprehension`, `retourne les restes uniques triés modulo ${c + 2} avec une compréhension d’ensemble`, `return sorted({value % ${c + 2} for value in values})`, cases([[[1, 2, 3, 4]], [[-1, c + 2]], [[]]], values => [...new Set(values.map(value => ((value % (c + 2)) + c + 2) % (c + 2)))].sort((a, b) => a - b)), 'SetComp'],
    [`uppercase_long_${c}_comprehension`, 'words', `uppercase words with at least ${c} characters using a list comprehension`, `met en majuscules les mots d’au moins ${c} caractères avec une compréhension de liste`, `return [word.upper() for word in words if len(word) >= ${c}]`, cases([[['a', 'python', 'code']], [['x']], [[]]], words => words.filter(word => word.length >= c).map(word => word.toUpperCase())), 'ListComp'],
    [`index_offset_${c}_comprehension`, 'values', `build a dictionary whose text keys are indexes starting at ${c}`, `construit un dictionnaire dont les clés textuelles sont des indices commençant à ${c}`, `return {str(index + ${c}): value for index, value in enumerate(values)}`, cases([[['a', 'b']], [[9]], [[]]], values => Object.fromEntries(values.map((value, index) => [String(index + c), value]))), 'DictComp'],
    [`flatten_plus_${c}_comprehension`, 'matrix', `flatten a matrix and add ${c} to each value with a comprehension`, `aplatit une matrice et ajoute ${c} à chaque valeur avec une compréhension`, `return [value + ${c} for row in matrix for value in row]`, cases([[[[1, 2], [3]]], [[[]]], [[]]], matrix => matrix.flat().map(value => value + c)), 'ListComp'],
    [`character_code_${c}_comprehension`, 'text', `return each character code plus ${c} with a list comprehension`, `retourne le code de chaque caractère plus ${c} avec une compréhension de liste`, `return [ord(char) + ${c} for char in text]`, cases([['abc'], ['A'], ['']], text => [...text].map(char => char.codePointAt(0) + c)), 'ListComp'],
    [`pair_sum_above_${c}_comprehension`, 'left, right', `return two-item lists whose sum exceeds ${c} using a nested comprehension`, `retourne des listes de deux éléments dont la somme dépasse ${c} avec une compréhension imbriquée`, `return [[a, b] for a in left for b in right if a + b > ${c}]`, cases([[[1, 3], [2, 4]], [[0], [0]], [[], [1]]], (left, right) => left.flatMap(a => right.filter(b => a + b > c).map(b => [a, b]))), 'ListComp'],
    [`comparison_flags_${c}_comprehension`, 'values', `return Boolean flags showing which values exceed ${c}`, `retourne des indicateurs booléens montrant quelles valeurs dépassent ${c}`, `return [value > ${c} for value in values]`, cases([[[0, c, c + 1]], [[]], [[10]]], values => values.map(value => value > c)), 'ListComp'],
  ];
  const [name, params, en, fr, body, testCases, nodeType] = definitions[family];
  add({ concept: 'Comprehension', name, params, en, fr, body, cases: testCases, nodes: [{ nodeType, minCount: 1 }], focus: 'the expression, iteration clauses, and optional filter order' });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`sum_plus_${c}_for`, 'values', `sum all values with a for loop, starting the total at ${c}`, `additionne toutes les valeurs avec une boucle for en commençant le total à ${c}`, `total = ${c}\n    for value in values:\n        total += value\n    return total`, cases([[[1, 2, 3]], [[]], [[-2, 5]]], values => values.reduce((a, b) => a + b, c))],
    [`count_divisible_${c}_for`, 'values', `count values divisible by ${c + 1} using a for loop`, `compte les valeurs divisibles par ${c + 1} avec une boucle for`, `count = 0\n    for value in values:\n        if value % ${c + 1} == 0:\n            count += 1\n    return count`, cases([[[1, 2, 3, 4, 6]], [[]], [[c + 1]]], values => values.filter(value => value % (c + 1) === 0).length)],
    [`square_offset_${c}_for`, 'values', `build a list of squares plus ${c} using a for loop`, `construit une liste de carrés plus ${c} avec une boucle for`, `result = []\n    for value in values:\n        result.append(value ** 2 + ${c})\n    return result`, cases([[[1, 2, 3]], [[]], [[-2]]], values => values.map(value => value ** 2 + c))],
    [`long_words_${c}_for`, 'words', `collect words with at least ${c} characters using a for loop`, `collecte les mots d’au moins ${c} caractères avec une boucle for`, `result = []\n    for word in words:\n        if len(word) >= ${c}:\n            result.append(word)\n    return result`, cases([[['a', 'python', 'code']], [[]], [['x'.repeat(c)]]], words => words.filter(word => word.length >= c))],
    [`positive_mapping_${c}_for`, 'values', `map each positive value's text to that value plus ${c} using a for loop`, `associe le texte de chaque valeur positive à cette valeur plus ${c} avec une boucle for`, `result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + ${c}\n    return result`, cases([[[-1, 1, 3]], [[]], [[2]]], values => Object.fromEntries(values.filter(value => value > 0).map(value => [String(value), value + c])))],
    [`target_index_${c}_for`, 'values, target', `find the first target index with a for loop, then add ${c} to a found index`, `trouve le premier indice cible avec une boucle for, puis ajoute ${c} à l’indice trouvé`, `for index, value in enumerate(values):\n        if value == target:\n            return index + ${c}\n    return -1`, cases([[[4, 7, 7], 7], [[1, 2], 9], [[], 1]], (values, target) => { const found = values.indexOf(target); return found < 0 ? -1 : found + c; })],
    [`flatten_rows_${c}_for`, 'matrix', `flatten rows with a for loop and append marker ${c}`, `aplatit les lignes avec une boucle for et ajoute le marqueur ${c}`, `result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(${c})\n    return result`, cases([[[[1, 2], [3]]], [[]], [[[]]]], matrix => matrix.flat().concat(c))],
    [`running_totals_${c}_for`, 'values', `return running totals beginning at ${c} using a for loop`, `retourne les totaux cumulés commençant à ${c} avec une boucle for`, `total = ${c}\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result`, cases([[[1, 2, 3]], [[]], [[-1, 4]]], values => { let total = c; return values.map(value => total += value); })],
    [`join_with_${c}_for`, 'items', `join item text with separator ${py(`-${c}-`)} using a for loop`, `joint le texte des éléments avec le séparateur ${py(`-${c}-`)} avec une boucle for`, `result = ""\n    for item in items:\n        if result:\n            result += ${py(`-${c}-`)}\n        result += str(item)\n    return result`, cases([[['a', 'b']], [[1]], [[]]], items => items.join(`-${c}-`))],
    [`count_digit_${c}_for`, 'text', `count digit ${c} in text using a for loop`, `compte le chiffre ${c} dans le texte avec une boucle for`, `count = 0\n    for char in text:\n        if char == ${py(String(c))}:\n            count += 1\n    return count`, cases([[`${c}a${c}`], ['abc'], ['']], text => [...text].filter(char => char === String(c)).length)],
  ];
  const [name, params, en, fr, body, testCases] = definitions[family];
  add({ concept: 'For Loop', name, params, en, fr, body, cases: testCases, nodes: [{ nodeType: 'For', minCount: 1 }], focus: 'the iterable, per-item operation, and final return position' });
}

for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 5);
  const c = index % 5 + 1;
  const definitions = [
    [`first_or_${c}_iterator`, 'values', `use an iterator to return the first value, or ${c} when empty`, `utilise un itérateur pour retourner la première valeur, ou ${c} si vide`, `iterator = iter(values)\n    return next(iterator, ${c})`, cases([[[9, 2]], [[]], [[-1]]], values => values.length ? values[0] : c), ['iter', 'next']],
    [`second_or_${c}_iterator`, 'values', `use an iterator to return the second value, or ${c} when unavailable`, `utilise un itérateur pour retourner la deuxième valeur, ou ${c} si indisponible`, `iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, ${c})`, cases([[[9, 2, 3]], [[1]], [[]]], values => values.length > 1 ? values[1] : c), ['iter', 'next']],
    [`take_${c}_iterator`, 'values', `take at most ${c} values by repeatedly calling \`next()\` on an iterator`, `prend au maximum ${c} valeurs en appelant plusieurs fois \`next()\` sur un itérateur`, `iterator = iter(values)\n    result = []\n    for _ in range(${c}):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result`, cases([[[1, 2, 3, 4, 5, 6]], [[9]], [[]]], values => values.slice(0, c)), ['iter', 'next']],
    [`iterator_sum_plus_${c}`, 'values', `sum an iterator and add ${c}`, `additionne un itérateur et ajoute ${c}`, `iterator = iter(values)\n    return sum(iterator) + ${c}`, cases([[[1, 2, 3]], [[]], [[-2, 5]]], values => values.reduce((a, b) => a + b, 0) + c), ['iter']],
    [`skip_${c}_iterator`, 'values, default', `skip ${c} iterator values and return the next one or \`default\``, `ignore ${c} valeurs de l’itérateur et retourne la suivante ou \`default\``, `iterator = iter(values)\n    for _ in range(${c}):\n        next(iterator, default)\n    return next(iterator, default)`, cases([[[1, 2, 3, 4, 5, 6], -1], [[9], 0], [[], 7]], (values, fallback) => values.length > c ? values[c] : fallback), ['iter', 'next']],
    [`first_pair_${c}_iterator`, 'values', `return the first two iterator values as a list, using ${c} for each missing value`, `retourne les deux premières valeurs de l’itérateur dans une liste en utilisant ${c} pour chaque valeur manquante`, `iterator = iter(values)\n    return [next(iterator, ${c}), next(iterator, ${c})]`, cases([[[1, 2, 3]], [[9]], [[]]], values => [values[0] ?? c, values[1] ?? c]), ['iter', 'next']],
    [`iterator_count_plus_${c}`, 'values', `count values consumed from an iterator and add ${c}`, `compte les valeurs consommées d’un itérateur et ajoute ${c}`, `iterator = iter(values)\n    count = ${c}\n    for _ in iterator:\n        count += 1\n    return count`, cases([[[1, 2, 3]], [[]], [['a']]], values => values.length + c), ['iter']],
    [`last_or_${c}_iterator`, 'values', `consume an iterator and return its last value, or ${c} when empty`, `consomme un itérateur et retourne sa dernière valeur, ou ${c} si vide`, `iterator = iter(values)\n    result = ${c}\n    for value in iterator:\n        result = value\n    return result`, cases([[[1, 2, 3]], [[]], [[-1]]], values => values.length ? values.at(-1) : c), ['iter']],
    [`iterator_all_above_${c}`, 'values', `use an iterator to test whether every value exceeds ${c}`, `utilise un itérateur pour tester si chaque valeur dépasse ${c}`, `iterator = iter(values)\n    for value in iterator:\n        if value <= ${c}:\n            return False\n    return True`, cases([[[c + 1, c + 2]], [[c, c + 2]], [[]]], values => values.every(value => value > c)), ['iter']],
    [`indexed_from_${c}_iterator`, 'values', `consume an iterator and pair values with indexes in two-item lists beginning at ${c}`, `consomme un itérateur et associe les valeurs à des indices dans des listes de deux éléments commençant à ${c}`, `iterator = iter(values)\n    result = []\n    index = ${c}\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result`, cases([[['a', 'b']], [[9]], [[]]], values => values.map((value, index) => [index + c, value])), ['iter']],
  ];
  const [name, params, en, fr, body, testCases, calls] = definitions[family];
  add({ concept: 'Iterator', name, params, en, fr, body, cases: testCases, calls, focus: 'creating the iterator, consuming values in order, and handling exhaustion safely' });
}

const expectedConcepts = ['While Loop', 'Boolean Logic', 'Built-in', 'Set', 'Comprehension', 'For Loop', 'Iterator'];
if (specs.length !== expectedConcepts.length * PACK_SIZE) throw new Error(`Expected 350 specs, found ${specs.length}`);
for (const concept of expectedConcepts) {
  const count = specs.filter(spec => spec.concept === concept).length;
  if (count !== PACK_SIZE) throw new Error(`${concept}: expected ${PACK_SIZE}, found ${count}`);
}
const names = specs.map(spec => spec.name);
if (new Set(names).size !== names.length) throw new Error('Generated function names must be unique.');

const labelFr = {
  'While Loop': 'boucle while', 'Boolean Logic': 'logique booléenne', 'Built-in': 'fonction intégrée',
  Set: 'ensemble', Comprehension: 'compréhension', 'For Loop': 'boucle for', Iterator: 'itérateur',
};
const exercises = [];
const graders = {};
const french = {};
const invoke = (spec, test) => `${spec.name}(${test.args.map(py).join(', ')})`;

specs.forEach((spec, index) => {
  const id = START_ID + index;
  const canonical = `def ${spec.name}(${spec.params}):\n    ${spec.body}`;
  const nestedBody = canonical.split('\n').slice(1).map(line => `    ${line}`).join('\n');
  const classBody = canonical.split('\n').map(line => `    ${line}`).join('\n');
  const solution = `# Example 1: canonical function approach\n${canonical}\n\nprint(${invoke(spec, spec.cases[0])})  # Expected: ${py(spec.cases[0].expected)}\nprint(${invoke(spec, spec.cases[1])})  # Expected: ${py(spec.cases[1].expected)}\n\n# Example 2: nested helper approach\ndef solve_problem_${id}(${spec.params}):\n    def calculate():\n${nestedBody}\n    return calculate()\n\nprint(${invoke({ ...spec, name: `solve_problem_${id}` }, spec.cases[0])})\n\n# Example 3: static method approach\nclass Problem${id}Solution:\n    @staticmethod\n${classBody}\n\nprint(Problem${id}Solution.${invoke(spec, spec.cases[1])})\n\n# Example 4: assigned result approach\nresult = ${invoke(spec, spec.cases[0])}\nprint(result)\n\n# Example 5: direct call\nprint(${invoke(spec, spec.cases[2])})`;
  const description = `Write a Python function called \`${spec.name}\` that must ${spec.en}. Practice ${spec.concept.toLowerCase()} syntax.\nDifficulty: Easy.\nExamples:\n  ${invoke(spec, spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec, spec.cases[1])} -> ${py(spec.cases[1].expected)}`;
  exercises.push({
    id, title: `Problem ${id}`, description, initialCode: `def ${spec.name}(${spec.params}):\n    pass`, solution,
    hint: `Focus on ${spec.focus}. Use the required ${spec.concept.toLowerCase()} structure instead of hard-coding an example.`,
    breakdown: `1. Identify each parameter and the required return type.\n2. Build the ${spec.concept.toLowerCase()} structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.`,
    category: `${spec.concept} Easy`,
  });
  const grader = { functionNames: [spec.name], tests: spec.cases };
  if (spec.nodes?.length) grader.requiredNodePatterns = spec.nodes;
  if (spec.calls?.length) grader.requiredCallPatterns = spec.calls.map(functionName => ({ functionName, minArgs: 0 }));
  if (spec.boolOps?.length) grader.requiredBoolOps = spec.boolOps;
  graders[id] = grader;
  french[id] = {
    description: `Écrivez une fonction Python appelée \`${spec.name}\` qui ${spec.fr}. Entraînez-vous avec la syntaxe de ${labelFr[spec.concept]}.\nDifficulté : Facile.\nExemples :\n  ${invoke(spec, spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec, spec.cases[1])} -> ${py(spec.cases[1].expected)}`,
    hint: `Concentrez-vous sur ${spec.focus}. Utilisez la structure de ${labelFr[spec.concept]} demandée au lieu de coder un exemple en dur.`,
    breakdown: `1. Identifiez chaque paramètre et le type de retour demandé.\n2. Construisez la structure de ${labelFr[spec.concept]} indiquée dans la consigne.\n3. Suivez le premier exemple opération par opération.\n4. Vérifiez l’entrée vide ou limite des tests cachés.\n5. Retournez la valeur terminée sans copier une sortie attendue.`,
  };
});

fs.writeFileSync(path.join(root, 'easyConceptPracticeExercises.ts'), `import type { Exercise } from './types';\n\nexport const EASY_CONCEPT_PRACTICE_EXERCISES: Exercise[] = ${JSON.stringify(exercises, null, 2)};\n`);
fs.writeFileSync(path.join(root, 'easyConceptPracticeGraders.ts'), `import type { AutoGrader } from './graders';\n\nexport const EASY_CONCEPT_PRACTICE_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders, null, 2)};\n`);
fs.writeFileSync(path.join(root, 'services/easyConceptPracticeFr.ts'), `export const EASY_CONCEPT_PRACTICE_FR: Record<number, { description: string; hint: string; breakdown: string }> = ${JSON.stringify(french, null, 2)};\n`);

console.log(`Generated ${specs.length} easy concept exercises (${START_ID}-${START_ID + specs.length - 1}).`);

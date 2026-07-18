#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const specs = [];
const pyModulo = (value, divisor) => ((value % divisor) + divisor) % divisor;
const py = value => {
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (value === null) return 'None';
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(py).join(', ')}]`;
  if (typeof value === 'object') return `{${Object.entries(value).map(([key, item]) => `${py(key)}: ${py(item)}`).join(', ')}}`;
  return String(value);
};
const add = spec => specs.push(spec);
const levels = (index, total) => index < Math.ceil(total / 3) ? 'Easy' : index < Math.ceil(total * 2 / 3) ? 'Intermediate' : 'Difficult';

const numericMaps = [
  ['square', 'square every number', 'met chaque nombre au carré', 'value ** 2', x => x ** 2],
  ['cube', 'cube every number', 'met chaque nombre au cube', 'value ** 3', x => x ** 3],
  ['double', 'double every number', 'double chaque nombre', 'value * 2', x => x * 2],
  ['triple', 'triple every number', 'triple chaque nombre', 'value * 3', x => x * 3],
  ['negate', 'change the sign of every number', 'change le signe de chaque nombre', '-value', x => -x],
  ['absolute', 'convert every number to its absolute value', 'convertit chaque nombre en valeur absolue', 'abs(value)', x => Math.abs(x)],
  ['increment', 'add one to every number', 'ajoute un à chaque nombre', 'value + 1', x => x + 1],
  ['decrement', 'subtract one from every number', 'soustrait un à chaque nombre', 'value - 1', x => x - 1],
  ['half', 'divide every number by two', 'divise chaque nombre par deux', 'value / 2', x => x / 2],
  ['last_digit', 'keep the final decimal digit of every number using modulo ten', 'conserve le dernier chiffre décimal de chaque nombre avec modulo dix', 'value % 10', x => pyModulo(x, 10)],
  ['distance_from_ten', 'calculate each number’s distance from 10', 'calcule la distance de chaque nombre par rapport à 10', 'abs(value - 10)', x => Math.abs(x - 10)],
  ['percent', 'convert every decimal value to a percentage', 'convertit chaque valeur décimale en pourcentage', 'value * 100', x => x * 100],
  ['remainder_three', 'calculate every number modulo 3', 'calcule chaque nombre modulo 3', 'value % 3', x => pyModulo(x, 3)],
  ['weighted', 'multiply every number by its one-based position', 'multiplie chaque nombre par sa position commençant à un', 'value * (index + 1)', (x, i) => x * (i + 1)],
  ['offset_index', 'add each zero-based index to its number', 'ajoute chaque indice commençant à zéro à son nombre', 'value + index', (x, i) => x + i],
];
const numericFilters = [
  ['even', 'keep only even numbers', 'conserve uniquement les nombres pairs', 'value % 2 == 0', x => x % 2 === 0],
  ['odd', 'keep only odd numbers', 'conserve uniquement les nombres impairs', 'value % 2 != 0', x => x % 2 !== 0],
  ['positive', 'keep only positive numbers', 'conserve uniquement les nombres positifs', 'value > 0', x => x > 0],
  ['negative', 'keep only negative numbers', 'conserve uniquement les nombres négatifs', 'value < 0', x => x < 0],
  ['nonzero', 'remove every zero', 'supprime chaque zéro', 'value != 0', x => x !== 0],
  ['at_least_five', 'keep numbers greater than or equal to five', 'conserve les nombres supérieurs ou égaux à cinq', 'value >= 5', x => x >= 5],
  ['below_ten', 'keep numbers strictly below ten', 'conserve les nombres strictement inférieurs à dix', 'value < 10', x => x < 10],
  ['multiple_three', 'keep multiples of three', 'conserve les multiples de trois', 'value % 3 == 0', x => x % 3 === 0],
  ['single_digit', 'keep numbers from zero through nine', 'conserve les nombres de zéro à neuf', '0 <= value <= 9', x => x >= 0 && x <= 9],
  ['outside_unit', 'keep numbers whose absolute value is greater than one', 'conserve les nombres dont la valeur absolue dépasse un', 'abs(value) > 1', x => Math.abs(x) > 1],
  ['even_index', 'keep values at even indexes', 'conserve les valeurs aux indices pairs', 'index % 2 == 0', (_x, i) => i % 2 === 0],
  ['odd_index', 'keep values at odd indexes', 'conserve les valeurs aux indices impairs', 'index % 2 != 0', (_x, i) => i % 2 !== 0],
  ['greater_index', 'keep values greater than their zero-based index', 'conserve les valeurs supérieures à leur indice', 'value > index', (x, i) => x > i],
  ['matching_parity', 'keep values with the same parity as their index', 'conserve les valeurs de même parité que leur indice', 'value % 2 == index % 2', (x, i) => ((x % 2) + 2) % 2 === i % 2],
  ['square_below_fifty', 'keep numbers whose square is below fifty', 'conserve les nombres dont le carré est inférieur à cinquante', 'value ** 2 < 50', x => x ** 2 < 50],
];
const stringMaps = [
  ['uppercase', 'convert every word to uppercase', 'convertit chaque mot en majuscules', 'value.upper()', x => x.toUpperCase()],
  ['lowercase', 'convert every word to lowercase', 'convertit chaque mot en minuscules', 'value.lower()', x => x.toLowerCase()],
  ['lengths', 'return the length of every word', 'retourne la longueur de chaque mot', 'len(value)', x => x.length],
  ['first_chars', 'return the first character of every non-empty word', 'retourne le premier caractère de chaque mot non vide', 'value[0]', x => x[0]],
  ['last_chars', 'return the last character of every non-empty word', 'retourne le dernier caractère de chaque mot non vide', 'value[-1]', x => x.at(-1)],
  ['reverse_words', 'reverse the characters in every word', 'inverse les caractères de chaque mot', 'value[::-1]', x => [...x].reverse().join('')],
  ['wrap_words', 'surround every word with square brackets', 'entoure chaque mot de crochets', '"[" + value + "]"', x => `[${x}]`],
  ['double_words', 'repeat every word twice', 'répète chaque mot deux fois', 'value * 2', x => x + x],
  ['initial_pairs', 'return each word’s first and last characters', 'retourne le premier et le dernier caractère de chaque mot', 'value[0] + value[-1]', x => x[0] + x.at(-1)],
  ['vowel_counts', 'count the vowels in every word', 'compte les voyelles dans chaque mot', 'sum(1 for char in value.lower() if char in "aeiou")', x => [...x.toLowerCase()].filter(c => 'aeiou'.includes(c)).length],
];
const numberCases = [[[1, 2, 3, 10]], [[-4, 0, 7, 12]], [[5]]];
const wordCases = [[['cat', 'Python', 'go']], [['A', 'level', 'Code']], [['sun']]];

function mappedCases(recipes, cases) {
  return cases.map(args => ({ args, expected: args[0].map(recipes[4]) }));
}
function filteredCases(recipe, cases = numberCases) {
  return cases.map(args => ({ args, expected: args[0].filter(recipe[4]) }));
}

// Comprehensions: list transforms, filters, indexed transforms, dictionaries, and flattening.
numericMaps.forEach((recipe, index) => add({
  concept: 'Comprehension', key: 'comprehensions', name: `${recipe[0]}_comprehension`, params: 'numbers',
  en: `${recipe[1]} with a list comprehension`, fr: `${recipe[2]} avec une compréhension de liste`,
  body: `return [${recipe[3]} for index, value in enumerate(numbers)]`, cases: mappedCases(recipe, numberCases),
  level: levels(index, 60), nodes: ['ListComp'], focus: 'the output expression and iterable of a list comprehension',
}));
numericFilters.forEach((recipe, index) => add({
  concept: 'Comprehension', key: 'comprehensions', name: `${recipe[0]}_filter_comprehension`, params: 'numbers',
  en: `${recipe[1]} with a conditional list comprehension`, fr: `${recipe[2]} avec une compréhension de liste conditionnelle`,
  body: `return [value for index, value in enumerate(numbers) if ${recipe[3]}]`, cases: filteredCases(recipe),
  level: levels(15 + index, 60), nodes: ['ListComp'], focus: 'the expression, iterable, and filtering condition',
}));
stringMaps.forEach((recipe, index) => add({
  concept: 'Comprehension', key: 'comprehensions', name: `${recipe[0]}_word_comprehension`, params: 'words',
  en: `${recipe[1]} with a list comprehension`, fr: `${recipe[2]} avec une compréhension de liste`,
  body: `return [${recipe[3]} for value in words]`, cases: mappedCases(recipe, wordCases),
  level: levels(30 + index, 60), nodes: ['ListComp'], focus: 'transforming each string in one comprehension',
}));
numericMaps.slice(0, 10).forEach((recipe, index) => add({
  concept: 'Comprehension', key: 'comprehensions', name: `${recipe[0]}_index_dictionary`, params: 'numbers',
  en: `build a dictionary mapping each index to the result when you ${recipe[1]}`, fr: `construit un dictionnaire associant chaque indice au résultat lorsque vous ${recipe[2]}`,
  body: `return {index: ${recipe[3]} for index, value in enumerate(numbers)}`, cases: numberCases.map(args => ({ args, expected: Object.fromEntries(args[0].map((x, i) => [i, recipe[4](x, i)])) })),
  level: levels(40 + index, 60), nodes: ['DictComp'], focus: 'creating key-value pairs in a dictionary comprehension',
}));
numericFilters.slice(0, 10).forEach((recipe, index) => add({
  concept: 'Comprehension', key: 'comprehensions', name: `${recipe[0]}_index_dictionary_filter`, params: 'numbers',
  en: `map indexes to values that satisfy this rule: ${recipe[1]}`, fr: `associe les indices aux valeurs qui respectent cette règle : ${recipe[2]}`,
  body: `return {index: value for index, value in enumerate(numbers) if ${recipe[3]}}`, cases: numberCases.map(args => ({ args, expected: Object.fromEntries(args[0].map((x, i) => [i, x]).filter(([i, x]) => recipe[4](x, i))) })),
  level: levels(50 + index, 60), nodes: ['DictComp'], focus: 'combining dictionary output with a condition',
}));

// For loops: equivalent transformations taught with explicit iteration and accumulators.
const forRecipes = [...numericMaps, ...numericFilters, ...stringMaps];
forRecipes.forEach((recipe, index) => {
  const isFilter = index >= numericMaps.length && index < numericMaps.length + numericFilters.length;
  const isString = index >= numericMaps.length + numericFilters.length;
  const cases = isString ? wordCases : numberCases;
  const expectedCases = isFilter ? filteredCases(recipe) : mappedCases(recipe, cases);
  const operation = isFilter
    ? `if ${recipe[3]}:\n            result.append(value)`
    : `result.append(${recipe[3]})`;
  add({ concept: 'For Loop', key: 'for_loops', name: `${recipe[0]}_explicit_for_loop`, params: isString ? 'words' : 'numbers',
    en: `${recipe[1]} using an explicit for loop`, fr: `${recipe[2]} avec une boucle for explicite`,
    body: `result = []\n    for index, value in enumerate(${isString ? 'words' : 'numbers'}):\n        ${operation}\n    return result`, cases: expectedCases,
    level: levels(index, 50), nodes: ['For'], focus: 'iteration, condition handling, and accumulator updates' });
});
numericMaps.slice(0, 10).forEach((recipe, offset) => {
  const index = forRecipes.length + offset;
  add({ concept: 'For Loop', key: 'for_loops', name: `${recipe[0]}_running_total_for_loop`, params: 'numbers',
    en: `return running totals after applying this operation: ${recipe[1]}`, fr: `retourne les totaux cumulés après cette opération : ${recipe[2]}`,
    body: `result = []\n    total = 0\n    for index, value in enumerate(numbers):\n        total += ${recipe[3]}\n        result.append(total)\n    return result`,
    cases: numberCases.map(args => { let total = 0; return { args, expected: args[0].map((x, i) => total += recipe[4](x, i)) }; }),
    level: levels(index, 50), nodes: ['For'], focus: 'a for loop with a running accumulator' });
});

// Generators: nested yield-based producers are collected so browser grading is deterministic.
[...numericMaps, ...numericFilters, ...stringMaps].forEach((recipe, index) => {
  const isFilter = index >= 15 && index < 30;
  const isString = index >= 30;
  const source = isString ? 'words' : 'numbers';
  const cases = isString ? wordCases : numberCases;
  const expectedCases = isFilter ? filteredCases(recipe) : mappedCases(recipe, cases);
  const yieldLine = isFilter ? `if ${recipe[3]}:\n                yield value` : `yield ${recipe[3]}`;
  add({ concept: 'Generator', key: 'generators', name: `${recipe[0]}_yield_generator`, params: source,
    en: `${recipe[1]} by consuming a nested generator that uses yield`, fr: `${recipe[2]} en consommant un générateur imbriqué qui utilise yield`,
    body: `def produce():\n        for index, value in enumerate(${source}):\n            ${yieldLine}\n    return list(produce())`, cases: expectedCases,
    level: levels(index, 50), nodes: ['Yield', 'FunctionDef'], focus: 'lazy production with yield and explicit consumption' });
});
numericMaps.slice(0, 10).forEach((recipe, offset) => {
  const index = 40 + offset;
  add({ concept: 'Generator', key: 'generators', name: `${recipe[0]}_enumerated_generator`, params: 'numbers',
    en: `yield index-result pairs while you ${recipe[1]}`, fr: `produit des paires indice-résultat lorsque vous ${recipe[2]}`,
    body: `def produce():\n        for index, value in enumerate(numbers):\n            yield (index, ${recipe[3]})\n    return list(produce())`,
    cases: numberCases.map(args => ({ args, expected: args[0].map((x, i) => [i, recipe[4](x, i)]) })),
    level: levels(index, 50), nodes: ['Yield', 'FunctionDef'], focus: 'yielding structured values one at a time' });
});

// Recursion: mappings, filters, reductions, and string traversal all call themselves on a smaller input.
numericMaps.forEach((recipe, index) => add({ concept: 'Recursion', key: 'recursion', name: `recursive_${recipe[0]}_values`, params: 'numbers, index=0',
  en: `${recipe[1]} recursively`, fr: `${recipe[2]} récursivement`,
  body: `if not numbers:\n        return []\n    return [${recipe[3].replaceAll('value', 'numbers[0]')}] + recursive_${recipe[0]}_values(numbers[1:], index + 1)`,
  cases: mappedCases(recipe, numberCases), level: levels(index, 60), nodes: ['If'], selfCall: true, focus: 'a base case and a smaller recursive list call' }));
numericFilters.forEach((recipe, index) => add({ concept: 'Recursion', key: 'recursion', name: `recursive_keep_${recipe[0]}`, params: 'numbers, index=0',
  en: `${recipe[1]} recursively`, fr: `${recipe[2]} récursivement`,
  body: `if not numbers:\n        return []\n    rest = recursive_keep_${recipe[0]}(numbers[1:], index + 1)\n    return ([numbers[0]] + rest) if ${recipe[3].replaceAll('value', 'numbers[0]')} else rest`,
  cases: filteredCases(recipe), level: levels(15 + index, 60), nodes: ['If'], selfCall: true, focus: 'base case, recursive remainder, and conditional reconstruction' }));
numericMaps.forEach((recipe, index) => add({ concept: 'Recursion', key: 'recursion', name: `recursive_total_${recipe[0]}`, params: 'numbers, index=0',
  en: `recursively total the results after you ${recipe[1]}`, fr: `additionne récursivement les résultats après avoir ${recipe[2]}`,
  body: `if not numbers:\n        return 0\n    return ${recipe[3].replaceAll('value', 'numbers[0]')} + recursive_total_${recipe[0]}(numbers[1:], index + 1)`,
  cases: numberCases.map(args => ({ args, expected: args[0].reduce((sum, x, i) => sum + recipe[4](x, i), 0) })),
  level: levels(30 + index, 60), nodes: ['If'], selfCall: true, focus: 'recursive reduction into one accumulated result' }));
stringMaps.slice(0, 10).forEach((recipe, index) => add({ concept: 'Recursion', key: 'recursion', name: `recursive_${recipe[0]}_words`, params: 'words',
  en: `${recipe[1]} recursively`, fr: `${recipe[2]} récursivement`,
  body: `if not words:\n        return []\n    value = words[0]\n    return [${recipe[3]}] + recursive_${recipe[0]}_words(words[1:])`,
  cases: mappedCases(recipe, wordCases), level: levels(45 + index, 60), nodes: ['If'], selfCall: true, focus: 'recursive text transformation over a shrinking list' }));
numericFilters.slice(0, 5).forEach((recipe, index) => add({ concept: 'Recursion', key: 'recursion', name: `recursive_count_${recipe[0]}`, params: 'numbers',
  en: `recursively count values that satisfy this rule: ${recipe[1]}`, fr: `compte récursivement les valeurs qui respectent cette règle : ${recipe[2]}`,
  body: `if not numbers:\n        return 0\n    matched = 1 if ${recipe[3].replaceAll('value', 'numbers[0]').replaceAll('index', '0')} else 0\n    return matched + recursive_count_${recipe[0]}(numbers[1:])`,
  cases: numberCases.map(args => ({ args, expected: args[0].filter(recipe[4]).length })), level: levels(55 + index, 60), nodes: ['If'], selfCall: true, focus: 'recursive counting with a Boolean contribution' }));

// Closures: each factory captures configuration and returns an inner function.
const closureOps = [
  ['adder', 'amount', 'add the captured amount', 'ajoute la valeur capturée', 'value + amount', (a, x) => x + a],
  ['multiplier', 'factor', 'multiply by the captured factor', 'multiplie par le facteur capturé', 'value * factor', (a, x) => x * a],
  ['power', 'exponent', 'raise a value to the captured exponent', 'élève une valeur à l’exposant capturé', 'value ** exponent', (a, x) => x ** a],
  ['minimum', 'minimum', 'replace smaller values with the captured minimum', 'remplace les petites valeurs par le minimum capturé', 'max(value, minimum)', (a, x) => Math.max(x, a)],
  ['maximum', 'maximum', 'replace larger values with the captured maximum', 'remplace les grandes valeurs par le maximum capturé', 'min(value, maximum)', (a, x) => Math.min(x, a)],
  ['remainder', 'divisor', 'calculate a value modulo the captured divisor', 'calcule une valeur modulo le diviseur capturé', 'value % divisor', (a, x) => pyModulo(x, a)],
  ['distance', 'target', 'measure distance from the captured target', 'mesure la distance par rapport à la cible capturée', 'abs(value - target)', (a, x) => Math.abs(x - a)],
  ['percentage', 'rate', 'apply the captured percentage rate', 'applique le taux capturé', 'value * rate / 100', (a, x) => x * a / 100],
  ['offset_square', 'offset', 'add a captured offset before squaring', 'ajoute un décalage capturé avant le carré', '(value + offset) ** 2', (a, x) => (x + a) ** 2],
  ['scale_then_add', 'factor', 'multiply by the captured factor and then add one', 'multiplie par le facteur capturé puis ajoute un', 'value * factor + 1', (a, x) => x * a + 1],
  ['subtract_from', 'total', 'subtract a value from the captured total', 'soustrait une valeur du total capturé', 'total - value', (a, x) => a - x],
  ['multiple_check', 'divisor', 'test divisibility by the captured divisor', 'teste la divisibilité par le diviseur capturé', 'value % divisor == 0', (a, x) => x % a === 0],
  ['greater_check', 'threshold', 'test whether a value exceeds the captured threshold', 'teste si une valeur dépasse le seuil capturé', 'value > threshold', (a, x) => x > a],
  ['range_check', 'limit', 'test whether a value lies between zero and the captured limit', 'teste si une valeur se trouve entre zéro et la limite capturée', '0 <= value <= limit', (a, x) => x >= 0 && x <= a],
];
closureOps.forEach((recipe, index) => add({ concept: 'Closure', key: 'closures', name: `make_${recipe[0]}_closure`, params: recipe[1],
  en: `return an inner function that will ${recipe[2]}`, fr: `retourne une fonction interne qui ${recipe[3]}`,
  body: `def apply(value):\n        return ${recipe[4]}\n    return apply`,
  cases: [[2, 5], [3, -2], [10, 4]].map(([config, value]) => ({ args: [config], callReturnedWith: [value], expected: recipe[5](config, value) })),
  level: levels(index, 42), nodes: ['FunctionDef'], minFunctions: 2, focus: 'capturing an enclosing numeric configuration' }));
const closureStrings = [
  ['prefix', 'prefix', 'place a captured prefix before text', 'place un préfixe capturé avant le texte', 'prefix + text', (a, x) => a + x],
  ['suffix', 'suffix', 'place a captured suffix after text', 'place un suffixe capturé après le texte', 'text + suffix', (a, x) => x + a],
  ['wrapper', 'marker', 'surround text with the captured marker', 'entoure le texte du marqueur capturé', 'marker + text + marker', (a, x) => a + x + a],
  ['separator', 'separator', 'join the characters using a captured separator', 'joint les caractères avec un séparateur capturé', 'separator.join(text)', (a, x) => [...x].join(a)],
  ['repeater', 'times', 'repeat text by the captured count', 'répète le texte selon le nombre capturé', 'text * times', (a, x) => x.repeat(a)],
  ['truncator', 'length', 'keep at most the captured number of characters', 'conserve au maximum le nombre de caractères capturé', 'text[:length]', (a, x) => x.slice(0, a)],
  ['contains', 'fragment', 'test for a captured fragment', 'teste la présence d’un fragment capturé', 'fragment in text', (a, x) => x.includes(a)],
  ['starts', 'prefix', 'test for a captured starting fragment', 'teste un début capturé', 'text.startswith(prefix)', (a, x) => x.startsWith(a)],
  ['ends', 'suffix', 'test for a captured ending fragment', 'teste une fin capturée', 'text.endswith(suffix)', (a, x) => x.endsWith(a)],
  ['replacement', 'old', 'replace a captured fragment with an underscore', 'remplace un fragment capturé par un soulignement', 'text.replace(old, "_")', (a, x) => x.split(a).join('_')],
  ['padding', 'width', 'left-pad text with zeros to a captured width', 'complète le texte à gauche avec des zéros jusqu’à une largeur capturée', 'text.zfill(width)', (a, x) => x.padStart(a, '0')],
  ['case_prefix', 'prefix', 'prepend an uppercase captured prefix', 'ajoute un préfixe capturé en majuscules', 'prefix.upper() + text', (a, x) => a.toUpperCase() + x],
  ['label', 'label', 'format text after a captured label and colon', 'formate le texte après une étiquette capturée et deux-points', 'f"{label}: {text}"', (a, x) => `${a}: ${x}`],
  ['remove', 'fragment', 'remove every captured fragment from text', 'supprime chaque fragment capturé du texte', 'text.replace(fragment, "")', (a, x) => x.split(a).join('')],
];
closureStrings.forEach((recipe, offset) => {
  const index = 14 + offset;
  add({ concept: 'Closure', key: 'closures', name: `make_${recipe[0]}_text_closure`, params: recipe[1], en: `return an inner function that will ${recipe[2]}`, fr: `retourne une fonction interne qui ${recipe[3]}`,
    body: `def apply(text):\n        return ${recipe[4]}\n    return apply`,
    cases: (['repeater', 'padding', 'truncator'].includes(recipe[0]) ? [[3, 'go'], [2, 'example'], [5, 'python']] : [['-', 'code'], ['x', 'example'], ['go', 'gopher']])
      .map(([config, value]) => ({ args: [config], callReturnedWith: [value], expected: recipe[5](config, value) })),
    level: levels(index, 42), nodes: ['FunctionDef'], minFunctions: 2, focus: 'capturing text-formatting configuration' });
});
closureOps.slice(0, 14).forEach((recipe, offset) => {
  const index = 28 + offset;
  add({ concept: 'Closure', key: 'closures', name: `build_${recipe[0]}_pipeline_closure`, params: recipe[1], en: `return a closure that applies this reusable pipeline: ${recipe[2]}`, fr: `retourne une fermeture qui applique ce pipeline réutilisable : ${recipe[3]}`,
    body: `def pipeline(value):\n        result = ${recipe[4]}\n        return result\n    return pipeline`,
    cases: [[4, 2], [5, 7], [2, -3]].map(([config, value]) => ({ args: [config], callReturnedWith: [value], expected: recipe[5](config, value) })),
    level: levels(index, 42), nodes: ['FunctionDef'], minFunctions: 2, focus: 'returning and later calling a configured inner pipeline' });
});

// Slicing: 25 list and 25 text operations with positive, negative, and stepped slices.
const sliceRecipes = [
  ['first_two', 'return the first two items', 'retourne les deux premiers éléments', 'items[:2]', a => a.slice(0,2)],
  ['last_two', 'return the final two items', 'retourne les deux derniers éléments', 'items[-2:]', a => a.slice(-2)],
  ['drop_first', 'return everything except the first item', 'retourne tout sauf le premier élément', 'items[1:]', a => a.slice(1)],
  ['drop_last', 'return everything except the final item', 'retourne tout sauf le dernier élément', 'items[:-1]', a => a.slice(0,-1)],
  ['reverse', 'return all items in reverse order', 'retourne tous les éléments dans l’ordre inverse', 'items[::-1]', a => [...a].reverse()],
  ['even_positions', 'return items at indexes 0, 2, 4, and so on', 'retourne les éléments aux indices 0, 2, 4, etc.', 'items[::2]', a => a.filter((_x,i)=>i%2===0)],
  ['odd_positions', 'return items at indexes 1, 3, 5, and so on', 'retourne les éléments aux indices 1, 3, 5, etc.', 'items[1::2]', a => a.filter((_x,i)=>i%2===1)],
  ['middle', 'remove the first and final items', 'supprime le premier et le dernier élément', 'items[1:-1]', a => a.slice(1,-1)],
  ['first_half', 'return the first half using integer division', 'retourne la première moitié avec la division entière', 'items[:len(items) // 2]', a => a.slice(0,Math.floor(a.length/2))],
  ['second_half', 'return the second half starting at integer midpoint', 'retourne la seconde moitié à partir du milieu entier', 'items[len(items) // 2:]', a => a.slice(Math.floor(a.length/2))],
  ['every_third', 'return every third item from the start', 'retourne un élément sur trois depuis le début', 'items[::3]', a => a.filter((_x,i)=>i%3===0)],
  ['reverse_every_second', 'step backward through every second item from the end', 'recule d’un élément sur deux depuis la fin', 'items[::-2]', a => [...a].reverse().filter((_x,i)=>i%2===0)],
  ['without_edges_two', 'remove the first two and final two items', 'supprime les deux premiers et deux derniers éléments', 'items[2:-2]', a => a.slice(2,-2)],
  ['first_three_reverse', 'reverse only the first three items', 'inverse uniquement les trois premiers éléments', 'items[:3][::-1]', a => a.slice(0,3).reverse()],
  ['last_three_reverse', 'reverse only the final three items', 'inverse uniquement les trois derniers éléments', 'items[-3:][::-1]', a => a.slice(-3).reverse()],
  ['copy', 'return a shallow slice copy of all items', 'retourne une copie superficielle de tous les éléments', 'items[:]', a => a.slice()],
  ['quarter_start', 'return items from index one through index three', 'retourne les éléments de l’indice un à trois', 'items[1:4]', a => a.slice(1,4)],
  ['bounded_step', 'return indexes one, three, and five when available', 'retourne les indices un, trois et cinq lorsqu’ils existent', 'items[1:6:2]', a => a.slice(1,6).filter((_x,i)=>i%2===0)],
  ['reverse_middle', 'reverse the items after dropping both edges', 'inverse les éléments après suppression des deux extrémités', 'items[-2:0:-1]', a => a.slice(1,-1).reverse()],
  ['first_from_reverse', 'return the reverse order without the original first item', 'retourne l’ordre inverse sans le premier élément original', 'items[:0:-1]', a => a.slice(1).reverse()],
  ['up_to_four', 'return at most the first four items', 'retourne au maximum les quatre premiers éléments', 'items[:4]', a => a.slice(0,4)],
  ['from_third', 'return items beginning at index two', 'retourne les éléments à partir de l’indice deux', 'items[2:]', a => a.slice(2)],
  ['exclude_last_three', 'return everything except the final three items', 'retourne tout sauf les trois derniers éléments', 'items[:-3]', a => a.slice(0,-3)],
  ['last_four_step_two', 'return every second item inside the final four', 'retourne un élément sur deux parmi les quatre derniers', 'items[-4::2]', a => a.slice(-4).filter((_x,i)=>i%2===0)],
  ['double_reverse_copy', 'reverse twice to produce an equal copy', 'inverse deux fois pour produire une copie égale', 'items[::-1][::-1]', a => a.slice()],
];
const listSliceCases = [[[0,1,2,3,4,5,6]], [['a','b','c','d']], [[9,8,7,6,5]]];
const textSliceCases = [['abcdefgh'], ['Python'], ['12345']];
sliceRecipes.forEach((recipe, index) => add({ concept: 'Slicing', key: 'slicing', name: `${recipe[0]}_list_slice`, params: 'items', en: `${recipe[1]} by slicing a list`, fr: `${recipe[2]} en découpant une liste`, body: `return ${recipe[3]}`,
  cases: listSliceCases.map(args => ({ args, expected: recipe[4](args[0]) })), level: levels(index, 50), nodes: ['Slice'], focus: 'start, stop, and step positions in a list slice' }));
sliceRecipes.forEach((recipe, offset) => {
  const index = 25 + offset;
  add({ concept: 'Slicing', key: 'slicing', name: `${recipe[0]}_text_slice`, params: 'text', en: `${recipe[1].replace('items','characters')} by slicing text`, fr: `${recipe[2].replace('éléments','caractères')} en découpant du texte`, body: `items = text\n    return ${recipe[3]}`,
    cases: textSliceCases.map(args => ({ args, expected: recipe[4]([...args[0]]).join('') })), level: levels(index, 50), nodes: ['Slice'], focus: 'start, stop, and step positions in a string slice' });
});

// Regex: fifteen distinct extraction, validation, replacement, splitting, and counting tasks.
const regexSpecs = [
  ['extract_signed_integers', 'find all signed or unsigned integers in text', 'trouve tous les entiers signés ou non dans un texte', 'text', 'return re.findall(r"[+-]?\\d+", text)', [[['x=-12 y=+7 z=4'],['-12','+7','4']],[['none'],[]],[['0 -3'],['0','-3']]], 'findall'],
  ['validate_simple_slug', 'validate a lowercase slug made of words separated by single hyphens', 'valide un slug minuscule composé de mots séparés par des tirets simples', 'text', 'return re.fullmatch(r"[a-z]+(?:-[a-z]+)*", text) is not None', [[['hello-world'],true],[['Hello-world'],false],[['one--two'],false]], 'fullmatch'],
  ['extract_named_groups', 'extract first and last names written as `Last, First` into tuple pairs', 'extrait les noms écrits `Nom, Prénom` sous forme de paires', 'text', 'return re.findall(r"([A-Z][a-z]+),\\s*([A-Z][a-z]+)", text)', [[['Smith, Ada; Jones, Bob'],[['Smith','Ada'],['Jones','Bob']]],[['none'],[]],[['Lee, Kim'],[['Lee','Kim']]]], 'findall'],
  ['normalize_dashes', 'replace runs of hyphens or underscores with one hyphen', 'remplace les suites de tirets ou soulignements par un tiret', 'text', 'return re.sub(r"[-_]+", "-", text)', [[['a__b---c'],'a-b-c'],[['clean'],'clean'],[['_x_'],'-x-']], 'sub'],
  ['split_pipe_fields', 'split fields around a pipe while ignoring surrounding whitespace', 'sépare les champs autour d’une barre verticale en ignorant les espaces', 'text', 'return re.split(r"\\s*\\|\\s*", text)', [[['a | b|c'],['a','b','c']],[['one'],['one']],[['x  |  y'],['x','y']]], 'split'],
  ['extract_html_attributes', 'extract double-quoted HTML attribute names and values', 'extrait les noms et valeurs d’attributs HTML entre guillemets doubles', 'text', 'return re.findall(r"([A-Za-z_:][-\\w:.]*)=\\\"([^\\\"]*)\\\"", text)', [[['id="main" class="box"'],[['id','main'],['class','box']]],[['disabled'],[]],[['x="1"'],[['x','1']]]], 'findall'],
  ['validate_binary_text', 'validate a non-empty string containing only binary digits', 'valide une chaîne non vide contenant uniquement des chiffres binaires', 'text', 'return re.fullmatch(r"[01]+", text) is not None', [[['10101'],true],[['102'],false],[[''],false]], 'fullmatch'],
  ['mask_card_groups', 'replace every four-digit group with four asterisks', 'remplace chaque groupe de quatre chiffres par quatre astérisques', 'text', 'return re.sub(r"\\d{4}", "****", text)', [[['1234 5678'],'**** ****'],[['id 12'],'id 12'],[['0000'],'****']], 'sub'],
  ['extract_markdown_links', 'extract label and URL pairs from simple Markdown links', 'extrait les paires libellé et URL des liens Markdown simples', 'text', 'return re.findall(r"\\[([^]]+)\\]\\(([^)]+)\\)", text)', [[['See [Docs](https://x.dev)'],[['Docs','https://x.dev']]],[['none'],[]],[['[A](a) [B](b)'],[['A','a'],['B','b']]]], 'findall'],
  ['count_sentence_endings', 'count `.`, `!`, or `?` groups that end sentences', 'compte les groupes `.`, `!` ou `?` qui terminent les phrases', 'text', 'return len(re.findall(r"[.!?]+(?:\\s|$)", text))', [[['Hi! How are you? Fine.'],3],[['none'],0],[['Wow!!!'],1]], 'findall'],
  ['extract_python_identifiers', 'extract valid Python-like identifiers from text', 'extrait les identifiants de style Python valides dans un texte', 'text', 'return re.findall(r"\\b[A-Za-z_]\\w*\\b", text)', [[['x1 = _value + 2'],['x1','_value']],[['123'],[]],[['hello world'],['hello','world']]], 'findall'],
  ['remove_duplicate_spaces_lines', 'replace horizontal whitespace runs while preserving newlines', 'remplace les suites d’espaces horizontaux tout en conservant les retours à la ligne', 'text', 'return re.sub(r"[^\\S\\n]+", " ", text)', [[['a   b\nc  d'],'a b\nc d'],[['x'],'x'],[['  hi  '],' hi ']], 'sub'],
  ['validate_decimal_number', 'validate an optional sign followed by an integer or decimal number', 'valide un signe facultatif suivi d’un nombre entier ou décimal', 'text', 'return re.fullmatch(r"[+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)", text) is not None', [[['-12.5'],true],[['.75'],true],[['1.2.3'],false]], 'fullmatch'],
  ['extract_log_levels', 'extract uppercase DEBUG, INFO, WARNING, or ERROR labels', 'extrait les étiquettes majuscules DEBUG, INFO, WARNING ou ERROR', 'text', 'return re.findall(r"\\b(?:DEBUG|INFO|WARNING|ERROR)\\b", text)', [[['INFO start ERROR stop'],['INFO','ERROR']],[['info'],[]],[['WARNING'],['WARNING']]], 'findall'],
  ['camel_to_words', 'insert spaces before capitals in a camel-case identifier and lowercase the result', 'insère des espaces avant les majuscules d’un identifiant camelCase puis met le résultat en minuscules', 'text', 'return re.sub(r"(?<!^)(?=[A-Z])", " ", text).lower()', [[['camelCaseWord'],'camel case word'],[['Python'],'python'],[['already'],'already']], 'sub'],
];
regexSpecs.forEach((item, index) => add({ concept: 'Regex', key: 'regex', name: `${item[0]}_regex`, params: item[3], en: item[1] + ' using regular expressions', fr: item[2] + ' avec des expressions régulières',
  body: `import re\n    ${item[4]}`, cases: item[5].map(([args, expected]) => ({ args, expected })), level: levels(index, 15), calls: [item[6]], focus: 'choosing the regex operation and pattern boundaries' }));

if (specs.length !== 327) throw new Error(`Expected 327 specs, found ${specs.length}`);

const conceptLabels = { Closure: 'closure', Comprehension: 'comprehension', Generator: 'generator', Recursion: 'recursion', Regex: 'regular expression', Slicing: 'slice', 'For Loop': 'for loop' };
const conceptLabelsFr = { Closure: 'fermeture', Comprehension: 'compréhension', Generator: 'générateur', Recursion: 'récursion', Regex: 'expression régulière', Slicing: 'découpage', 'For Loop': 'boucle for' };
const exercises = {};
const graders = {};
const french = {};

specs.forEach((spec, index) => {
  const id = 2481 + index;
  const args1 = spec.cases[0].args.map(py).join(', ');
  const args2 = spec.cases[1].args.map(py).join(', ');
  const invoke = test => test.callReturnedWith
    ? `${spec.name}(${test.args.map(py).join(', ')})(${test.callReturnedWith.map(py).join(', ')})`
    : `${spec.name}(${test.args.map(py).join(', ')})`;
  const canonical = `def ${spec.name}(${spec.params}):\n    ${spec.body}`;
  const classApproach = canonical.split('\n').map(line => `    ${line}`).join('\n');
  const helperBody = canonical.split('\n').slice(1).map(line => `    ${line}`).join('\n');
  const alternativeBody = canonical.split('\n').slice(1).map(line => `    ${line}`).join('\n');
  const solution = `# Using function approach\n# Example 1: direct ${conceptLabels[spec.concept]} function\n${canonical}\n\nprint(${invoke(spec.cases[0])})  # Expected: ${py(spec.cases[0].expected)}\nprint(${invoke(spec.cases[1])})  # Expected: ${py(spec.cases[1].expected)}\n\n# Alternative helper implementation\ndef ${spec.name}(${spec.params}):\n    def compute_result():\n${alternativeBody}\n    return compute_result()\n\n# Example 2: callable class approach\nclass Problem${id}${spec.concept.replaceAll(' ', '')}Solution:\n    @staticmethod\n${classApproach}\n\nprint(Problem${id}${spec.concept.replaceAll(' ', '')}Solution.${spec.name}(${args1})${spec.cases[0].callReturnedWith ? `(${spec.cases[0].callReturnedWith.map(py).join(', ')})` : ''})\n\n# Example 3: nested helper approach\ndef solve_problem_${id}(${spec.params}):\n    def execute():\n${helperBody}\n    return execute()\n\nprint(solve_problem_${id}(${args2})${spec.cases[1].callReturnedWith ? `(${spec.cases[1].callReturnedWith.map(py).join(', ')})` : ''})\n\n# Example 4: script approach\nresult = ${invoke(spec.cases[0])}\nprint(result)\n\n# Example 5: direct call\nprint(${invoke(spec.cases[2])})`;
  const description = `Write a Python function called \`${spec.name}\` that must ${spec.en}. Use ${conceptLabels[spec.concept]} syntax.\nDifficulty: ${spec.level}.\nExamples:\n  ${invoke(spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec.cases[1])} -> ${py(spec.cases[1].expected)}`;
  exercises[id] = { id, title: `Problem ${id}`, description, initialCode: `def ${spec.name}(${spec.params}):\n    pass`, solution,
    hint: `Identify the input, the required output, and the ${conceptLabels[spec.concept]} structure. Focus on ${spec.focus}.`,
    breakdown: `1. Read the input and output types in the examples.\n2. Build the required ${conceptLabels[spec.concept]} structure.\n3. Apply the operation without hard-coding the examples.\n4. Check the boundary or base case.\n5. Return the result.`,
    category: `${spec.concept} ${spec.level}` };
  const grader = { functionNames: [spec.name], tests: spec.cases };
  if (spec.nodes?.length) grader.requiredNodePatterns = spec.nodes.map(nodeType => ({ nodeType, minCount: nodeType === 'FunctionDef' && spec.minFunctions ? spec.minFunctions : 1 }));
  if (spec.calls?.length) grader.requiredAnyCallPatterns = spec.calls.map(functionName => ({ functionName, minArgs: 1 }));
  if (spec.selfCall) grader.requiredCallPatterns = [{ functionName: spec.name, minArgs: 1 }];
  graders[id] = grader;
  french[id] = {
    description: `Écrivez une fonction Python appelée \`${spec.name}\` qui ${spec.fr}. Utilisez la syntaxe de ${conceptLabelsFr[spec.concept]}.\nDifficulté : ${spec.level === 'Easy' ? 'Facile' : spec.level === 'Intermediate' ? 'Intermédiaire' : 'Difficile'}.\nExemples :\n  ${invoke(spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec.cases[1])} -> ${py(spec.cases[1].expected)}`,
    hint: `Identifiez les entrées, la sortie attendue et la structure de ${conceptLabelsFr[spec.concept]}. Vérifiez chaque étape de la structure demandée avant de retourner le résultat.`,
    breakdown: `1. Lisez les types d’entrée et de sortie dans les exemples.\n2. Construisez la structure de ${conceptLabelsFr[spec.concept]} demandée.\n3. Appliquez l’opération sans coder les exemples en dur.\n4. Vérifiez la limite ou le cas de base.\n5. Retournez le résultat.`,
  };
});

fs.writeFileSync(path.join(root, 'conceptExpansionExercises.ts'), `import type { Exercise } from './types';\n\nexport const CONCEPT_EXPANSION_EXERCISES: Exercise[] = ${JSON.stringify(Object.values(exercises), null, 2)};\n`);
fs.writeFileSync(path.join(root, 'conceptExpansionGraders.ts'), `import type { AutoGrader } from './graders';\n\nexport const CONCEPT_EXPANSION_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders, null, 2)};\n`);
fs.writeFileSync(path.join(root, 'services/conceptExpansionFr.ts'), `export const CONCEPT_EXPANSION_FR: Record<number, { description: string; hint: string; breakdown: string }> = ${JSON.stringify(french, null, 2)};\n`);

console.log(`Generated ${specs.length} concept expansion exercises (2481-2807).`);

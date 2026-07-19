#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const START_ID = 2808;
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
const level = index => index < 17 ? 'Easy' : index < 34 ? 'Intermediate' : 'Difficult';
const replaceName = (expression, from, to) => expression.replace(new RegExp(`\\b${from}\\b`, 'g'), to);
const add = spec => specs.push(spec);

const numericInputs = [5, -4, 0];
const textInputs = ['Python', 'level', 'a b c'];
const listInputs = [[1, 2, 3], [-2, 0, 5], [3, 3, 1]];
const operation = (key, en, fr, expression, inputs, evaluate) => ({
  key, en, fr, expression,
  cases: inputs.map(value => ({ args: [value], expected: evaluate(value) })),
});

const operations = [
  operation('double', 'double the supplied number', 'double le nombre fourni', 'value * 2', numericInputs, value => value * 2),
  operation('triple', 'triple the supplied number', 'triple le nombre fourni', 'value * 3', numericInputs, value => value * 3),
  operation('square', 'square the supplied number', 'met le nombre fourni au carré', 'value ** 2', numericInputs, value => value ** 2),
  operation('cube', 'cube the supplied number', 'met le nombre fourni au cube', 'value ** 3', numericInputs, value => value ** 3),
  operation('increment', 'add one to the supplied number', 'ajoute un au nombre fourni', 'value + 1', numericInputs, value => value + 1),
  operation('decrement', 'subtract one from the supplied number', 'soustrait un au nombre fourni', 'value - 1', numericInputs, value => value - 1),
  operation('negate', 'reverse the sign of the supplied number', 'inverse le signe du nombre fourni', '-value', numericInputs, value => -value),
  operation('absolute', 'return the absolute value of the supplied number', 'retourne la valeur absolue du nombre fourni', 'abs(value)', numericInputs, value => Math.abs(value)),
  operation('half', 'divide the supplied number by two', 'divise le nombre fourni par deux', 'value / 2', numericInputs, value => value / 2),
  operation('remainder_three', 'return the supplied number modulo three', 'retourne le nombre fourni modulo trois', 'value % 3', numericInputs, value => ((value % 3) + 3) % 3),
  operation('last_digit', 'return the final decimal digit', 'retourne le dernier chiffre décimal', 'value % 10', numericInputs, value => ((value % 10) + 10) % 10),
  operation('distance_ten', 'measure the distance from ten', 'mesure la distance par rapport à dix', 'abs(value - 10)', numericInputs, value => Math.abs(value - 10)),
  operation('clamp_zero', 'replace negative values with zero', 'remplace les valeurs négatives par zéro', 'max(value, 0)', numericInputs, value => Math.max(value, 0)),
  operation('is_even', 'test whether the number is even', 'teste si le nombre est pair', 'value % 2 == 0', numericInputs, value => value % 2 === 0),
  operation('is_positive', 'test whether the number is positive', 'teste si le nombre est positif', 'value > 0', numericInputs, value => value > 0),
  operation('sign_label', 'return positive, negative, or zero according to the number', 'retourne positif, négatif ou zéro selon le nombre', '"positive" if value > 0 else "negative" if value < 0 else "zero"', numericInputs, value => value > 0 ? 'positive' : value < 0 ? 'negative' : 'zero'),
  operation('digit_count', 'count its decimal digits without counting the sign', 'compte ses chiffres décimaux sans compter le signe', 'len(str(abs(value)))', numericInputs, value => String(Math.abs(value)).length),
  operation('digit_sum', 'add its decimal digits without counting the sign', 'additionne ses chiffres décimaux sans compter le signe', 'sum(int(digit) for digit in str(abs(value)))', [52, -407, 0], value => [...String(Math.abs(value))].reduce((sum, digit) => sum + Number(digit), 0)),
  operation('triangular', 'calculate the triangular total from zero through its absolute value', 'calcule le total triangulaire de zéro à sa valeur absolue', 'abs(value) * (abs(value) + 1) // 2', numericInputs, value => Math.abs(value) * (Math.abs(value) + 1) / 2),
  operation('within_ten', 'test whether it lies from negative ten through positive ten', 'teste s’il se trouve entre moins dix et plus dix', '-10 <= value <= 10', [5, -14, 10], value => value >= -10 && value <= 10),
  operation('uppercase', 'convert the text to uppercase', 'convertit le texte en majuscules', 'value.upper()', textInputs, value => value.toUpperCase()),
  operation('lowercase', 'convert the text to lowercase', 'convertit le texte en minuscules', 'value.lower()', textInputs, value => value.toLowerCase()),
  operation('reverse_text', 'reverse all characters in the text', 'inverse tous les caractères du texte', 'value[::-1]', textInputs, value => [...value].reverse().join('')),
  operation('text_length', 'return the number of characters in the text', 'retourne le nombre de caractères du texte', 'len(value)', textInputs, value => value.length),
  operation('first_character', 'return its first character or an empty string', 'retourne son premier caractère ou une chaîne vide', 'value[0] if value else ""', ['Python', '', 'z'], value => value ? value[0] : ''),
  operation('last_character', 'return its final character or an empty string', 'retourne son dernier caractère ou une chaîne vide', 'value[-1] if value else ""', ['Python', '', 'z'], value => value ? value.at(-1) : ''),
  operation('vowel_count', 'count vowels without regard to case', 'compte les voyelles sans tenir compte de la casse', 'sum(1 for char in value.lower() if char in "aeiou")', textInputs, value => [...value.toLowerCase()].filter(char => 'aeiou'.includes(char)).length),
  operation('word_count', 'count whitespace-separated words', 'compte les mots séparés par des espaces', 'len(value.split())', textInputs, value => value.trim() ? value.trim().split(/\s+/).length : 0),
  operation('remove_spaces', 'remove every space from the text', 'supprime tous les espaces du texte', 'value.replace(" ", "")', textInputs, value => value.replaceAll(' ', '')),
  operation('hyphenate', 'replace spaces with hyphens', 'remplace les espaces par des tirets', 'value.replace(" ", "-")', textInputs, value => value.replaceAll(' ', '-')),
  operation('title_words', 'capitalize every whitespace-separated word', 'met une majuscule à chaque mot séparé par des espaces', 'value.title()', textInputs, value => value.replace(/\b\w/g, char => char.toUpperCase())),
  operation('palindrome', 'test whether the text is a case-sensitive palindrome', 'teste si le texte est un palindrome sensible à la casse', 'value == value[::-1]', textInputs, value => value === [...value].reverse().join('')),
  operation('digit_characters', 'count digit characters in the text', 'compte les chiffres dans le texte', 'sum(char.isdigit() for char in value)', ['a1b2', '2026', 'none'], value => [...value].filter(char => /\d/.test(char)).length),
  operation('initials', 'return the uppercase initials of its words', 'retourne les initiales majuscules de ses mots', '"".join(word[0].upper() for word in value.split() if word)', ['python code', 'Ada Lovelace', 'solo'], value => value.split(/\s+/).filter(Boolean).map(word => word[0].toUpperCase()).join('')),
  operation('bracket_text', 'surround the text with square brackets', 'entoure le texte de crochets', '"[" + value + "]"', textInputs, value => `[${value}]`),
  operation('sum_items', 'add every number in the list', 'additionne tous les nombres de la liste', 'sum(value)', listInputs, value => value.reduce((sum, item) => sum + item, 0)),
  operation('maximum_item', 'return the largest list item', 'retourne le plus grand élément de la liste', 'max(value)', listInputs, value => Math.max(...value)),
  operation('minimum_item', 'return the smallest list item', 'retourne le plus petit élément de la liste', 'min(value)', listInputs, value => Math.min(...value)),
  operation('reverse_items', 'return the list in reverse order', 'retourne la liste dans l’ordre inverse', 'value[::-1]', listInputs, value => [...value].reverse()),
  operation('sort_items', 'return a new ascending list', 'retourne une nouvelle liste croissante', 'sorted(value)', listInputs, value => [...value].sort((a, b) => a - b)),
  operation('unique_items', 'preserve only the first occurrence of each item', 'conserve uniquement la première occurrence de chaque élément', 'list(dict.fromkeys(value))', listInputs, value => [...new Set(value)]),
  operation('even_items', 'return only even list items', 'retourne uniquement les éléments pairs de la liste', '[item for item in value if item % 2 == 0]', listInputs, value => value.filter(item => item % 2 === 0)),
  operation('odd_items', 'return only odd list items', 'retourne uniquement les éléments impairs de la liste', '[item for item in value if item % 2 != 0]', listInputs, value => value.filter(item => item % 2 !== 0)),
  operation('positive_items', 'return only positive list items', 'retourne uniquement les éléments positifs de la liste', '[item for item in value if item > 0]', listInputs, value => value.filter(item => item > 0)),
  operation('square_items', 'square every list item', 'met chaque élément de la liste au carré', '[item ** 2 for item in value]', listInputs, value => value.map(item => item ** 2)),
  operation('item_count', 'return the number of list items', 'retourne le nombre d’éléments de la liste', 'len(value)', listInputs, value => value.length),
  operation('average_items', 'return the arithmetic average of the list', 'retourne la moyenne arithmétique de la liste', 'sum(value) / len(value)', listInputs, value => value.reduce((sum, item) => sum + item, 0) / value.length),
  operation('running_total', 'return all running totals', 'retourne tous les totaux cumulés', '[sum(value[:index + 1]) for index in range(len(value))]', listInputs, value => { let total = 0; return value.map(item => total += item); }),
  operation('index_pairs', 'pair every item with its zero-based index', 'associe chaque élément à son indice commençant à zéro', 'list(enumerate(value))', listInputs, value => value.map((item, index) => [index, item])),
  operation('nonzero_count', 'count nonzero list items', 'compte les éléments non nuls de la liste', 'sum(item != 0 for item in value)', listInputs, value => value.filter(Boolean).length),
];

if (operations.length !== PACK_SIZE) throw new Error(`Expected ${PACK_SIZE} reusable operations, found ${operations.length}`);

operations.forEach((item, index) => {
  const expression = replaceName(item.expression, 'value', 'original');
  add({ concept: 'Decorator', key: 'decorators', name: `decorated_${item.key}`, params: 'value',
    en: `use a decorator to ${item.en} after calling a wrapped identity function`, fr: `utilise un décorateur qui ${item.fr} après l’appel d’une fonction identité décorée`,
    body: `def transform_result(function):\n        def wrapper(value):\n            original = function(value)\n            return ${expression}\n        return wrapper\n\n    @transform_result\n    def identity(value):\n        return value\n\n    return identity(value)`,
    cases: item.cases, level: level(index), nodes: [{ nodeType: 'FunctionDef', minCount: 3 }], decorators: ['transform_result'], definedFunctions: ['wrapper', 'identity'],
    focus: 'the decorator factory, wrapper, @ syntax, and wrapped call' });
});

operations.forEach((item, index) => {
  const values = item.cases.map(test => test.args[0]);
  const expected = item.cases.map(test => test.expected);
  const iteratorCases = [
    { args: [values], expected },
    { args: [[values[2], values[0]]], expected: [expected[2], expected[0]] },
    { args: [[values[1]]], expected: [expected[1]] },
  ];
  add({ concept: 'Iterator', key: 'iterators', name: `iterate_${item.key}`, params: 'values',
    en: `use iter() and next() to visit every value and ${item.en}`, fr: `utilise iter() et next() pour parcourir chaque valeur et ${item.fr}`,
    body: `iterator = iter(values)\n    result = []\n    while True:\n        try:\n            item = next(iterator)\n        except StopIteration:\n            break\n        result.append(${replaceName(item.expression, 'value', 'item')})\n    return result`,
    cases: iteratorCases, level: level(index), nodes: [{ nodeType: 'While' }, { nodeType: 'Try' }], calls: ['iter', 'next'],
    focus: 'creating an iterator, requesting values with next(), and handling StopIteration' });
});

operations.forEach((item, index) => add({ concept: 'Context Manager', key: 'contextManagers', name: `managed_${item.key}`, params: 'value',
  en: `use a custom context manager to safely expose a value and ${item.en}`, fr: `utilise un gestionnaire de contexte personnalisé pour exposer une valeur en toute sécurité et ${item.fr}`,
  body: `class ManagedValue:\n        def __init__(self, stored):\n            self.stored = stored\n\n        def __enter__(self):\n            return self.stored\n\n        def __exit__(self, exc_type, exc_value, traceback):\n            return False\n\n    with ManagedValue(value) as current:\n        result = ${replaceName(item.expression, 'value', 'current')}\n    return result`,
  cases: item.cases, level: level(index), nodes: [{ nodeType: 'With' }, { nodeType: 'ClassDef' }], definedFunctions: ['__enter__', '__exit__'],
  focus: 'the context-manager protocol, as target, managed block, and cleanup method' }));

operations.forEach((item, index) => add({ concept: 'Dataclass', key: 'dataclasses', name: `dataclass_${item.key}`, params: 'value',
  en: `store the value in a @dataclass and ${item.en} through an instance method`, fr: `stocke la valeur dans une @dataclass et ${item.fr} grâce à une méthode d’instance`,
  body: `from dataclasses import dataclass\n\n    @dataclass\n    class ValueRecord:\n        value: object\n\n        def calculate(self):\n            return ${replaceName(item.expression, 'value', 'self.value')}\n\n    return ValueRecord(value).calculate()`,
  cases: item.cases, level: level(index), nodes: [{ nodeType: 'ClassDef' }, { nodeType: 'AnnAssign' }], decorators: ['dataclass'], definedFunctions: ['calculate'],
  focus: 'the @dataclass decorator, annotated field, generated initializer, and instance method' }));

const magicGroups = [
  { method: '__str__', params: 'value', labels: ['Value', 'Number', 'Item', 'Score', 'Data'],
    make: label => ({ name: `string_${label.toLowerCase()}`, en: `format an object as ${label}(value) with __str__`, fr: `formate un objet sous la forme ${label}(valeur) avec __str__`,
      body: `return f"${label}({self.value})"`, invoke: 'str(box)', cases: [3, -2, 0].map(value => ({ args: [value], expected: `${label}(${value})` })) }) },
  { method: '__repr__', params: 'value', labels: ['Point', 'Record', 'Token', 'Entry', 'Packet'],
    make: label => ({ name: `representation_${label.toLowerCase()}`, en: `produce ${label}(value=value) with __repr__`, fr: `produit ${label}(value=valeur) avec __repr__`,
      body: `return f"${label}(value={self.value})"`, invoke: 'repr(box)', cases: [3, -2, 0].map(value => ({ args: [value], expected: `${label}(value=${value})` })) }) },
  { method: '__len__', params: 'value', labels: ['characters', 'items', 'unique', 'truthy', 'words'],
    make: kind => { const configs = {
      characters: ['return len(self.value)', ['python', '', 'go'], value => value.length], items: ['return len(self.value)', [[1,2], [], [3]], value => value.length],
      unique: ['return len(set(self.value))', [[1,1,2], [], [3,3]], value => new Set(value).size], truthy: ['return sum(bool(item) for item in self.value)', [[0,1,2], [], ['', 'x']], value => value.filter(Boolean).length],
      words: ['return len(self.value.split())', ['one two', '', 'three'], value => value.trim() ? value.trim().split(/\s+/).length : 0],
    }; const [body, inputs, evaluate] = configs[kind]; return { name: `length_${kind}`, en: `calculate the number of ${kind} with __len__`, fr: `calcule le nombre de ${kind} avec __len__`, body, invoke: 'len(box)', cases: inputs.map(value => ({ args:[value], expected:evaluate(value) })) }; } },
  { method: '__eq__', params: 'value, other', labels: ['exact', 'absolute', 'lowercase', 'length', 'sorted'],
    make: kind => { const configs = {
      exact: ['return self.value == other', [[2,2],[2,3],['a','a']], (a,b)=>a===b], absolute: ['return abs(self.value) == abs(other)', [[-2,2],[3,-4],[0,0]], (a,b)=>Math.abs(a)===Math.abs(b)],
      lowercase: ['return str(self.value).lower() == str(other).lower()', [['Python','python'],['A','b'],['x','X']], (a,b)=>String(a).toLowerCase()===String(b).toLowerCase()],
      length: ['return len(self.value) == len(other)', [['ab','cd'],['a','xyz'],[[],[]]], (a,b)=>a.length===b.length], sorted: ['return sorted(self.value) == sorted(other)', [[[2,1],[1,2]],[[1],[2]],[[3,3],[3,3]]], (a,b)=>JSON.stringify([...a].sort())===JSON.stringify([...b].sort())],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`equality_${kind}`, en:`compare ${kind} values with __eq__`, fr:`compare des valeurs selon ${kind} avec __eq__`, body, invoke:'box == other', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__lt__', params: 'value, other', labels: ['numeric', 'absolute', 'text_length', 'list_sum', 'lowercase'],
    make: kind => { const configs = {
      numeric:['return self.value < other',[[2,3],[4,1],[0,0]],(a,b)=>a<b], absolute:['return abs(self.value) < abs(other)',[[-2,3],[4,-1],[0,0]],(a,b)=>Math.abs(a)<Math.abs(b)],
      text_length:['return len(self.value) < len(other)',[['a','abc'],['long','x'],['ab','cd']],(a,b)=>a.length<b.length], list_sum:['return sum(self.value) < sum(other)',[[[1],[2]],[[5],[1,2]],[[0],[0]]],(a,b)=>a.reduce((s,x)=>s+x,0)<b.reduce((s,x)=>s+x,0)],
      lowercase:['return self.value.lower() < other.lower()',[['a','B'],['z','a'],['x','X']],(a,b)=>a.toLowerCase()<b.toLowerCase()],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`ordering_${kind}`, en:`order ${kind} values with __lt__`, fr:`ordonne des valeurs selon ${kind} avec __lt__`, body, invoke:'box < other', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__add__', params: 'value, other', labels: ['numbers', 'text', 'lists', 'offset', 'absolute'],
    make: kind => { const configs = {
      numbers:['return self.value + other',[[2,3],[-1,4],[0,0]],(a,b)=>a+b], text:['return self.value + other',[['py','thon'],['a',''],['x','y']],(a,b)=>a+b], lists:['return self.value + other',[[[1],[2]],[[1,2],[]],[[],[3]]],(a,b)=>[...a,...b]],
      offset:['return self.value + other + 1',[[2,3],[-1,4],[0,0]],(a,b)=>a+b+1], absolute:['return abs(self.value) + abs(other)',[[-2,3],[-1,-4],[0,0]],(a,b)=>Math.abs(a)+Math.abs(b)],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`addition_${kind}`, en:`combine ${kind} with __add__`, fr:`combine des valeurs ${kind} avec __add__`, body, invoke:'box + other', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__sub__', params: 'value, other', labels: ['numbers', 'absolute', 'distance', 'floored', 'doubled'],
    make: kind => { const configs = {
      numbers:['return self.value - other',[[5,2],[-1,4],[0,0]],(a,b)=>a-b], absolute:['return abs(self.value) - abs(other)',[[-5,2],[-1,-4],[0,0]],(a,b)=>Math.abs(a)-Math.abs(b)], distance:['return abs(self.value - other)',[[5,2],[-1,4],[0,0]],(a,b)=>Math.abs(a-b)],
      floored:['return max(0, self.value - other)',[[5,2],[1,4],[0,0]],(a,b)=>Math.max(0,a-b)], doubled:['return self.value - (other * 2)',[[5,2],[-1,4],[0,0]],(a,b)=>a-b*2],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`subtraction_${kind}`, en:`calculate ${kind} subtraction with __sub__`, fr:`calcule une soustraction ${kind} avec __sub__`, body, invoke:'box - other', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__mul__', params: 'value, other', labels: ['numbers', 'text', 'lists', 'absolute', 'offset'],
    make: kind => { const configs = {
      numbers:['return self.value * other',[[3,2],[-2,4],[0,5]],(a,b)=>a*b], text:['return self.value * other',[['ab',2],['x',0],['z',3]],(a,b)=>a.repeat(b)], lists:['return self.value * other',[[[1],2],[[1,2],0],[[3],3]],(a,b)=>Array.from({length:b},()=>a).flat()],
      absolute:['return abs(self.value * other)',[[-3,2],[-2,-4],[0,5]],(a,b)=>Math.abs(a*b)], offset:['return self.value * other + 1',[[3,2],[-2,4],[0,5]],(a,b)=>a*b+1],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`multiplication_${kind}`, en:`calculate ${kind} multiplication with __mul__`, fr:`calcule une multiplication ${kind} avec __mul__`, body, invoke:'box * other', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__contains__', params: 'value, target', labels: ['direct', 'casefold', 'keys', 'absolute', 'substring'],
    make: kind => { const configs = {
      direct:['return target in self.value',[[[1,2],2],[[1],3],['abc','b']],(a,b)=>a.includes(b)], casefold:['return str(target).lower() in str(self.value).lower()',[['Python','PY'],['abc','Z'],['Test','test']],(a,b)=>String(a).toLowerCase().includes(String(b).toLowerCase())],
      keys:['return target in self.value.keys()',[[{a:1},'a'],[{a:1},'b'],[{},'x']],(a,b)=>Object.hasOwn(a,b)], absolute:['return abs(target) in [abs(item) for item in self.value]',[[[-2,3],2],[[1],-3],[[0],0]],(a,b)=>a.map(Math.abs).includes(Math.abs(b))],
      substring:['return str(target) in " ".join(self.value)',[[['red','blue'],'blue'],[['a'],'z'],[['python','code'],'on']],(a,b)=>a.join(' ').includes(String(b))],
    }; const [body,pairs,evaluate]=configs[kind]; return { name:`contains_${kind}`, en:`test ${kind} membership with __contains__`, fr:`teste l’appartenance ${kind} avec __contains__`, body, invoke:'target in box', cases:pairs.map(([a,b])=>({args:[a,b],expected:evaluate(a,b)})) }; } },
  { method: '__bool__', params: 'value', labels: ['direct', 'any_items', 'positive', 'longer_two', 'all_items'],
    make: kind => { const configs = {
      direct:['return bool(self.value)',[0,1,''],value=>Boolean(value)], any_items:['return any(self.value)',[[0,1],[0,0],[]],value=>value.some(Boolean)], positive:['return self.value > 0',[-1,2,0],value=>value>0],
      longer_two:['return len(self.value) > 2',['abc','a',''],value=>value.length>2], all_items:['return all(self.value)',[[1,2],[1,0],[]],value=>value.every(Boolean)],
    }; const [body,inputs,evaluate]=configs[kind]; return { name:`truth_${kind}`, en:`calculate ${kind} truth with __bool__`, fr:`calcule la valeur de vérité ${kind} avec __bool__`, body, invoke:'bool(box)', cases:inputs.map(value=>({args:[value],expected:evaluate(value)})) }; } },
];

magicGroups.forEach(group => group.labels.forEach((label, offset) => {
  const item = group.make(label);
  const index = specs.filter(spec => spec.concept === 'Magic Method').length;
  const methodArgument = group.params.includes(',') ? group.params.split(',')[1].trim() : '';
  add({ concept: 'Magic Method', key: 'magicMethods', name: `magic_${item.name}`, params: group.params, en: item.en, fr: item.fr,
    body: `class MagicValue:\n        def __init__(self, value):\n            self.value = value\n\n        def ${group.method}(self${methodArgument ? `, ${methodArgument}` : ''}):\n            ${item.body}\n\n    box = MagicValue(value)\n    return ${item.invoke}`,
    cases: item.cases, level: level(index), nodes: [{ nodeType: 'ClassDef' }], definedFunctions: [group.method], focus: `the ${group.method} protocol and the operation that triggers it` });
}));

if (specs.filter(spec => spec.concept === 'Magic Method').length !== PACK_SIZE) throw new Error('Magic method pack must contain 50 specs');

const masks = [1, 3, 15, 85, 170];
const positions = [0, 1, 2, 3, 4];
const bitCases = [0, 5, 42];
const bitFamilies = [
  ['and_mask', 'keep only bits selected by mask', 'conserve uniquement les bits sélectionnés par le masque', (mask) => `number & ${mask}`, (number, mask) => number & mask, 'BitAnd', masks],
  ['or_mask', 'turn on every bit selected by mask', 'active tous les bits sélectionnés par le masque', (mask) => `number | ${mask}`, (number, mask) => number | mask, 'BitOr', masks],
  ['xor_mask', 'toggle every bit selected by mask', 'inverse tous les bits sélectionnés par le masque', (mask) => `number ^ ${mask}`, (number, mask) => number ^ mask, 'BitXor', masks],
  ['left_shift', 'shift all bits left', 'décale tous les bits vers la gauche', (amount) => `number << ${amount}`, (number, amount) => number << amount, 'LShift', [1,2,3,4,5]],
  ['right_shift', 'shift all bits right', 'décale tous les bits vers la droite', (amount) => `number >> ${amount}`, (number, amount) => number >> amount, 'RShift', [1,2,3,4,5]],
  ['set_bit', 'set one bit at the selected zero-based position', 'active un bit à la position choisie commençant à zéro', (position) => `number | (1 << ${position})`, (number, position) => number | (1 << position), 'BitOr', positions],
  ['clear_bit', 'clear one bit at the selected zero-based position', 'désactive un bit à la position choisie commençant à zéro', (position) => `number & ~(1 << ${position})`, (number, position) => number & ~(1 << position), 'BitAnd', positions],
  ['toggle_bit', 'toggle one bit at the selected zero-based position', 'inverse un bit à la position choisie commençant à zéro', (position) => `number ^ (1 << ${position})`, (number, position) => number ^ (1 << position), 'BitXor', positions],
  ['test_bit', 'test whether one selected bit is on', 'teste si un bit sélectionné est actif', (position) => `bool(number & (1 << ${position}))`, (number, position) => Boolean(number & (1 << position)), 'BitAnd', positions],
  ['extract_field', 'extract a three-bit field beginning at the selected position', 'extrait un champ de trois bits commençant à la position choisie', (position) => `(number >> ${position}) & 0b111`, (number, position) => (number >> position) & 7, 'RShift', positions],
];
bitFamilies.forEach((family, familyIndex) => family[6].forEach((constant, offset) => {
  const index = familyIndex * 5 + offset;
  add({ concept: 'Bitwise Operation', key: 'bitwise', name: `${family[0]}_${constant}_bitwise`, params: 'number',
    en: `${family[1]} using ${constant}`, fr: `${family[2]} avec ${constant}`,
    body: `return ${family[3](constant)}`,
    cases: bitCases.map(number => ({ args: [number], expected: family[4](number, constant) })), level: level(index), astOperators: [family[5]],
    focus: 'the binary representation, mask or shift amount, and resulting bits' });
}));

const expectedCounts = { Decorator: 50, Iterator: 50, 'Context Manager': 50, Dataclass: 50, 'Magic Method': 50, 'Bitwise Operation': 50 };
if (specs.length !== 300) throw new Error(`Expected 300 specs, found ${specs.length}`);
for (const [concept, count] of Object.entries(expectedCounts)) {
  const found = specs.filter(spec => spec.concept === concept).length;
  if (found !== count) throw new Error(`${concept}: expected ${count}, found ${found}`);
}

const labels = { Decorator: 'decorator', Iterator: 'iterator', 'Context Manager': 'context manager', Dataclass: 'dataclass', 'Magic Method': 'magic method', 'Bitwise Operation': 'bitwise operator' };
const labelsFr = { Decorator: 'décorateur', Iterator: 'itérateur', 'Context Manager': 'gestionnaire de contexte', Dataclass: 'dataclass', 'Magic Method': 'méthode spéciale', 'Bitwise Operation': 'opérateur bit à bit' };
const exercises = [];
const graders = {};
const french = {};

const invoke = (spec, test) => `${spec.name}(${test.args.map(py).join(', ')})`;
specs.forEach((spec, index) => {
  const id = START_ID + index;
  const canonical = `def ${spec.name}(${spec.params}):\n    ${spec.body}`;
  const nestedBody = canonical.split('\n').slice(1).map(line => `    ${line}`).join('\n');
  const classBody = canonical.split('\n').map(line => `    ${line}`).join('\n');
  const solution = `# Using function approach\n# Example 1: canonical ${labels[spec.concept]} solution\n${canonical}\n\nprint(${invoke(spec, spec.cases[0])})  # Expected: ${py(spec.cases[0].expected)}\nprint(${invoke(spec, spec.cases[1])})  # Expected: ${py(spec.cases[1].expected)}\n\n# Example 2: nested helper approach\ndef solve_problem_${id}(${spec.params}):\n    def execute():\n${nestedBody}\n    return execute()\n\nprint(solve_problem_${id}(${spec.cases[0].args.map(py).join(', ')}))\n\n# Example 3: static method approach\nclass Problem${id}Solution:\n    @staticmethod\n${classBody}\n\nprint(Problem${id}Solution.${spec.name}(${spec.cases[1].args.map(py).join(', ')}))\n\n# Example 4: assigned result approach\nresult = ${invoke(spec, spec.cases[0])}\nprint(result)\n\n# Example 5: direct call\nprint(${invoke(spec, spec.cases[2])})`;
  exercises.push({
    id, title: `Problem ${id}`,
    description: `Write a Python function called \`${spec.name}\` that must ${spec.en}. Use ${labels[spec.concept]} syntax.\nDifficulty: ${spec.level}.\nExamples:\n  ${invoke(spec, spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec, spec.cases[1])} -> ${py(spec.cases[1].expected)}`,
    initialCode: `def ${spec.name}(${spec.params}):\n    pass`, solution,
    hint: `Build the ${labels[spec.concept]} structure before implementing the result. Focus on ${spec.focus}.`,
    breakdown: `1. Identify the input and expected output.\n2. Build the required ${labels[spec.concept]} structure.\n3. Trace the value through that structure.\n4. Handle the boundary case shown by the hidden tests.\n5. Return the final result without hard-coding examples.`,
    category: `${spec.concept} ${spec.level}`,
  });
  const grader = { functionNames: [spec.name], tests: spec.cases };
  if (spec.nodes) grader.requiredNodePatterns = spec.nodes;
  if (spec.calls) grader.requiredCallPatterns = spec.calls.map(functionName => ({ functionName, minArgs: 1 }));
  if (spec.decorators) grader.requiredDecorators = spec.decorators;
  if (spec.definedFunctions) grader.requiredDefinedFunctions = spec.definedFunctions;
  if (spec.astOperators) grader.requiredAstOperators = spec.astOperators;
  graders[id] = grader;
  french[id] = {
    description: `Écrivez une fonction Python appelée \`${spec.name}\` qui ${spec.fr}. Utilisez la syntaxe de ${labelsFr[spec.concept]}.\nDifficulté : ${spec.level === 'Easy' ? 'Facile' : spec.level === 'Intermediate' ? 'Intermédiaire' : 'Difficile'}.\nExemples :\n  ${invoke(spec, spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec, spec.cases[1])} -> ${py(spec.cases[1].expected)}`,
    hint: `Construisez d’abord la structure de ${labelsFr[spec.concept]}, puis suivez la valeur à chaque étape. Concentrez-vous sur le protocole demandé plutôt que sur les seules sorties d’exemple.`,
    breakdown: `1. Identifiez l’entrée et la sortie attendue.\n2. Construisez la structure de ${labelsFr[spec.concept]} demandée.\n3. Suivez la valeur dans cette structure.\n4. Gérez le cas limite couvert par les tests cachés.\n5. Retournez le résultat sans coder les exemples en dur.`,
  };
});

fs.writeFileSync(path.join(root, 'advancedConceptExercises.ts'), `import type { Exercise } from './types';\n\nexport const ADVANCED_CONCEPT_EXERCISES: Exercise[] = ${JSON.stringify(exercises, null, 2)};\n`);
fs.writeFileSync(path.join(root, 'advancedConceptGraders.ts'), `import type { AutoGrader } from './graders';\n\nexport const ADVANCED_CONCEPT_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders, null, 2)};\n`);
fs.writeFileSync(path.join(root, 'services/advancedConceptFr.ts'), `export const ADVANCED_CONCEPT_FR: Record<number, { description: string; hint: string; breakdown: string }> = ${JSON.stringify(french, null, 2)};\n`);

console.log(`Generated ${specs.length} advanced concept exercises (${START_ID}-${START_ID + specs.length - 1}).`);

#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const START_ID = 7108;
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
const add = spec => specs.push(spec);
const tests = (inputs, evaluate) => inputs.map(args => ({ args, expected: evaluate(...args) }));
const numericSort = values => [...values].sort((a, b) => a - b);
const parameterNames = params => {
  const parts = [];
  let current = '';
  let depth = 0;
  for (const character of params) {
    if ('[({'.includes(character)) depth += 1;
    if (']})'.includes(character)) depth -= 1;
    if (character === ',' && depth === 0) {
      parts.push(current);
      current = '';
    } else current += character;
  }
  if (current) parts.push(current);
  return parts.map(parameter => parameter.trim().split(':')[0]);
};
const levelFor = (concept, index) => {
  if (concept === 'Sorting Key') return index < 70 ? 'Easy' : index < 110 ? 'Intermediate' : 'Difficult';
  if (concept === 'Enumerate & Zip') return index < 40 ? 'Easy' : index < 80 ? 'Intermediate' : 'Difficult';
  return index < 20 ? 'Easy' : index < 40 ? 'Intermediate' : 'Difficult';
};

// 150 sorting-key exercises: seven beginner-friendly families, four intermediate, four expert.
for (let index = 0; index < 150; index += 1) {
  const family = Math.floor(index / 10);
  const c = index % 10 + 1;
  const defs = [
    { name: `sort_numbers_ascending_${c}`, params: 'values', en: `return numbers in ascending order followed by marker ${c}`, fr: `retourne les nombres par ordre croissant suivis du marqueur ${c}`, body: `return sorted(values) + [${c}]`, inputs: [[[3,1,2]], [[-1,4,0]], [[]]], eval: values => numericSort(values).concat(c) },
    { name: `sort_numbers_descending_${c}`, params: 'values', en: `return marker ${c} followed by numbers in descending order`, fr: `retourne le marqueur ${c} suivi des nombres par ordre décroissant`, body: `return [${c}] + sorted(values, reverse=True)`, inputs: [[[3,1,2]], [[-1,4,0]], [[]]], eval: values => [c, ...numericSort(values).reverse()] },
    { name: `sort_words_by_length_${c}`, params: 'words', en: `sort words by length then alphabetically and append marker_${c}`, fr: `trie les mots par longueur puis alphabétiquement et ajoute marker_${c}`, body: `return sorted(words, key=lambda word: (len(word), word)) + ["marker_${c}"]`, inputs: [[['pear','a','fig']], [['bb','aa','c']], [[]]], eval: words => [...words].sort((a,b)=>a.length-b.length||a.localeCompare(b)).concat(`marker_${c}`) },
    { name: `sort_words_casefold_${c}`, params: 'words', en: `sort words without case sensitivity and append marker_${c}`, fr: `trie les mots sans tenir compte de la casse et ajoute marker_${c}`, body: `return sorted(words, key=str.casefold) + ["marker_${c}"]`, inputs: [[['Zoo','apple','Banana']], [['b','A']], [[]]], eval: words => [...words].sort((a,b)=>a.toLowerCase().localeCompare(b.toLowerCase())).concat(`marker_${c}`) },
    { name: `sort_pairs_second_${c}`, params: 'pairs', en: `sort pairs by second item then first item and append marker pair ${c}`, fr: `trie les paires par le second élément puis le premier et ajoute la paire marqueur ${c}`, body: `return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [["marker", ${c}]]`, inputs: [[[['b',2],['a',1],['c',1]]], [[['x',0]]], [[]]], eval: pairs => [...pairs].sort((a,b)=>a[1]-b[1]||String(a[0]).localeCompare(String(b[0]))).concat([['marker',c]]) },
    { name: `sort_records_field_${c}`, params: 'records, field', en: `sort dictionaries by a named numeric field and append marker record ${c}`, fr: `trie les dictionnaires selon un champ numérique nommé et ajoute l’enregistrement marqueur ${c}`, body: `return sorted(records, key=lambda record: record[field]) + [{"marker": ${c}}]`, inputs: [[[{'score':3},{'score':1}], 'score'], [[{'age':4}], 'age'], [[], 'x']], eval: (records,field)=>[...records].sort((a,b)=>a[field]-b[field]).concat({marker:c}) },
    { name: `sort_by_absolute_${c}`, params: 'values', en: `sort numbers by absolute value then numeric value and append ${c}`, fr: `trie les nombres par valeur absolue puis valeur numérique et ajoute ${c}`, body: `return sorted(values, key=lambda value: (abs(value), value)) + [${c}]`, inputs: [[[-3,1,-1,2]], [[0,-5,4]], [[]]], eval: values => [...values].sort((a,b)=>Math.abs(a)-Math.abs(b)||a-b).concat(c) },
    { name: `sort_even_before_odd_${c}`, params: 'values', en: `sort even numbers before odd numbers with ascending values, then append ${c}`, fr: `trie les nombres pairs avant les impairs en ordre croissant puis ajoute ${c}`, body: `return sorted(values, key=lambda value: (value % 2, value)) + [${c}]`, inputs: [[[5,2,3,4]], [[-1,-2,0]], [[]]], eval: values => [...values].sort((a,b)=>((a%2)+2)%2-((b%2)+2)%2||a-b).concat(c) },
    { name: `sort_by_distance_${c}`, params: 'values, target', en: `sort values by distance from target then by value and append ${c}`, fr: `trie les valeurs selon leur distance à target puis leur valeur et ajoute ${c}`, body: `return sorted(values, key=lambda value: (abs(value - target), value)) + [${c}]`, inputs: [[[1,8,4],5], [[-3,2,7],0], [[],9]], eval: (values,target)=>[...values].sort((a,b)=>Math.abs(a-target)-Math.abs(b-target)||a-b).concat(c) },
    { name: `sort_by_character_count_${c}`, params: 'words, character', en: `sort words by descending character count then alphabetically and append marker_${c}`, fr: `trie les mots par nombre décroissant du caractère puis alphabétiquement et ajoute marker_${c}`, body: `return sorted(words, key=lambda word: (-word.count(character), word)) + ["marker_${c}"]`, inputs: [[['banana','pear','apple'],'a'], [['test','tree'],'t'], [[],'x']], eval: (words,ch)=>[...words].sort((a,b)=>b.split(ch).length-a.split(ch).length||a.localeCompare(b)).concat(`marker_${c}`) },
    { name: `sort_people_multiple_fields_${c}`, params: 'people', en: `sort people by descending score, ascending age, then name and append marker ${c}`, fr: `trie les personnes par score décroissant, âge croissant puis nom et ajoute le marqueur ${c}`, body: `return sorted(people, key=lambda person: (-person["score"], person["age"], person["name"])) + [{"marker": ${c}}]`, inputs: [[[{'name':'B','score':9,'age':30},{'name':'A','score':9,'age':20}]], [[{'name':'X','score':1,'age':2}]], [[]]], eval: people=>[...people].sort((a,b)=>b.score-a.score||a.age-b.age||a.name.localeCompare(b.name)).concat({marker:c}) },
    { name: `sort_nested_by_sum_${c}`, params: 'groups', en: `sort nested number lists by sum, length, then contents and append marker list ${c}`, fr: `trie les listes imbriquées par somme, longueur puis contenu et ajoute la liste marqueur ${c}`, body: `return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[${c}]]`, inputs: [[[[2,2],[1],[0,1]]], [[[3],[-1,1]]], [[]]], eval: groups=>[...groups].sort((a,b)=>a.reduce((x,y)=>x+y,0)-b.reduce((x,y)=>x+y,0)||a.length-b.length||JSON.stringify(a).localeCompare(JSON.stringify(b))).concat([[c]]) },
    { name: `sort_files_extension_${c}`, params: 'names', en: `sort filenames by lowercase extension then lowercase name and append marker_${c}.txt`, fr: `trie les fichiers par extension minuscule puis nom minuscule et ajoute marker_${c}.txt`, body: `def key(name):\n        stem, separator, extension = name.rpartition(".")\n        return (extension.casefold() if separator else "", name.casefold())\n    return sorted(names, key=key) + ["marker_${c}.txt"]`, inputs: [[['b.py','a.TXT','README']], [['z.csv','A.csv']], [[]]], eval: names=>[...names].sort((a,b)=>{const ea=a.includes('.')?a.split('.').at(-1).toLowerCase():'';const eb=b.includes('.')?b.split('.').at(-1).toLowerCase():'';return ea.localeCompare(eb)||a.toLowerCase().localeCompare(b.toLowerCase())}).concat(`marker_${c}.txt`) },
    { name: `sort_by_frequency_${c}`, params: 'values', en: `sort values by descending frequency then numeric value and append ${c}`, fr: `trie les valeurs par fréquence décroissante puis valeur numérique et ajoute ${c}`, body: `counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [${c}]`, inputs: [[[3,1,3,2,1,3]], [[2,2,1]], [[]]], eval: values=>{const counts={};values.forEach(v=>counts[v]=(counts[v]||0)+1);return [...values].sort((a,b)=>counts[b]-counts[a]||a-b).concat(c)} },
    { name: `sort_by_modulo_${c}`, params: 'values, divisor', en: `sort values by remainder, quotient, then value and append ${c}`, fr: `trie les valeurs par reste, quotient puis valeur et ajoute ${c}`, body: `return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [${c}]`, inputs: [[[8,3,5,2],3], [[10,-1,4],4], [[],2]], eval: (values,d)=>[...values].sort((a,b)=>((a%d)+d)%d-((b%d)+d)%d||Math.floor(a/d)-Math.floor(b/d)||a-b).concat(c) },
  ];
  const d = defs[family];
  add({ concept:'Sorting Key', ...d, cases:tests(d.inputs,d.eval), calls:['sorted'], focus:'the key tuple, ascending versus descending fields, tie breakers, and stable ordering' });
}

// 50 testing and debugging exercises.
for (let index=0; index<50; index+=1) {
  const family=Math.floor(index/10), c=index%10+1;
  const defs=[
    {name:`compare_test_outputs_${c}`,params:'actual, expected',en:`return per-item equality results and append test marker ${c}`,fr:`retourne les résultats d’égalité élément par élément et ajoute le marqueur de test ${c}`,body:`assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [${c}]`,inputs:[[[1,2],[1,3]],[[],[]],[['a'],['a']]],eval:(a,e)=>a.slice(0,Math.min(a.length,e.length)).map((v,i)=>v===e[i]).concat(c)},
    {name:`first_test_failure_${c}`,params:'actual, expected',en:`return the first mismatching index plus ${c}, or -1 when all tested values match`,fr:`retourne le premier indice différent plus ${c}, ou -1 si toutes les valeurs testées correspondent`,body:`assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + ${c}\n    return -1`,inputs:[[[1,9],[1,2]],[[1],[1]],[[],[]]],eval:(a,e)=>{const i=a.findIndex((v,j)=>v!==e[j]);return i<0?-1:i+c}},
    {name:`approximately_equal_${c}`,params:'left, right',en:`test whether two numbers differ by at most ${c} thousandth(s)`,fr:`teste si deux nombres diffèrent d’au plus ${c} millième(s)`,imports:'import math',body:`assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=${c} / 1000)`,inputs:[[1,1+c/2000],[1,1+c/500],[-2,-2]],eval:(a,b)=>Math.abs(a-b)<=c/1000+1e-12,calls:['isclose']},
    {name:`count_passing_cases_${c}`,params:'values, minimum',en:`count values meeting the minimum and add ${c} to the test count`,fr:`compte les valeurs atteignant le minimum et ajoute ${c} au nombre de tests`,body:`assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + ${c}`,inputs:[[[1,5,7],5],[[],0],[[-2,0],-1]],eval:(v,m)=>v.filter(x=>x>=m).length+c},
    {name:`invalid_integer_positions_${c}`,params:'texts',en:`debug integer input by returning invalid positions followed by marker ${c}`,fr:`débogue les entrées entières en retournant les positions invalides suivies du marqueur ${c}`,body:`invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [${c}]`,inputs:[[['1','x','3']],[['-2','0']],[[]]],eval:texts=>texts.map((x,i)=>{try{return [Number.isInteger(Number(x))&&String(x).trim()!==''?null:i]}catch{return [i]}}).flat().filter(x=>x!==null).concat(c),nodes:[{nodeType:'Try'}]},
  ]; const d=defs[family]; add({concept:'Testing & Debugging',...d,cases:tests(d.inputs,d.eval),nodes:d.nodes||[{nodeType:'Assert'}],calls:d.calls,focus:'the tested invariant, expected versus actual values, failure location, and useful diagnostics'});
}

// 50 type-hint exercises.
for (let index=0; index<50; index+=1) {
  const family=Math.floor(index/10),c=index%10+1;
  const defs=[
    {name:`typed_scale_${c}`,params:'value: int',returnType:'int',en:`multiply an integer by ${c} with complete type hints`,fr:`multiplie un entier par ${c} avec des annotations de type complètes`,body:`return value * ${c}`,inputs:[[3],[-2],[0]],eval:v=>v*c},
    {name:`typed_prefix_${c}`,params:'text: str',returnType:'str',en:`prefix text with label_${c}: using complete type hints`,fr:`préfixe le texte avec label_${c}: avec des annotations complètes`,body:`return "label_${c}:" + text`,inputs:[['abc'],[''],['Python']],eval:t=>`label_${c}:`+t},
    {name:`typed_filter_${c}`,params:'values: list[int]',returnType:'list[int]',en:`return integers at least ${c} with collection type hints`,fr:`retourne les entiers supérieurs ou égaux à ${c} avec des annotations de collection`,body:`return [value for value in values if value >= ${c}]`,inputs:[[[1,5,10]],[[c]], [[]]],eval:v=>v.filter(x=>x>=c)},
    {name:`typed_lookup_${c}`,params:'mapping: dict[str, int], key: str',returnType:'int',en:`look up an integer by string key or return ${c}, with type hints`,fr:`cherche un entier par clé chaîne ou retourne ${c}, avec des annotations`,body:`return mapping.get(key, ${c})`,inputs:[[{a:1},'a'],[{},'x'],[{x:0},'x']],eval:(m,k)=>Object.hasOwn(m,k)?m[k]:c},
    {name:`typed_summary_${c}`,params:'values: list[int]',returnType:'list[int]',en:`return sum plus ${c} and item count as a typed two-item list`,fr:`retourne la somme plus ${c} et le nombre d’éléments dans une liste typée de deux éléments`,body:`return [sum(values) + ${c}, len(values)]`,inputs:[[[1,2]], [[]], [[-1,1]]],eval:v=>[v.reduce((a,b)=>a+b,0)+c,v.length]},
  ]; const d=defs[family]; add({concept:'Type Hint',...d,cases:tests(d.inputs,d.eval),typeHints:{minParameters:parameterNames(d.params).length,requireReturn:true},focus:'every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior'});
}

// 50 exception-handling exercises.
for (let index=0; index<50; index+=1) {
  const family=Math.floor(index/10),c=index%10+1;
  const defs=[
    {name:`safe_integer_offset_${c}`,params:'text',en:`convert text to an integer plus ${c}, or return ${c} when conversion fails`,fr:`convertit le texte en entier plus ${c}, ou retourne ${c} si la conversion échoue`,body:`try:\n        return int(text) + ${c}\n    except (TypeError, ValueError):\n        return ${c}`,inputs:[['5'],['bad'],[null]],eval:t=>t===null||String(t).trim()===''||!Number.isInteger(Number(t))?c:Number(t)+c},
    {name:`safe_division_${c}`,params:'value, divisor',en:`divide value by divisor and add ${c}, returning None for invalid division`,fr:`divise value par divisor et ajoute ${c}, en retournant None pour une division invalide`,body:`try:\n        return value / divisor + ${c}\n    except (TypeError, ZeroDivisionError):\n        return None`,inputs:[[10,2],[5,0],['x',2]],eval:(v,d)=>typeof v==='number'&&typeof d==='number'&&d!==0?v/d+c:null},
    {name:`safe_list_item_${c}`,params:'values, index',en:`return a list item plus ${c}, or None for an invalid index or value`,fr:`retourne un élément de liste plus ${c}, ou None pour un indice ou une valeur invalide`,body:`try:\n        return values[index] + ${c}\n    except (IndexError, TypeError):\n        return None`,inputs:[[[1,5],1],[[1],9],[['x'],0]],eval:(v,i)=>i>=0&&i<v.length&&typeof v[i]==='number'?v[i]+c:null},
    {name:`safe_mapping_value_${c}`,params:'mapping, key',en:`return a numeric mapping value plus ${c}, or ${c} for a missing or invalid value`,fr:`retourne une valeur numérique du dictionnaire plus ${c}, ou ${c} si elle manque ou est invalide`,body:`try:\n        return mapping[key] + ${c}\n    except (KeyError, TypeError):\n        return ${c}`,inputs:[[{a:2},'a'],[{},'x'],[{x:'bad'},'x']],eval:(m,k)=>typeof m[k]==='number'?m[k]+c:c},
    {name:`safe_square_root_${c}`,params:'value',en:`return square root plus ${c}, or None for a negative or invalid value`,fr:`retourne la racine carrée plus ${c}, ou None pour une valeur négative ou invalide`,imports:'import math',body:`try:\n        return math.sqrt(value) + ${c}\n    except (TypeError, ValueError):\n        return None`,inputs:[[9],[-1],['x']],eval:v=>typeof v==='number'&&v>=0?Math.sqrt(v)+c:null,calls:['sqrt']},
  ]; const d=defs[family]; add({concept:'Exceptions',...d,cases:tests(d.inputs,d.eval),nodes:[{nodeType:'Try'},{nodeType:'ExceptHandler'}],calls:d.calls,focus:'the exact operation that may fail, narrow exception types, fallback behavior, and successful return path'});
}

// 50 equality and identity exercises.
for (let index=0; index<50; index+=1) {
  const family=Math.floor(index/10),c=index%10+1;
  const defs=[
    {name:`normalized_text_equal_${c}`,params:'left, right',en:`compare text after trimming and casefolding, variant ${c}`,fr:`compare les textes après nettoyage et normalisation de casse, variante ${c}`,body:'return left.strip().casefold() == right.strip().casefold()',inputs:[[' Python ','python'],['A','b'],['',' ']],eval:(a,b)=>a.trim().toLowerCase()===b.trim().toLowerCase()},
    {name:`strict_value_equal_${c}`,params:'left, right',en:`test equal value and identical type, variant ${c}`,fr:`teste une valeur égale et un type identique, variante ${c}`,body:'return type(left) is type(right) and left == right',inputs:[[1,1],[1,true],['1',1]],eval:(a,b)=>typeof a===typeof b&&a===b},
    {name:`sequence_equal_${c}`,params:'left, right',en:`test whether two sequences have equal ordered contents, variant ${c}`,fr:`teste si deux séquences ont le même contenu ordonné, variante ${c}`,body:'return list(left) == list(right)',inputs:[[[1,2],[1,2]],[[1,2],[2,1]],[[],[]]],eval:(a,b)=>JSON.stringify(a)===JSON.stringify(b)},
    {name:`both_none_identity_${c}`,params:'left, right',en:`use identity to test whether both values are None, variant ${c}`,fr:`utilise l’identité pour tester si les deux valeurs sont None, variante ${c}`,body:'return left is None and right is None',inputs:[[null,null],[null,0],[false,false]],eval:(a,b)=>a===null&&b===null,operators:['Is']},
    {name:`unordered_values_equal_${c}`,params:'left, right',en:`test whether two integer lists contain equal values with equal duplicate counts, variant ${c}`,fr:`teste si deux listes d’entiers contiennent les mêmes valeurs avec les mêmes doublons, variante ${c}`,body:'return sorted(left) == sorted(right)',inputs:[[[1,2,1],[2,1,1]],[[1,2],[1,1]],[[],[]]],eval:(a,b)=>JSON.stringify(numericSort(a))===JSON.stringify(numericSort(b)),calls:['sorted']},
  ]; const d=defs[family]; add({concept:'Equality & Identity',...d,cases:tests(d.inputs,d.eval),operators:d.operators,focus:'value equality versus object identity, normalization, type sensitivity, order, and duplicate counts'});
}

// 100 enumerate-and-zip exercises.
for (let index=0; index<100; index+=1) {
  const family=Math.floor(index/10),c=index%10+1;
  const defs=[
    {name:`enumerated_pairs_${c}`,params:'values',en:`return index-value lists starting at ${c}`,fr:`retourne les listes indice-valeur à partir de ${c}`,body:`return [[index, value] for index, value in enumerate(values, start=${c})]`,inputs:[[['a','b']],[[]],[[9]]],eval:v=>v.map((x,i)=>[i+c,x]),calls:['enumerate']},
    {name:`enumerated_labels_${c}`,params:'values',en:`return labels combining indexes from ${c} with values`,fr:`retourne des étiquettes combinant les indices depuis ${c} avec les valeurs`,body:`return [f"{index}:{value}" for index, value in enumerate(values, start=${c})]`,inputs:[[['a','b']],[[]],[[9]]],eval:v=>v.map((x,i)=>`${i+c}:${x}`),calls:['enumerate']},
    {name:`positions_matching_${c}`,params:'values, target',en:`return matching indexes offset by ${c}`,fr:`retourne les indices correspondants décalés de ${c}`,body:`return [index + ${c} for index, value in enumerate(values) if value == target]`,inputs:[[[1,2,1],1],[['a'],'x'],[[],0]],eval:(v,t)=>v.map((x,i)=>x===t?i+c:null).filter(x=>x!==null),calls:['enumerate']},
    {name:`zip_to_pairs_${c}`,params:'left, right',en:`zip two inputs into lists and append marker pair ${c}`,fr:`combine deux entrées en listes et ajoute la paire marqueur ${c}`,body:`return [[a, b] for a, b in zip(left, right)] + [["marker", ${c}]]`,inputs:[[[1,2],['a','b']],[[1],['a','b']],[[],[]]],eval:(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>[x,b[i]]).concat([['marker',c]]),calls:['zip']},
    {name:`zip_add_values_${c}`,params:'left, right',en:`add parallel numbers plus ${c}`,fr:`additionne les nombres parallèles plus ${c}`,body:`return [a + b + ${c} for a, b in zip(left, right)]`,inputs:[[[1,2],[3,4]],[[1],[2,3]],[[],[]]],eval:(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>x+b[i]+c),calls:['zip']},
    {name:`zip_dictionary_${c}`,params:'keys, values',en:`build a dictionary from parallel inputs and add marker_${c}`,fr:`construit un dictionnaire depuis des entrées parallèles et ajoute marker_${c}`,body:`result = dict(zip(keys, values))\n    result["marker_${c}"] = ${c}\n    return result`,inputs:[[['a','b'],[1,2]],[['x'],[5,6]],[[],[]]],eval:(k,v)=>({...Object.fromEntries(k.slice(0,Math.min(k.length,v.length)).map((x,i)=>[x,v[i]])),[`marker_${c}`]:c}),calls:['zip','dict']},
    {name:`enumerate_zip_rows_${c}`,params:'names, scores',en:`return rank-name-score lists beginning at rank ${c}`,fr:`retourne les listes rang-nom-score à partir du rang ${c}`,body:`return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=${c})]`,inputs:[[['A','B'],[9,8]],[['X'],[1,2]],[[],[]]],eval:(n,s)=>n.slice(0,Math.min(n.length,s.length)).map((x,i)=>[i+c,x,s[i]]),calls:['enumerate','zip']},
    {name:`zip_differences_${c}`,params:'left, right',en:`return absolute parallel differences plus ${c}`,fr:`retourne les différences absolues parallèles plus ${c}`,body:`return [abs(a - b) + ${c} for a, b in zip(left, right)]`,inputs:[[[1,5],[4,2]],[[0],[0,1]],[[],[]]],eval:(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>Math.abs(x-b[i])+c),calls:['zip']},
    {name:`zip_longest_fill_${c}`,params:'left, right',en:`zip all values into lists using ${c} as the fill value`,fr:`combine toutes les valeurs en listes en utilisant ${c} comme remplissage`,imports:'from itertools import zip_longest',body:`return [list(pair) for pair in zip_longest(left, right, fillvalue=${c})]`,inputs:[[[1,2],['a']],[[1],['a','b']],[[],[]]],eval:(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>[i<a.length?a[i]:c,i<b.length?b[i]:c]),calls:['zip_longest']},
    {name:`indexed_products_${c}`,params:'left, right',en:`multiply parallel values and add their index plus ${c}`,fr:`multiplie les valeurs parallèles et ajoute leur indice plus ${c}`,body:`return [a * b + index + ${c} for index, (a, b) in enumerate(zip(left, right))]`,inputs:[[[2,3],[4,5]],[[1],[9,8]],[[],[]]],eval:(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>x*b[i]+i+c),calls:['enumerate','zip']},
  ]; const d=defs[family]; add({concept:'Enumerate & Zip',...d,cases:tests(d.inputs,d.eval),calls:d.calls,focus:'enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values'});
}

const expected = {'Sorting Key':150,'Testing & Debugging':50,'Type Hint':50,'Exceptions':50,'Equality & Identity':50,'Enumerate & Zip':100};
if (specs.length !== 450) throw new Error(`Expected 450 specs, found ${specs.length}`);
for (const [concept,count] of Object.entries(expected)) if (specs.filter(spec=>spec.concept===concept).length!==count) throw new Error(`${concept} count mismatch`);
if (new Set(specs.map(spec=>spec.name)).size !== specs.length) throw new Error('Duplicate function names');

const labelsFr={'Sorting Key':'clés de tri','Testing & Debugging':'tests et débogage','Type Hint':'annotations de type','Exceptions':'exceptions','Equality & Identity':'égalité et identité','Enumerate & Zip':'enumerate et zip'};
const levelsFr={Easy:'Facile',Intermediate:'Intermédiaire',Difficult:'Expert'};
const exercises=[], graders={}, french={};
const invoke=(spec,test,name=spec.name)=>`${name}(${test.args.map(py).join(', ')})`;

specs.forEach((spec,index)=>{
  const id=START_ID+index, level=levelFor(spec.concept,index-(Object.keys(expected).slice(0,Object.keys(expected).indexOf(spec.concept)).reduce((n,key)=>n+expected[key],0)));
  const imports=spec.imports?`${spec.imports}\n\n`:'';
  const signature=`def ${spec.name}(${spec.params})${spec.returnType?` -> ${spec.returnType}`:''}:`;
  const definition=`${signature}\n    ${spec.body}`;
  const argumentNames=parameterNames(spec.params);
  const solution=`${imports}# Example 1: canonical function approach\n${definition}\n\nprint(${invoke(spec,spec.cases[0])})  # Expected: ${py(spec.cases[0].expected)}\nprint(${invoke(spec,spec.cases[1])})  # Expected: ${py(spec.cases[1].expected)}\n\n# Example 2: named wrapper approach\ndef solve_problem_${id}(${spec.params}):\n    return ${spec.name}(${argumentNames.join(', ')})\n\n# Example 3: static method approach\nclass Problem${id}Solution:\n    @staticmethod\n${definition.split('\n').map(line=>`    ${line}`).join('\n')}\n\n# Example 4: assigned result approach\nresult = ${invoke(spec,spec.cases[0])}\nprint(result)\n\n# Example 5: boundary case\nprint(${invoke(spec,spec.cases[2])})`;
  exercises.push({id,title:`Problem ${id}`,description:`Write a Python function called \`${spec.name}\` that must ${spec.en}. Practice ${spec.concept.toLowerCase()}.\nDifficulty: ${level==='Difficult'?'Expert':level}.\nExamples:\n  ${invoke(spec,spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec,spec.cases[1])} -> ${py(spec.cases[1].expected)}`,initialCode:`${imports}${signature}\n    pass`,solution,hint:`Focus on ${spec.focus}. Derive the behavior from the task instead of copying an example output.`,breakdown:`1. Identify every input type and the exact return type.\n2. Apply the required ${spec.concept.toLowerCase()} rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.`,category:`${spec.concept} ${level}`});
  const grader={functionNames:[spec.name],tests:spec.cases};
  if(spec.calls) grader.requiredCallPatterns=spec.calls.map(functionName=>({functionName,minArgs:0}));
  if(spec.nodes) grader.requiredNodePatterns=spec.nodes;
  if(spec.operators) grader.requiredAstOperators=spec.operators;
  if(spec.typeHints) grader.requiredTypeHints=spec.typeHints;
  graders[id]=grader;
  french[id]={description:`Écrivez une fonction Python appelée \`${spec.name}\` qui ${spec.fr}. Entraînez-vous avec ${labelsFr[spec.concept]}.\nDifficulté : ${levelsFr[level]}.\nExemples :\n  ${invoke(spec,spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec,spec.cases[1])} -> ${py(spec.cases[1].expected)}`,hint:`Concentrez-vous sur ${labelsFr[spec.concept]}, les types d’entrée et le comportement demandé. Ne copiez pas une sortie d’exemple.`,breakdown:`1. Identifiez chaque type d’entrée et le type de retour.\n2. Appliquez la règle de ${labelsFr[spec.concept]} demandée.\n3. Suivez les valeurs intermédiaires dans l’ordre.\n4. Vérifiez les cas vides, invalides, égaux ou limites.\n5. Retournez un résultat général valable pour les tests cachés.`};
});

fs.writeFileSync(path.join(root,'supplementalConceptExercises.ts'),`import type { Exercise } from './types';\n\nexport const SUPPLEMENTAL_CONCEPT_EXERCISES: Exercise[] = ${JSON.stringify(exercises,null,2)};\n`);
fs.writeFileSync(path.join(root,'supplementalConceptGraders.ts'),`import type { AutoGrader } from './graders';\n\nexport const SUPPLEMENTAL_CONCEPT_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders,null,2)};\n`);
fs.writeFileSync(path.join(root,'services/supplementalConceptFr.ts'),`export const SUPPLEMENTAL_CONCEPT_FR: Record<number, { description: string; hint: string; breakdown: string }> = ${JSON.stringify(french,null,2)};\n`);
console.log(`Generated ${specs.length} supplemental exercises (${START_ID}-${START_ID+specs.length-1}).`);

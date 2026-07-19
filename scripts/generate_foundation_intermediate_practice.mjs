#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const START_ID = 3658;
const PACK_SIZE = 100;
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
const cases = (inputs, evaluate) => inputs.map(args => ({ args, expected: evaluate(...args) }));
const levelFor = (track, index) => track === 'beginner' ? (index < 70 ? 'Easy' : 'Intermediate') : (index < 25 ? 'Easy' : 'Intermediate');
const targets = ['a', 'e', 'i', 'o', 'u', 'x', 'y', 'z', '1', '-'];
const separators = [',', ';', '|', ':', '/', '-', '_', '.', '+', ' '];
const longText = ['abcdefghijkl', 'PYTHONcoding', '0123456789xy'];
const longLists = [Array.from({ length: 12 }, (_, i) => i + 1), Array.from({ length: 12 }, (_, i) => (i + 1) * 3), Array.from({ length: 12 }, (_, i) => 20 - i)];

// Beginner 1: Indexing.
for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 10);
  const k = index % 10;
  const definitions = [
    [`character_at_${k}`, `return character ${k} from a string using positive indexing`, `retourne le caractère ${k} d’une chaîne avec un indice positif`, 'text', `return text[${k}]`, cases(longText.map(text => [text]), text => text[k]), [{ nodeType: 'Subscript' }]],
    [`character_from_end_${k + 1}`, `return character ${k + 1} from the end of a string`, `retourne le caractère ${k + 1} depuis la fin d’une chaîne`, 'text', `return text[-${k + 1}]`, cases(longText.map(text => [text]), text => text.at(-(k + 1))), [{ nodeType: 'Subscript' }]],
    [`list_item_at_${k}`, `return list item ${k} using positive indexing`, `retourne l’élément ${k} d’une liste avec un indice positif`, 'values', `return values[${k}]`, cases(longLists.map(values => [values]), values => values[k]), [{ nodeType: 'Subscript' }]],
    [`list_item_from_end_${k + 1}`, `return list item ${k + 1} from the end`, `retourne l’élément ${k + 1} depuis la fin`, 'values', `return values[-${k + 1}]`, cases(longLists.map(values => [values]), values => values.at(-(k + 1))), [{ nodeType: 'Subscript' }]],
    [`adjacent_characters_${k}`, `join string characters ${k} and ${k + 1}`, `joint les caractères ${k} et ${k + 1} d’une chaîne`, 'text', `return text[${k}] + text[${k + 1}]`, cases(longText.map(text => [text]), text => text[k] + text[k + 1]), [{ nodeType: 'Subscript', minCount: 2 }]],
    [`adjacent_item_sum_${k}`, `add list items ${k} and ${k + 1}`, `additionne les éléments ${k} et ${k + 1} d’une liste`, 'values', `return values[${k}] + values[${k + 1}]`, cases(longLists.map(values => [values]), values => values[k] + values[k + 1]), [{ nodeType: 'Subscript', minCount: 2 }]],
    [`opposite_items_${k}`, `return a tuple containing list item ${k} and item ${k + 1} from the end`, `retourne un tuple avec l’élément ${k} et l’élément ${k + 1} depuis la fin`, 'values', `return values[${k}], values[-${k + 1}]`, cases(longLists.map(values => [values]), values => [values[k], values.at(-(k + 1))]), [{ nodeType: 'Subscript', minCount: 2 }, { nodeType: 'Tuple' }]],
    [`swap_adjacent_${k}`, `return a copy with items ${k} and ${k + 1} swapped`, `retourne une copie où les éléments ${k} et ${k + 1} sont échangés`, 'values', `result = values.copy()\n    result[${k}], result[${k + 1}] = result[${k + 1}], result[${k}]\n    return result`, cases(longLists.map(values => [values]), values => { const out = [...values]; [out[k], out[k + 1]] = [out[k + 1], out[k]]; return out; }), [{ nodeType: 'Subscript', minCount: 4 }]],
    [`matrix_position_${k}`, `return matrix cell at row ${Math.floor(k / 4)} and column ${k % 4}`, `retourne la cellule de matrice à la ligne ${Math.floor(k / 4)} et colonne ${k % 4}`, 'matrix', `return matrix[${Math.floor(k / 4)}][${k % 4}]`, cases([[[[1,2,3,4],[5,6,7,8],[9,10,11,12]]], [[[12,11,10,9],[8,7,6,5],[4,3,2,1]]], [[[2,4,6,8],[10,12,14,16],[18,20,22,24]]]], matrix => matrix[Math.floor(k / 4)][k % 4]), [{ nodeType: 'Subscript', minCount: 2 }]],
    [`mapping_value_by_position_${k}`, `return the dictionary value belonging to key position ${k}`, `retourne la valeur du dictionnaire correspondant à la position de clé ${k}`, 'mapping', `key = list(mapping)[${k}]\n    return mapping[key]`, cases([
      [Object.fromEntries(Array.from({length:12},(_,i)=>[`k${i}`,i+10]))],
      [Object.fromEntries(Array.from({length:12},(_,i)=>[`item${i}`,(i+1)*2]))],
      [Object.fromEntries(Array.from({length:12},(_,i)=>[`v${i}`,100-i]))],
    ], mapping => mapping[Object.keys(mapping)[k]]), [{ nodeType: 'Subscript', minCount: 2 }]],
  ];
  const [name, en, fr, params, body, testCases, nodes] = definitions[family];
  add({ concept: 'Indexing', key: 'indexing', track: 'beginner', name, en, fr, params, body, cases: testCases, nodes, focus: 'zero-based positions, negative positions, and the exact indexed value' });
}

// Beginner 2: String methods.
for (let index = 0; index < PACK_SIZE; index += 1) {
  const family = Math.floor(index / 10);
  const k = index % 10;
  const target = targets[k];
  const sep = separators[k];
  const textCases = [['abracadabra'], ['example-text-123'], ['Python is practical']];
  const wordCases = [[['red','green','blue']], [['a','bb','ccc']], [['Python','code']]];
  const definitions = [
    [`count_${k}_string_method`, `count ${py(target)} with str.count()`, `compte ${py(target)} avec str.count()`, 'text', `return text.count(${py(target)})`, cases(textCases, text => text.split(target).length - 1), ['count']],
    [`replace_${k}_string_method`, `replace every ${py(target)} with "*"`, `remplace chaque ${py(target)} par "*"`, 'text', `return text.replace(${py(target)}, "*")`, cases(textCases, text => text.split(target).join('*')), ['replace']],
    [`find_${k}_string_method`, `find the first position of ${py(target)}`, `trouve la première position de ${py(target)}`, 'text', `return text.find(${py(target)})`, cases(textCases, text => text.indexOf(target)), ['find']],
    [`starts_${k}_string_method`, `test whether text starts with ${py(target)}`, `teste si le texte commence par ${py(target)}`, 'text', `return text.startswith(${py(target)})`, cases(textCases, text => text.startsWith(target)), ['startswith']],
    [`ends_${k}_string_method`, `test whether text ends with ${py(target)}`, `teste si le texte se termine par ${py(target)}`, 'text', `return text.endswith(${py(target)})`, cases(textCases, text => text.endsWith(target)), ['endswith']],
    [`split_${k}_string_method`, `split text wherever ${py(sep)} appears`, `sépare le texte partout où ${py(sep)} apparaît`, 'text', `return text.split(${py(sep)})`, cases([[`a${sep}b${sep}c`], [`one${sep}two`], ['plain']], text => text.split(sep)), ['split']],
    [`join_${k}_string_method`, `join words with ${py(sep)}`, `joint les mots avec ${py(sep)}`, 'words', `return ${py(sep)}.join(words)`, cases(wordCases, words => words.join(sep)), ['join']],
    [`strip_${k}_string_method`, `strip ${py(target)} from both ends`, `retire ${py(target)} aux deux extrémités`, 'text', `return text.strip(${py(target)})`, cases([[`${target}${target}hello${target}`], [`${target}code${target}${target}`], ['plain']], text => text.replace(new RegExp(`^[${target.replace(/[\\\]\-^]/g,'\\$&')}]+|[${target.replace(/[\\\]\-^]/g,'\\$&')}]+$`,'g'),'')), ['strip']],
    [`partition_${k}_string_method`, `partition text at the first ${py(sep)}`, `partitionne le texte au premier ${py(sep)}`, 'text', `return text.partition(${py(sep)})`, cases([[`left${sep}right`], [`a${sep}b${sep}c`], ['plain']], text => { const p=text.indexOf(sep); return p<0?[text,'','']:[text.slice(0,p),sep,text.slice(p+sep.length)]; }), ['partition']],
    [`casefold_${k}_string_method`, `casefold text and count ${py(target.toLowerCase())}`, `normalise la casse puis compte ${py(target.toLowerCase())}`, 'text', `return text.casefold().count(${py(target.toLowerCase())})`, cases([['AbrAcadAbra'], ['EXAMPLE xyz'], ['Python Is Practical']], text => text.toLowerCase().split(target.toLowerCase()).length-1), ['casefold','count']],
  ];
  const [name,en,fr,params,body,testCases,calls]=definitions[family];
  add({ concept:'String Method',key:'stringMethods',track:'beginner',name,en,fr,params,body,cases:testCases,calls,focus:'the receiver string, method argument, returned value, and whether the original text changes' });
}

// Beginner 3: List methods.
for (let index=0; index<PACK_SIZE; index+=1) {
  const family=Math.floor(index/10), k=index%10, value=k+1;
  const inputs=[[[1,2,3]], [[3,1,2]], [[value,9,value]]];
  const definitions=[
    [`append_${value}_list_method`,`append ${value} to a copied list`,`ajoute ${value} à une copie de liste`,'values',`result = values.copy()\n    result.append(${value})\n    return result`,cases(inputs,v=>[...v,value]),['copy','append']],
    [`extend_${value}_list_method`,`extend a copied list with ${value} and ${value+1}`,`étend une copie avec ${value} et ${value+1}`,'values',`result = values.copy()\n    result.extend([${value}, ${value+1}])\n    return result`,cases(inputs,v=>[...v,value,value+1]),['copy','extend']],
    [`insert_${k}_list_method`,`insert ${value} at position ${k%4}`,`insère ${value} à la position ${k%4}`,'values',`result = values.copy()\n    result.insert(${k%4}, ${value})\n    return result`,cases(inputs,v=>{const o=[...v];o.splice(k%4,0,value);return o;}),['copy','insert']],
    [`count_${value}_list_method`,`count occurrences of ${value}`,`compte les occurrences de ${value}`,'values',`return values.count(${value})`,cases(inputs,v=>v.filter(x=>x===value).length),['count']],
    [`index_${value}_list_method`,`return the first index of ${value}, or -1 when absent`,`retourne le premier indice de ${value}, ou -1 s’il est absent`,'values',`return values.index(${value}) if ${value} in values else -1`,cases(inputs,v=>v.indexOf(value)),['index']],
    [`remove_${value}_list_method`,`remove the first ${value} from a copied list when present`,`retire le premier ${value} d’une copie s’il existe`,'values',`result = values.copy()\n    if ${value} in result:\n        result.remove(${value})\n    return result`,cases(inputs,v=>{const o=[...v],p=o.indexOf(value);if(p>=0)o.splice(p,1);return o;}),['copy','remove']],
    [`pop_${k}_list_method`,`pop position ${k%3} from a copied list and add ${value} to the removed value`,`retire la position ${k%3} d’une copie et ajoute ${value} à la valeur retirée`,'values',`result = values.copy()\n    return result.pop(${k%3}) + ${value}`,cases(inputs,v=>v[k%3]+value),['copy','pop']],
    [`reverse_${k}_list_method`,`reverse a copied list then append marker ${value}`,`inverse une copie puis ajoute le marqueur ${value}`,'values',`result = values.copy()\n    result.reverse()\n    result.append(${value})\n    return result`,cases(inputs,v=>[...v].reverse().concat(value)),['copy','reverse','append']],
    [`sort_${k}_list_method`,`sort a copied list then insert ${value} at the front`,`trie une copie puis insère ${value} au début`,'values',`result = values.copy()\n    result.sort()\n    result.insert(0, ${value})\n    return result`,cases(inputs,v=>[value,...v].slice(1).sort((a,b)=>a-b).reduce((a,x)=>a.concat(x),[value])),['copy','sort','insert']],
    [`clear_${k}_list_method`,`clear a copied list and append its former length plus ${value}`,`vide une copie puis ajoute son ancienne longueur plus ${value}`,'values',`result = values.copy()\n    old_length = len(result)\n    result.clear()\n    result.append(old_length + ${value})\n    return result`,cases(inputs,v=>[v.length+value]),['copy','clear','append']],
  ];
  const [name,en,fr,params,body,testCases,calls]=definitions[family];
  add({concept:'List Method',key:'listMethods',track:'beginner',name,en,fr,params,body,cases:testCases,calls,focus:'copying before mutation, the list method side effect, and the returned result'});
}

// Beginner 4: Dictionary methods.
for (let index=0;index<PACK_SIZE;index+=1){
  const family=Math.floor(index/10),k=index%10,key=`k${k}`,value=(k+1)*10;
  const inputs=[[{a:1,b:2,[key]:value}],[{x:5,y:7}],[{[key]:k,z:9}]];
  const definitions=[
    [`get_${key}_dict_method`,`get key ${py(key)} with default ${value}`,`obtient la clé ${py(key)} avec la valeur par défaut ${value}`,'mapping',`return mapping.get(${py(key)}, ${value})`,cases(inputs,m=>Object.hasOwn(m,key)?m[key]:value),['get']],
    [`keys_${k}_dict_method`,`return the first ${k%3+1} keys followed by marker ${py(key)}`,`retourne les ${k%3+1} premières clés suivies du marqueur ${py(key)}`,'mapping',`return list(mapping.keys())[:${k%3+1}] + [${py(key)}]`,cases(inputs,m=>Object.keys(m).slice(0,k%3+1).concat(key)),['keys','list']],
    [`values_${k}_dict_method`,`return the sum of values plus ${k}`,`retourne la somme des valeurs plus ${k}`,'mapping',`return sum(mapping.values()) + ${k}`,cases(inputs,m=>Object.values(m).reduce((a,b)=>a+b,0)+k),['values','sum']],
    [`items_${k}_dict_method`,`return key-value pairs whose value is at least ${k}`,`retourne les paires dont la valeur vaut au moins ${k}`,'mapping',`return [(key, value) for key, value in mapping.items() if value >= ${k}]`,cases(inputs,m=>Object.entries(m).filter(([,v])=>v>=k)),['items']],
    [`update_${key}_dict_method`,`update a copy with ${py(key)} mapped to ${value}`,`met à jour une copie avec ${py(key)} associé à ${value}`,'mapping',`result = mapping.copy()\n    result.update({${py(key)}: ${value}})\n    return result`,cases(inputs,m=>({...m,[key]:value})),['copy','update']],
    [`pop_${key}_dict_method`,`pop ${py(key)} from a copy and return its value or ${value}`,`retire ${py(key)} d’une copie et retourne sa valeur ou ${value}`,'mapping',`result = mapping.copy()\n    return result.pop(${py(key)}, ${value})`,cases(inputs,m=>Object.hasOwn(m,key)?m[key]:value),['copy','pop']],
    [`popitem_${k}_dict_method`,`pop the last pair from a copy after assigning marker ${py(key)}`,`retire la dernière paire après avoir affecté le marqueur ${py(key)}`,'mapping',`result = mapping.copy()\n    result[${py(key)}] = ${value}\n    return result.popitem()`,cases(inputs,m=>{const result={...m};result[key]=value;const last=Object.keys(result).at(-1);return [last,result[last]];}),['copy','popitem']],
    [`setdefault_${key}_dict_method`,`set default ${value} for ${py(key)} in a copy`,`définit ${value} par défaut pour ${py(key)} dans une copie`,'mapping',`result = mapping.copy()\n    result.setdefault(${py(key)}, ${value})\n    return result`,cases(inputs,m=>Object.hasOwn(m,key)?{...m}:{...m,[key]:value}),['copy','setdefault']],
    [`fromkeys_${k}_dict_method`,`create a dictionary from existing keys with value ${k}`,`crée un dictionnaire avec les clés existantes et la valeur ${k}`,'mapping',`return dict.fromkeys(mapping.keys(), ${k})`,cases(inputs,m=>Object.fromEntries(Object.keys(m).map(x=>[x,k]))),['fromkeys','keys']],
    [`clear_${k}_dict_method`,`clear a copy and store the former size under ${py(key)}`,`vide une copie et stocke l’ancienne taille sous ${py(key)}`,'mapping',`result = mapping.copy()\n    size = len(result)\n    result.clear()\n    result[${py(key)}] = size\n    return result`,cases(inputs,m=>({[key]:Object.keys(m).length})),['copy','clear']],
  ];
  const [name,en,fr,params,body,testCases,calls]=definitions[family];
  add({concept:'Dictionary Method',key:'dictionaryMethods',track:'beginner',name,en,fr,params,body,cases:testCases,calls,focus:'dictionary keys, method defaults, mutation versus copying, and the returned value'});
}

const numericInputs=[[5],[-4],[0]];
const baseNumericOperation=(family,k,variable='value')=>{
  const c=k+1;
  const defs=[
    [`add_${c}`,`add ${c}`,`ajoute ${c}`,`${variable} + ${c}`,(v)=>v+c],
    [`multiply_${c}`,`multiply by ${c}`,`multiplie par ${c}`,`${variable} * ${c}`,(v)=>v*c],
    [`power_${c+1}`,`raise to power ${c+1}`,`élève à la puissance ${c+1}`,`${variable} ** ${c+1}`,(v)=>v**(c+1)],
    [`distance_${c}`,`measure distance from ${c}`,`mesure la distance depuis ${c}`,`abs(${variable} - ${c})`,(v)=>Math.abs(v-c)],
    [`modulo_${c+1}`,`return modulo ${c+1}`,`retourne modulo ${c+1}`,`${variable} % ${c+1}`,(v)=>((v%(c+1))+(c+1))%(c+1)],
    [`at_least_${c}`,`test whether it is at least ${c}`,`teste si elle vaut au moins ${c}`,`${variable} >= ${c}`,(v)=>v>=c],
    [`within_${c}`,`test whether its absolute value is within ${c}`,`teste si sa valeur absolue ne dépasse pas ${c}`,`abs(${variable}) <= ${c}`,(v)=>Math.abs(v)<=c],
    [`label_${c}`,`return "high" when it exceeds ${c}, otherwise "low"`,`retourne « high » si elle dépasse ${c}, sinon « low »`,`"high" if ${variable} > ${c} else "low"`,(v)=>v>c?'high':'low'],
    [`clamp_${c}`,`clamp it to a maximum of ${c}`,`la limite à un maximum de ${c}`,`min(${variable}, ${c})`,(v)=>Math.min(v,c)],
    [`offset_square_${c}`,`square it then add ${c}`,`la met au carré puis ajoute ${c}`,`${variable} ** 2 + ${c}`,(v)=>v**2+c],
  ];
  return defs[family];
};

// Beginner 5: Print versus return.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10;const [suffix,enOp,frOp,expression,evaluate]=baseNumericOperation(family,k);add({concept:'Print vs Return',key:'printReturn',track:'beginner',name:`return_${suffix}`,en:`return the result after you ${enOp}; do not only print it`,fr:`retourne le résultat après avoir effectué ceci : ${frOp} ; ne l’affiche pas seulement`,params:'value',body:`result = ${expression}\n    return result`,cases:cases(numericInputs,evaluate),nodes:[{nodeType:'Return'}],focus:'the difference between displaying a value with print() and sending it back with return'});}

// Beginner 6: Function arguments.
for(let index=0;index<PACK_SIZE;index+=1){
  const family=Math.floor(index/10),k=index%10,c=k+1;
  const defs=[
    [`positional_${k}`,'first, second',`add two positional arguments and ${c}`,`additionne deux arguments positionnels et ${c}`,'return first + second + '+c,cases([[1,2],[5,-2],[0,0]],(a,b)=>a+b+c)],
    [`default_${k}`,'value, amount = '+c,`use a default argument of ${c} when adding an amount`,`utilise un argument par défaut de ${c} pour ajouter une quantité`,'return value + amount',[{args:[5],expected:5+c},{args:[2,3],expected:5},{args:[-1,c],expected:c-1}]],
    [`keyword_${k}`,'value, *, amount = '+c,`use a keyword-only amount with default ${c}`,`utilise une quantité nommée seulement avec ${c} par défaut`,'return value * amount',[{args:[3],expected:3*c},{args:[2],kwargs:{amount:4},expected:8},{args:[-1],kwargs:{amount:2},expected:-2}]],
    [`variadic_${k}`,'*values',`sum every positional argument then add ${c}`,`additionne tous les arguments positionnels puis ajoute ${c}`,'return sum(values) + '+c,[{args:[1,2,3],expected:6+c},{args:[5],expected:5+c},{args:[],expected:c}]],
    [`keyword_values_${k}`,'**values',`sum every keyword argument value then add ${c}`,`additionne toutes les valeurs des arguments nommés puis ajoute ${c}`,'return sum(values.values()) + '+c,[{args:[],kwargs:{a:1,b:2},expected:3+c},{args:[],kwargs:{x:5},expected:5+c},{args:[],kwargs:{},expected:c}]],
    [`mixed_${k}`,'first, second, bonus = '+c,`combine two required arguments and optional bonus ${c}`,`combine deux arguments requis et le bonus facultatif ${c}`,'return first * second + bonus',[{args:[2,3],expected:6+c},{args:[2,3,4],expected:10},{args:[-1,5],expected:-5+c}]],
    [`prefix_${k}`,'text, prefix = '+py(String(c)),`prepend a default text argument ${py(String(c))}`,`ajoute le texte par défaut ${py(String(c))} au début`,'return prefix + text',[{args:['code'],expected:String(c)+'code'},{args:['x','P:'],expected:'P:x'},{args:[''],expected:String(c)}]],
    [`start_total_${k}`,'values, start = '+c,`sum a list from starting value ${c}`,`additionne une liste à partir de ${c}`,'return sum(values, start)',[{args:[[1,2]],expected:3+c},{args:[[],5],expected:5},{args:[[-1,1]],expected:c}]],
    [`positional_only_${k}`,'value, /, amount = '+c,`use a positional-only value and default amount ${c}`,`utilise une valeur positionnelle seulement et ${c} par défaut`,'return value - amount',[{args:[10],expected:10-c},{args:[10,3],expected:7},{args:[-1,c],expected:-1-c}]],
    [`named_pair_${k}`,'*, left, right = '+c,`use keyword-only left and right arguments with right default ${c}`,`utilise des arguments nommés left et right avec ${c} par défaut`,'return left + right',[{args:[],kwargs:{left:2},expected:2+c},{args:[],kwargs:{left:3,right:4},expected:7},{args:[],kwargs:{left:-1},expected:c-1}]],
  ];
  const [name,params,en,fr,body,testCases]=defs[family];add({concept:'Function Argument',key:'functionArguments',track:'beginner',name,en,fr,params,body,cases:testCases,focus:'the parameter order, defaults, positional or keyword calling rules, and the resulting binding'});
}

// Beginner 7: Boolean logic.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`between_${c}`,`test whether a number is between ${-c} and ${c}`,`teste si un nombre est entre ${-c} et ${c}`,'value',`return value >= ${-c} and value <= ${c}`,cases(numericInputs,v=>v>=-c&&v<=c),['And']],
 [`outside_${c}`,`test whether a number is below ${-c} or above ${c}`,`teste si un nombre est inférieur à ${-c} ou supérieur à ${c}`,'value',`return value < ${-c} or value > ${c}`,cases(numericInputs,v=>v<-c||v>c),['Or']],
 [`not_equal_${c}`,`use not to test that a number does not equal ${c}`,`utilise not pour tester qu’un nombre n’est pas égal à ${c}`,'value',`return not value == ${c}`,cases(numericInputs,v=>v!==c),[]],
 [`positive_even_${c}`,`test whether a number is positive and divisible by ${c+1}`,`teste si un nombre est positif et divisible par ${c+1}`,'value',`return value > 0 and value % ${c+1} == 0`,cases(numericInputs,v=>v>0&&v%(c+1)===0),['And']],
 [`empty_or_short_${c}`,`test whether text is empty or shorter than ${c}`,`teste si le texte est vide ou plus court que ${c}`,'text',`return not text or len(text) < ${c}`,cases([[''],['cat'],['python coding']],t=>!t||t.length<c),['Or']],
 [`starts_and_ends_${k}`,`test whether text starts with ${py(targets[k])} and ends with the same character`,`teste si le texte commence et finit par ${py(targets[k])}`,'text',`return text.startswith(${py(targets[k])}) and text.endswith(${py(targets[k])})`,cases([[targets[k]+'middle'+targets[k]],['plain'],[targets[k]]],t=>t.startsWith(targets[k])&&t.endsWith(targets[k])),['And']],
 [`all_or_none_${c}`,`test whether both values are truthy or both are falsy for variant ${c}`,`teste si les deux valeurs sont vraies ou toutes deux fausses, variante ${c}`,'left, right',`return (bool(left) and bool(right)) or (not left and not right)`,cases([[1,2],[0,3],['','']],(a,b)=>(!!a&&!!b)||(!a&&!b)),['And','Or']],
 [`exclusive_${c}`,`test whether exactly one of two values is truthy for variant ${c}`,`teste si exactement une des deux valeurs est vraie, variante ${c}`,'left, right',`return bool(left) != bool(right)`,cases([[1,0],[0,0],['x','y']],(a,b)=>!!a!==!!b),[]],
 [`valid_length_${c}`,`test whether a list is non-empty and has at most ${c+2} items`,`teste si une liste n’est pas vide et contient au plus ${c+2} éléments`,'values',`return bool(values) and len(values) <= ${c+2}`,cases([[[1]], [Array.from({length:c+3},(_,i)=>i)], [[]]],v=>v.length>0&&v.length<=c+2),['And']],
 [`none_guard_${c}`,`test that a value is not None and is at least ${c}`,`teste qu’une valeur n’est pas None et vaut au moins ${c}`,'value',`return value is not None and value >= ${c}`,cases([[c],[c-1],[null]],v=>v!==null&&v>=c),['And']],
];const [name,en,fr,params,body,testCases,boolOps]=defs[family];add({concept:'Boolean Logic',key:'booleanLogic',track:'beginner',name,en,fr,params,body,cases:testCases,boolOps,focus:'comparison truth values, short-circuit order, and how and, or, and not combine conditions'});}

// Beginner 8: Input parsing (functions receive the raw text so hidden cases stay deterministic).
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1,sep=separators[k];const defs=[
 [`parse_integer_${c}`,`convert stripped integer text and add ${c}`,`convertit un entier texte nettoyé puis ajoute ${c}`,'raw',`return int(raw.strip()) + ${c}`,cases([[' 12 '],['-3'],['0']],r=>parseInt(r.trim(),10)+c),['strip','int']],
 [`parse_float_${c}`,`convert decimal text and multiply by ${c}`,`convertit un décimal texte puis multiplie par ${c}`,'raw',`return float(raw.strip()) * ${c}`,cases([['2.5'],['-1.25'],['0']],r=>parseFloat(r.trim())*c),['strip','float']],
 [`parse_words_${c}`,`split whitespace text and return at most ${c} words`,`sépare le texte par espaces et retourne au plus ${c} mots`,'raw',`return raw.split()[:${c}]`,cases([['one two three four'],['  a   b '],['']],r=>r.trim()?r.trim().split(/\s+/).slice(0,c):[]),['split']],
 [`parse_delimited_${k}`,`split raw text on ${py(sep)}`,`sépare le texte brut sur ${py(sep)}`,'raw',`return raw.split(${py(sep)})`,cases([[`a${sep}b${sep}c`],[`one${sep}two`],['plain']],r=>r.split(sep)),['split']],
 [`parse_number_list_${k}`,`parse ${py(sep)}-separated integers into a list`,`analyse des entiers séparés par ${py(sep)} dans une liste`,'raw',`return [int(part.strip()) for part in raw.split(${py(sep)})]`,cases([[`1${sep}2${sep}3`],[`4${sep}5`],[`0`]],r=>r.split(sep).map(x=>parseInt(x.trim(),10))),['split','int']],
 [`parse_number_total_${k}`,`sum integers separated by ${py(sep)} plus ${c}`,`additionne les entiers séparés par ${py(sep)} puis ajoute ${c}`,'raw',`return sum(int(part.strip()) for part in raw.split(${py(sep)})) + ${c}`,cases([[`1${sep}2${sep}3`],[`4${sep}5`],['0']],r=>r.split(sep).reduce((a,x)=>a+parseInt(x.trim(),10),c)),['split','int','sum']],
 [`parse_yes_no_${k}`,`parse yes/no text and accept ${py(['yes','true','1','on','y','ok','sure','oui','vrai','active'][k])} as true`,`analyse un texte oui/non et accepte ${py(['yes','true','1','on','y','ok','sure','oui','vrai','active'][k])} comme vrai`,'raw',`return raw.strip().lower() == ${py(['yes','true','1','on','y','ok','sure','oui','vrai','active'][k])}`,cases([[['yes','true','1','on','y','ok','sure','oui','vrai','active'][k]],['no'],[' YES ']],(r)=>r.trim().toLowerCase()===['yes','true','1','on','y','ok','sure','oui','vrai','active'][k]),['strip','lower']],
 [`parse_key_value_${k}`,`split one key/value pair at ${py(sep)} into a tuple`,`sépare une paire clé/valeur sur ${py(sep)} dans un tuple`,'raw',`key, value = raw.split(${py(sep)}, 1)\n    return key.strip(), value.strip()`,cases([[`name${sep}Ada`],[`x${sep} 10`],[`left${sep}right${sep}extra`]],r=>{const p=r.indexOf(sep);return [r.slice(0,p).trim(),r.slice(p+1).trim()];}),['split','strip']],
 [`parse_binary_${c}`,`parse binary text and add ${c}`,`analyse un texte binaire puis ajoute ${c}`,'raw',`return int(raw.strip(), 2) + ${c}`,cases([['101'],['0'],['1111']],r=>parseInt(r.trim(),2)+c),['strip','int']],
 [`parse_csv_field_${k}`,`return field ${k} from a comma-separated line`,`retourne le champ ${k} d’une ligne séparée par des virgules`,'raw',`return raw.split(",")[${k}]`,cases([[Array.from({length:10},(_,i)=>`f${i}`).join(',')],[Array.from({length:10},(_,i)=>String(i)).join(',')],[Array.from({length:10},(_,i)=>`x${9-i}`).join(',')]],r=>r.split(',')[k]),['split']],
];const [name,en,fr,params,body,testCases,calls]=defs[family];add({concept:'Input Parsing',key:'inputParsing',track:'beginner',name,en,fr,params,body,cases:testCases,calls,focus:'raw string input, whitespace, separators, conversion order, and the final Python type'});}

// Beginner 9: range().
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`range_zero_${c}`,`return range(0, n) with every value increased by ${c}`,`retourne range(0, n) avec chaque valeur augmentée de ${c}`,'n',`return [value + ${c} for value in range(n)]`,cases([[0],[3],[6]],n=>Array.from({length:n},(_,i)=>i+c))],
 [`range_start_${c}`,`return integers from ${c} up to n, excluding n`,`retourne les entiers de ${c} jusqu’à n, sans n`,'n',`return list(range(${c}, n))`,cases([[c],[c+3],[c+6]],n=>Array.from({length:Math.max(0,n-c)},(_,i)=>i+c))],
 [`range_step_${c}`,`return values from zero below n using step ${c}`,`retourne les valeurs de zéro à n avec un pas de ${c}`,'n',`return list(range(0, n, ${c}))`,cases([[0],[c*3+1],[c*5]],n=>{const o=[];for(let x=0;x<n;x+=c)o.push(x);return o;})],
 [`range_sum_${c}`,`sum range(1, n + 1) then add ${c}`,`additionne range(1, n + 1) puis ajoute ${c}`,'n',`return sum(range(1, n + 1)) + ${c}`,cases([[0],[3],[7]],n=>n*(n+1)/2+c)],
 [`range_squares_${c}`,`return squares for range(${c}, n)`,`retourne les carrés pour range(${c}, n)`,'n',`return [value ** 2 for value in range(${c}, n)]`,cases([[c],[c+3],[c+6]],n=>Array.from({length:Math.max(0,n-c)},(_,i)=>(i+c)**2))],
 [`range_countdown_${c}`,`count down from n to ${c}, including ${c}`,`compte à rebours de n jusqu’à ${c}, inclus`,'n',`return list(range(n, ${c-1}, -1))`,cases([[c],[c+3],[c+6]],n=>Array.from({length:n-c+1},(_,i)=>n-i))],
 [`range_multiples_${c}`,`return the first n positive multiples of ${c}`,`retourne les n premiers multiples positifs de ${c}`,'n',`return [${c} * value for value in range(1, n + 1)]`,cases([[0],[3],[5]],n=>Array.from({length:n},(_,i)=>c*(i+1)))],
 [`range_indexes_${c}`,`return indexes of text starting at ${c-1}`,`retourne les indices du texte à partir de ${c-1}`,'text',`return list(range(${c-1}, len(text)))`,cases([[''],['python'],['abcdefghijk']],t=>Array.from({length:Math.max(0,t.length-(c-1))},(_,i)=>i+c-1))],
 [`range_pairs_${c}`,`pair range(n) values with each value plus ${c}`,`associe les valeurs de range(n) avec chaque valeur plus ${c}`,'n',`return [(value, value + ${c}) for value in range(n)]`,cases([[0],[3],[5]],n=>Array.from({length:n},(_,i)=>[i,i+c]))],
 [`range_reverse_indexes_${c}`,`return valid list indexes in reverse, skipping ${c-1} from the end`,`retourne les indices valides en sens inverse en sautant ${c-1} depuis la fin`,'values',`return list(range(len(values) - ${c}, -1, -1))`,cases([[[1,2,3]], [Array.from({length:12},(_,i)=>i)], [[]]],v=>{const o=[];for(let i=v.length-c;i>=0;i--)o.push(i);return o;})],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Range Practice',key:'ranges',track:'beginner',name,en,fr,params,body,cases:testCases,calls:['range'],focus:'start, stop, step, excluded stop values, and the sequence range produces'});}

// Beginner 10: Basic validation.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`validate_min_${c}`,`validate that a number is at least ${c}`,`valide qu’un nombre vaut au moins ${c}`,'value',`return value >= ${c}`,cases([[c],[c-1],[c+5]],v=>v>=c)],
 [`validate_max_${c}`,`validate that a number is at most ${c}`,`valide qu’un nombre vaut au plus ${c}`,'value',`return value <= ${c}`,cases([[c],[c+1],[c-5]],v=>v<=c)],
 [`validate_length_${c}`,`validate that text has at least ${c} characters`,`valide qu’un texte contient au moins ${c} caractères`,'text',`return len(text) >= ${c}`,cases([['x'.repeat(c)],['x'.repeat(Math.max(0,c-1))],['x'.repeat(c+2)]],t=>t.length>=c)],
 [`validate_nonempty_${c}`,`validate that a collection is non-empty for rule ${c}`,`valide qu’une collection n’est pas vide pour la règle ${c}`,'values',`return bool(values)`,cases([[[]],[[c]],[[1,2]]],v=>v.length>0)],
 [`validate_type_${c}`,`validate that a value is an integer but not a boolean for rule ${c}`,`valide qu’une valeur est un entier mais pas un booléen pour la règle ${c}`,'value',`return isinstance(value, int) and not isinstance(value, bool)`,cases([[c],[String(c)],[true]],v=>Number.isInteger(v)&&typeof v!=='boolean')],
 [`validate_choice_${c}`,`validate that text is one of option${c}, yes, or no`,`valide que le texte est option${c}, yes ou no`,'text',`return text in {"option${c}", "yes", "no"}`,cases([[`option${c}`],['yes'],['other']],t=>new Set([`option${c}`,'yes','no']).has(t))],
 [`validate_even_${c}`,`validate that a number is even and at least ${c}`,`valide qu’un nombre est pair et vaut au moins ${c}`,'value',`return value % 2 == 0 and value >= ${c}`,cases([[c],[c+1],[c+10]],v=>v%2===0&&v>=c)],
 [`validate_key_${c}`,`validate that dictionary key ${py('k'+c)} exists`,`valide que la clé ${py('k'+c)} existe dans le dictionnaire`,'mapping',`return ${py('k'+c)} in mapping`,cases([[{['k'+c]:1}],[{other:2}],[{}]],m=>Object.hasOwn(m,'k'+c))],
 [`validate_all_${c}`,`validate that every list number is at least ${c}`,`valide que chaque nombre de la liste vaut au moins ${c}`,'values',`return all(value >= ${c} for value in values)`,cases([[[c,c+1]],[[c-1,c]], [[]]],v=>v.every(x=>x>=c))],
 [`validate_optional_${c}`,`accept None or a number at least ${c}`,`accepte None ou un nombre valant au moins ${c}`,'value',`return value is None or value >= ${c}`,cases([[null],[c],[c-1]],v=>v===null||v>=c)],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Basic Validation',key:'basicValidation',track:'beginner',name,en,fr,params,body,cases:testCases,focus:'the accepted boundary, rejected values, data type, and boolean result'});}

// Intermediate 1: enumerate() and zip().
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;let spec;if(family<5){const defs=[
 [`enumerate_offset_${c}`,`pair each item with its index starting at ${c}`,`associe chaque élément à son indice commençant à ${c}`,`return list(enumerate(values, start=${c}))`,(v)=>v.map((x,i)=>[i+c,x])],
 [`enumerate_scaled_${c}`,`pair each item with its zero-based index multiplied by ${c}`,`associe chaque élément à son indice multiplié par ${c}`,`return [(index * ${c}, value) for index, value in enumerate(values)]`,v=>v.map((x,i)=>[i*c,x])],
 [`enumerate_filter_${c}`,`return items whose index is divisible by ${c}`,`retourne les éléments dont l’indice est divisible par ${c}`,`return [value for index, value in enumerate(values) if index % ${c} == 0]`,v=>v.filter((_x,i)=>i%c===0)],
 [`enumerate_dict_${c}`,`map indexes starting at ${c} to their items`,`associe les indices commençant à ${c} à leurs éléments`,`return {index: value for index, value in enumerate(values, start=${c})}`,v=>Object.fromEntries(v.map((x,i)=>[String(i+c),x]))],
 [`enumerate_label_${c}`,`format each item as its index plus ${c} followed by a colon`,`formate chaque élément avec son indice plus ${c} suivi de deux-points`,`return [f"{index + ${c}}:{value}" for index, value in enumerate(values)]`,v=>v.map((x,i)=>`${i+c}:${x}`)],
];const [name,en,fr,body,evaluate]=defs[family];spec={name,en,fr,params:'values',body,cases:cases([[['a','b','c']],[[10,20]], [[]]],evaluate),calls:['enumerate']};}else{const f=family-5;const defs=[
 [`zip_pairs_${c}`,`zip two lists and add ${c} to each right-hand value`,`combine deux listes et ajoute ${c} à chaque valeur de droite`,`return [(left, right + ${c}) for left, right in zip(lefts, rights)]`,(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>[x,b[i]+c])],
 [`zip_sums_${c}`,`zip two number lists and add paired values plus ${c}`,`combine deux listes numériques et additionne les paires plus ${c}`,`return [left + right + ${c} for left, right in zip(lefts, rights)]`,(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>x+b[i]+c)],
 [`zip_products_${c}`,`zip two number lists and multiply each pair by ${c}`,`combine deux listes et multiplie chaque paire par ${c}`,`return [left * right * ${c} for left, right in zip(lefts, rights)]`,(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>x*b[i]*c)],
 [`zip_mapping_${c}`,`zip keys and values after adding ${c} to each value`,`combine des clés et valeurs après avoir ajouté ${c}`,`return dict(zip(keys, [value + ${c} for value in values]))`,(a,b)=>Object.fromEntries(a.slice(0,Math.min(a.length,b.length)).map((x,i)=>[x,b[i]+c]))],
 [`zip_differences_${c}`,`zip two lists and return left minus right minus ${c}`,`combine deux listes et retourne gauche moins droite moins ${c}`,`return [left - right - ${c} for left, right in zip(lefts, rights)]`,(a,b)=>a.slice(0,Math.min(a.length,b.length)).map((x,i)=>x-b[i]-c)],
];const [name,en,fr,body,evaluate]=defs[f];const keyMode=f===3;spec={name,en,fr,params:keyMode?'keys, values':'lefts, rights',body,cases:keyMode?cases([[['a','b'],[1,2]],[['x'],[5,6]],[[],[]]],evaluate):cases([[[1,2,3],[4,5]], [[-1,0],[2,3]], [[],[1]]],evaluate),calls:['zip']};}add({concept:'Enumerate & Zip',key:'enumerateZip',track:'intermediate',...spec,focus:'parallel iteration, shortest-input behavior, index starts, and the produced pairs'});}

// Intermediate 2: Searching and counting.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1,target=targets[k];const defs=[
 [`count_value_${c}`,`count number ${c} in a list`,`compte le nombre ${c} dans une liste`,'values',`return values.count(${c})`,cases([[[c,1,c]],[[1,2]], [[]]],v=>v.filter(x=>x===c).length)],
 [`first_value_${c}`,`find the first index of ${c}, or -1`,`trouve le premier indice de ${c}, ou -1`,'values',`return values.index(${c}) if ${c} in values else -1`,cases([[[0,c,2,c]],[[1,2]], [[]]],v=>v.indexOf(c))],
 [`last_value_${c}`,`find the last index of ${c}, or -1`,`trouve le dernier indice de ${c}, ou -1`,'values',`for index in range(len(values) - 1, -1, -1):\n        if values[index] == ${c}:\n            return index\n    return -1`,cases([[[c,1,c]],[[1,2]], [[]]],v=>v.lastIndexOf(c))],
 [`count_greater_${c}`,`count numbers greater than ${c}`,`compte les nombres supérieurs à ${c}`,'values',`return sum(value > ${c} for value in values)`,cases([[[1,c,c+1,c+2]],[[c]], [[]]],v=>v.filter(x=>x>c).length)],
 [`find_word_length_${c}`,`return the first word with length ${c}, or an empty string`,`retourne le premier mot de longueur ${c}, ou une chaîne vide`,'words',`return next((word for word in words if len(word) == ${c}), "")`,cases([[['a','bb','x'.repeat(c)]],[['no','match']], [[]]],w=>w.find(x=>x.length===c)||'')],
 [`count_character_${k}`,`count ${py(target)} without regard to case`,`compte ${py(target)} sans tenir compte de la casse`,'text',`return text.lower().count(${py(target.toLowerCase())})`,cases([['Abracadabra'],['Example XYZ'],['']],t=>t.toLowerCase().split(target.toLowerCase()).length-1)],
 [`positions_character_${k}`,`return every index containing ${py(target)}`,`retourne chaque indice contenant ${py(target)}`,'text',`return [index for index, char in enumerate(text) if char == ${py(target)}]`,cases([[`a${target}b${target}`],['plain'],['']],t=>[...t].flatMap((x,i)=>x===target?[i]:[]))],
 [`frequency_above_${c}`,`return values appearing at least ${c} times`,`retourne les valeurs apparaissant au moins ${c} fois`,'values',`return [value for value in dict.fromkeys(values) if values.count(value) >= ${c}]`,cases([[Array(c).fill(1).concat(Array(Math.max(0,c-1)).fill(2))],[Array(c+1).fill(c)], [[]]],v=>[...new Set(v)].filter(x=>v.filter(y=>y===x).length>=c))],
 [`nearest_${c}`,`return the number nearest to ${c}`,`retourne le nombre le plus proche de ${c}`,'values',`return min(values, key=lambda value: (abs(value - ${c}), value))`,cases([[[1,5,10]],[[c-1,c+1]], [[c]]],v=>[...v].sort((a,b)=>Math.abs(a-c)-Math.abs(b-c)||a-b)[0])],
 [`count_range_${c}`,`count numbers from ${-c} through ${c}`,`compte les nombres de ${-c} à ${c}`,'values',`return sum(${-c} <= value <= ${c} for value in values)`,cases([[[-c-1,-c,0,c,c+1]],[[0]], [[]]],v=>v.filter(x=>x>=-c&&x<=c).length)],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Searching & Counting',key:'searchingCounting',track:'intermediate',name,en,fr,params,body,cases:testCases,focus:'the search target, first versus all matches, boundary conditions, and count updates'});}

// Intermediate 3: Nested collections.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const matrixInputs=[[[1,2,3],[4,5,6],[7,8,9]],[[c,0,2],[1,c,3],[4,5,c]],[[c,c+1,c+2],[c+3,c+4,c+5],[c+6,c+7,c+8]]];const defs=[
 [`nested_row_sum_${k}`,`sum matrix row ${k%3} and add ${c}`,`additionne la ligne ${k%3} de la matrice puis ajoute ${c}`,'matrix',`return sum(matrix[${k%3}]) + ${c}`,cases(matrixInputs.map(m=>[m]),m=>m[k%3].reduce((a,b)=>a+b,0)+c)],
 [`nested_column_${k}`,`return matrix column ${k%3} with ${c} added to every item`,`retourne la colonne ${k%3} avec ${c} ajouté à chaque élément`,'matrix',`return [row[${k%3}] + ${c} for row in matrix if len(row) > ${k%3}]`,cases(matrixInputs.map(m=>[m]),m=>m.filter(r=>r.length>k%3).map(r=>r[k%3]+c))],
 [`nested_flatten_${c}`,`flatten a matrix and add ${c} to every value`,`aplatit une matrice et ajoute ${c} à chaque valeur`,'matrix',`return [value + ${c} for row in matrix for value in row]`,cases(matrixInputs.map(m=>[m]),m=>m.flat().map(x=>x+c))],
 [`nested_max_${c}`,`return the largest nested value plus ${c}`,`retourne la plus grande valeur imbriquée plus ${c}`,'matrix',`return max(value for row in matrix for value in row) + ${c}`,cases(matrixInputs.map(m=>[m]),m=>Math.max(...m.flat())+c)],
 [`records_field_${k}`,`return field ${py('field'+k)} from every record that contains it`,`retourne le champ ${py('field'+k)} de chaque fiche qui le contient`,'records',`return [record[${py('field'+k)}] for record in records if ${py('field'+k)} in record]`,cases([[[{['field'+k]:1},{x:2},{['field'+k]:3}]], [[{['field'+k]:c}]], [[]]],r=>r.filter(x=>Object.hasOwn(x,'field'+k)).map(x=>x['field'+k]))],
 [`records_total_${k}`,`sum field ${py('field'+k)} across records with default zero`,`additionne le champ ${py('field'+k)} des fiches avec zéro par défaut`,'records',`return sum(record.get(${py('field'+k)}, 0) for record in records)`,cases([[[{['field'+k]:1},{x:2},{['field'+k]:3}]], [[{['field'+k]:c}]], [[]]],r=>r.reduce((a,x)=>a+(x['field'+k]||0),0))],
 [`dict_lists_lengths_${c}`,`add ${c} to the length of every list stored in a dictionary`,`ajoute ${c} à la longueur de chaque liste d’un dictionnaire`,'mapping',`return {key: len(values) + ${c} for key, values in mapping.items()}`,cases([[{a:[1,2],b:[]}],[{x:[1]}],[{}]],m=>Object.fromEntries(Object.entries(m).map(([x,v])=>[x,v.length+c])))],
 [`dict_lists_flatten_${c}`,`flatten dictionary lists and add ${c} to numeric items`,`aplatit les listes du dictionnaire et ajoute ${c} aux nombres`,'mapping',`return [value + ${c} for values in mapping.values() for value in values]`,cases([[{a:[1,2],b:[3]}],[{x:[0]}],[{}]],m=>Object.values(m).flat().map(x=>x+c))],
 [`group_records_${k}`,`group record names by field ${py('group'+k)}`,`regroupe les noms des fiches par le champ ${py('group'+k)}`,'records',`result = {}\n    for record in records:\n        result.setdefault(record[${py('group'+k)}], []).append(record["name"])\n    return result`,cases([[[{name:'a',['group'+k]:'x'},{name:'b',['group'+k]:'x'},{name:'c',['group'+k]:'y'}]], [[{name:'z',['group'+k]:'q'}]], [[]]],r=>{const o={};for(const x of r)(o[x['group'+k]]??=[]).push(x.name);return o;})],
 [`nested_diagonal_${c}`,`return the main diagonal with ${c} added to each value`,`retourne la diagonale principale avec ${c} ajouté`,'matrix',`return [row[index] + ${c} for index, row in enumerate(matrix) if index < len(row)]`,cases(matrixInputs.map(m=>[m]),m=>m.flatMap((r,i)=>i<r.length?[r[i]+c]:[]))],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Nested Collection',key:'nestedCollections',track:'intermediate',name,en,fr,params,body,cases:testCases,focus:'each collection level, inner iteration, missing fields, and the final nested or flattened shape'});}

// Intermediate 4: Sorting keys.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`sort_length_${c}`,`sort strings by length then alphabetically, variant ${c}`,`trie les chaînes par longueur puis alphabet, variante ${c}`,'words','return sorted(words, key=lambda word: (len(word), word))',cases([[['bbb','a','cc']],[['x','aa','b']],[[]]],w=>[...w].sort((a,b)=>a.length-b.length||a.localeCompare(b)))],
 [`sort_last_${c}`,`sort non-empty strings by final character then whole word, variant ${c}`,`trie les chaînes par dernier caractère puis mot, variante ${c}`,'words','return sorted(words, key=lambda word: (word[-1], word))',cases([[['cat','dog','bee']],[['za','ab','aa']],[['x']]],w=>[...w].sort((a,b)=>a.at(-1).localeCompare(b.at(-1))||a.localeCompare(b)))],
 [`sort_abs_${c}`,`sort numbers by distance from ${c} then numeric value`,`trie les nombres par distance depuis ${c} puis valeur`,'values',`return sorted(values, key=lambda value: (abs(value - ${c}), value))`,cases([[[1,5,10]],[[c-2,c+2,c]], [[]]],v=>[...v].sort((a,b)=>Math.abs(a-c)-Math.abs(b-c)||a-b))],
 [`sort_remainder_${c}`,`sort numbers by remainder modulo ${c+1} then value`,`trie les nombres par reste modulo ${c+1} puis valeur`,'values',`return sorted(values, key=lambda value: (value % ${c+1}, value))`,cases([[[5,2,8,1]],[[-1,0,c]], [[]]],v=>[...v].sort((a,b)=>((a%(c+1))+(c+1))%(c+1)-(((b%(c+1))+(c+1))%(c+1))||a-b))],
 [`sort_tuple_${k}`,`sort tuples by position ${k%2}, then add ${c} to each first value`,`trie les tuples par position ${k%2}, puis ajoute ${c} à chaque première valeur`,'pairs',`ordered = sorted(pairs, key=lambda pair: (pair[${k%2}], pair[${1-k%2}]))\n    return [(left + ${c}, right) for left, right in ordered]`,cases([[ [[2,1],[1,3],[1,2]] ],[ [[c,0],[0,c]] ],[ [] ]],p=>[...p].sort((a,b)=>a[k%2]-b[k%2]||a[1-k%2]-b[1-k%2]).map(([a,b])=>[a+c,b]))],
 [`sort_record_${k}`,`sort records by field ${py('field'+k)} then name`,`trie les fiches par ${py('field'+k)} puis nom`,'records',`return sorted(records, key=lambda record: (record[${py('field'+k)}], record["name"]))`,cases([[[{name:'b',['field'+k]:1},{name:'a',['field'+k]:1},{name:'c',['field'+k]:0}]], [[{name:'x',['field'+k]:c}]], [[]]],r=>[...r].sort((a,b)=>a['field'+k]-b['field'+k]||a.name.localeCompare(b.name)))],
 [`sort_digit_sum_${c}`,`sort nonnegative integers by digit sum plus ${c}, then value`,`trie les entiers par somme des chiffres plus ${c}, puis valeur`,'values',`return sorted(values, key=lambda value: (sum(int(digit) for digit in str(value)) + ${c}, value))`,cases([[[12,3,21,10]],[[c,99]], [[]]],v=>[...v].sort((a,b)=>String(a).split('').reduce((s,x)=>s+ +x,0)-String(b).split('').reduce((s,x)=>s+ +x,0)||a-b))],
 [`sort_vowels_${c}`,`sort words by vowel count then length, variant ${c}`,`trie les mots par nombre de voyelles puis longueur, variante ${c}`,'words',`return sorted(words, key=lambda word: (sum(char in "aeiou" for char in word.lower()), len(word), word))`,cases([[['sky','apple','bee']],[['a','bb','io']],[[]]],w=>[...w].sort((a,b)=>[...a.toLowerCase()].filter(x=>'aeiou'.includes(x)).length-[...b.toLowerCase()].filter(x=>'aeiou'.includes(x)).length||a.length-b.length||a.localeCompare(b)))],
 [`sort_casefold_${c}`,`sort text case-insensitively then by original text, variant ${c}`,`trie le texte sans tenir compte de la casse puis par texte original, variante ${c}`,'words','return sorted(words, key=lambda word: (word.casefold(), word))',cases([[['b','A','a']],[['Python','code','Code']],[[]]],w=>[...w].sort((a,b)=>a.toLowerCase()<b.toLowerCase()?-1:a.toLowerCase()>b.toLowerCase()?1:a<b?-1:a>b?1:0))],
 [`sort_desc_field_${k}`,`sort records descending by ${py('score'+k)} and ascending by name`,`trie les fiches par ${py('score'+k)} décroissant puis nom`,'records',`return sorted(records, key=lambda record: (-record[${py('score'+k)}], record["name"]))`,cases([[[{name:'b',['score'+k]:2},{name:'a',['score'+k]:2},{name:'c',['score'+k]:1}]], [[{name:'x',['score'+k]:c}]], [[]]],r=>[...r].sort((a,b)=>b['score'+k]-a['score'+k]||a.name.localeCompare(b.name)))],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Sorting Key',key:'sortingKeys',track:'intermediate',name,en,fr,params,body,cases:testCases,calls:['sorted'],nodes:[{nodeType:'Lambda'}],focus:'the key tuple, ascending versus descending components, tie breakers, and stable ordering'});}

// Intermediate 5: String parsing.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1,sep=separators[k];const defs=[
 [`parse_fields_${k}`,`trim fields separated by ${py(sep)}`,`nettoie les champs séparés par ${py(sep)}`,'text',`return [field.strip() for field in text.split(${py(sep)})]`,cases([[` a ${sep} b ${sep}c `],[`one${sep}two`],['plain']],t=>t.split(sep).map(x=>x.trim()))],
 [`parse_pairs_${k}`,`parse ${py(sep)}-separated key=value fields into a dictionary`,`analyse des champs clé=valeur séparés par ${py(sep)}`,'text',`return {key.strip(): value.strip() for key, value in (field.split("=", 1) for field in text.split(${py(sep)}))}`,cases([[`a=1${sep}b=2`],[`name=Ada`],[`x=5${sep}y=6`]],t=>Object.fromEntries(t.split(sep).map(f=>f.split('=').map(x=>x.trim()))))],
 [`parse_integer_fields_${k}`,`parse integers separated by ${py(sep)} and add ${c} to each`,`analyse les entiers séparés par ${py(sep)} et ajoute ${c}`,'text',`return [int(field.strip()) + ${c} for field in text.split(${py(sep)})]`,cases([[`1${sep}2${sep}3`],[`4${sep}0`],['5']],t=>t.split(sep).map(x=>parseInt(x.trim(),10)+c))],
 [`parse_words_length_${c}`,`return words with at least ${c} characters`,`retourne les mots d’au moins ${c} caractères`,'text',`return [word for word in text.split() if len(word) >= ${c}]`,cases([['one three Python'],['a bb ccc'],['']],t=>(t.trim()?t.trim().split(/\s+/):[]).filter(x=>x.length>=c))],
 [`parse_extension_${k}`,`return the lowercase extension after the last dot, variant ${c}`,`retourne l’extension en minuscules après le dernier point, variante ${c}`,'filename',`return filename.rsplit(".", 1)[-1].lower() if "." in filename else ""`,cases([['photo.JPG'],['archive.tar.gz'],['README']],f=>f.includes('.')?f.split('.').at(-1).toLowerCase():'')],
 [`parse_path_${c}`,`return non-empty path parts and skip the first ${k} part(s)`,`retourne les parties non vides du chemin et saute ${k} partie(s)`,'path_text',`return [part for part in path_text.split("/") if part][${k}:]`,cases([['/a/b/c/d/e/f/g/h/i/j/k'],['one/two/three/four/five/six/seven/eight/nine/ten'],['/']],t=>t.split('/').filter(Boolean).slice(k))],
 [`parse_tag_${k}`,`extract text between <tag${k}> and </tag${k}>`,`extrait le texte entre <tag${k}> et </tag${k}>`,'text',`start = text.find(${py(`<tag${k}>`)})\n    end = text.find(${py(`</tag${k}>`)})\n    return text[start + ${5+String(k).length}:end] if start != -1 and end != -1 else ""`,cases([[`x<tag${k}>value</tag${k}>y`],['plain'],[`<tag${k}>code</tag${k}>`]],t=>{const a=`<tag${k}>`,b=`</tag${k}>`,s=t.indexOf(a),e=t.indexOf(b);return s>=0&&e>=0?t.slice(s+a.length,e):'';})],
 [`parse_coordinates_${c}`,`parse x,y coordinates and add ${c} to both`,`analyse des coordonnées x,y et ajoute ${c} aux deux`,'text',`x, y = text.split(",", 1)\n    return int(x.strip()) + ${c}, int(y.strip()) + ${c}`,cases([['1,2'],['-1, 5'],['0,0']],t=>t.split(',').map(x=>parseInt(x.trim(),10)+c))],
 [`parse_header_${k}`,`parse a ${py(':')}-separated header and lowercase its name, variant ${c}`,`analyse un en-tête séparé par deux-points et met son nom en minuscules, variante ${c}`,'text',`name, value = text.split(":", 1)\n    return name.strip().lower(), value.strip()`,cases([['Content-Type: text/plain'],['X-Test: 5'],['Name:Ada']],t=>{const p=t.indexOf(':');return [t.slice(0,p).trim().toLowerCase(),t.slice(p+1).trim()];})],
 [`parse_sentences_${c}`,`split dot-separated sentences and keep those with at least ${c} words`,`sépare les phrases par point et conserve celles d’au moins ${c} mots`,'text',`return [sentence.strip() for sentence in text.split(".") if len(sentence.split()) >= ${c}]`,cases([['one two. three four five. x.'],['a b c.'],['']],t=>t.split('.').map(x=>x.trim()).filter(x=>x.split(/\s+/).filter(Boolean).length>=c))],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'String Parsing',key:'stringParsing',track:'intermediate',name,en,fr,params,body,cases:testCases,focus:'separator boundaries, whitespace normalization, conversion order, and malformed or missing fields'});}

// Intermediate 6: Accumulation patterns.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`accumulate_sum_${c}`,`sum values after adding ${c} to each`,`additionne les valeurs après avoir ajouté ${c} à chacune`,'values',`total = 0\n    for value in values:\n        total += value + ${c}\n    return total`,cases([[[1,2,3]],[[-1,0]], [[]]],v=>v.reduce((a,x)=>a+x+c,0))],
 [`accumulate_product_${c}`,`multiply every value plus ${c}`,`multiplie chaque valeur plus ${c}`,'values',`product = 1\n    for value in values:\n        product *= value + ${c}\n    return product`,cases([[[1,2,3]],[[0,1]], [[]]],v=>v.reduce((a,x)=>a*(x+c),1))],
 [`accumulate_count_${c}`,`count values greater than ${c}`,`compte les valeurs supérieures à ${c}`,'values',`count = 0\n    for value in values:\n        if value > ${c}:\n            count += 1\n    return count`,cases([[[1,c,c+1,c+2]],[[c]], [[]]],v=>v.filter(x=>x>c).length)],
 [`accumulate_running_${c}`,`return running totals starting from ${c}`,`retourne les totaux cumulés à partir de ${c}`,'values',`total = ${c}\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result`,cases([[[1,2,3]],[[-1,1]], [[]]],v=>{let t=c;return v.map(x=>t+=x);})],
 [`accumulate_max_${c}`,`return the largest value after adding ${c}`,`retourne la plus grande valeur après avoir ajouté ${c}`,'values',`largest = None\n    for value in values:\n        adjusted = value + ${c}\n        if largest is None or adjusted > largest:\n            largest = adjusted\n    return largest`,cases([[[1,5,2]],[[-3,-1]], [[0]]],v=>Math.max(...v)+c)],
 [`accumulate_text_${c}`,`join words manually with separator ${py(separators[k])}`,`joint manuellement les mots avec ${py(separators[k])}`,'words',`result = ""\n    for word in words:\n        if result:\n            result += ${py(separators[k])}\n        result += word\n    return result`,cases([[['a','b','c']],[['one']], [[]]],w=>w.join(separators[k]))],
 [`accumulate_frequency_${c}`,`count values and add ${c} to each final frequency`,`compte les valeurs et ajoute ${c} à chaque fréquence finale`,'values',`counts = {}\n    for value in values:\n        counts[value] = counts.get(value, 0) + 1\n    return {key: count + ${c} for key, count in counts.items()}`,cases([[[1,1,2]],[['a','b','a']], [[]]],v=>{const o={};for(const x of v)o[x]=(o[x]||0)+1;return Object.fromEntries(Object.entries(o).map(([x,n])=>[x,n+c]));})],
 [`accumulate_weighted_${c}`,`sum each value multiplied by its one-based index plus ${c}`,`additionne chaque valeur multipliée par son indice plus ${c}`,'values',`total = 0\n    for index, value in enumerate(values, start=1):\n        total += value * index + ${c}\n    return total`,cases([[[1,2,3]],[[5]], [[]]],v=>v.reduce((a,x,i)=>a+x*(i+1)+c,0))],
 [`accumulate_groups_${c}`,`group numbers by remainder modulo ${c+1}`,`regroupe les nombres par reste modulo ${c+1}`,'values',`groups = {}\n    for value in values:\n        groups.setdefault(value % ${c+1}, []).append(value)\n    return groups`,cases([[[1,2,3,4]],[[0,-1,c]], [[]]],v=>{const o={};for(const x of v){const r=((x%(c+1))+(c+1))%(c+1);(o[r]??=[]).push(x);}return o;})],
 [`accumulate_difference_${c}`,`subtract each value from starting total ${c*10}`,`soustrait chaque valeur du total initial ${c*10}`,'values',`total = ${c*10}\n    for value in values:\n        total -= value\n    return total`,cases([[[1,2,3]],[[0]], [[]]],v=>v.reduce((a,x)=>a-x,c*10))],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Accumulation Pattern',key:'accumulationPatterns',track:'intermediate',name,en,fr,params,body,cases:testCases,nodes:[{nodeType:'For'}],focus:'the accumulator identity, update statement, loop order, and final return after iteration'});}

// Intermediate 7: Filtering and transformation.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`filter_add_${c}`,`keep numbers above ${c} and add ${c} to each`,`conserve les nombres supérieurs à ${c} et ajoute ${c}`,'values',`return [value + ${c} for value in values if value > ${c}]`,cases([[[1,c,c+1,c+2]],[[c]], [[]]],v=>v.filter(x=>x>c).map(x=>x+c))],
 [`filter_multiply_${c}`,`keep numbers divisible by ${c+1} and multiply them by ${c}`,`conserve les nombres divisibles par ${c+1} et les multiplie par ${c}`,'values',`return [value * ${c} for value in values if value % ${c+1} == 0]`,cases([[[0,c+1,2*(c+1),3]],[[c]], [[]]],v=>v.filter(x=>x%(c+1)===0).map(x=>x*c))],
 [`filter_words_${c}`,`keep words of at least ${c} characters and uppercase them`,`conserve les mots d’au moins ${c} caractères et les met en majuscules`,'words',`return [word.upper() for word in words if len(word) >= ${c}]`,cases([[['a','python','code']], [['x'.repeat(c)]], [[]]],w=>w.filter(x=>x.length>=c).map(x=>x.toUpperCase()))],
 [`filter_indexes_${c}`,`keep values at indexes divisible by ${c} and pair them with the index`,`conserve les valeurs aux indices divisibles par ${c} et les associe à l’indice`,'values',`return [(index, value) for index, value in enumerate(values) if index % ${c} == 0]`,cases([[[1,2,3,4,5]],[[9]], [[]]],v=>v.flatMap((x,i)=>i%c===0?[[i,x]]:[]))],
 [`filter_strings_${k}`,`keep strings containing ${py(targets[k])} and reverse them`,`conserve les chaînes contenant ${py(targets[k])} et les inverse`,'words',`return [word[::-1] for word in words if ${py(targets[k])} in word]`,cases([[[`a${targets[k]}b`,'plain',targets[k]]],[['none']], [[]]],w=>w.filter(x=>x.includes(targets[k])).map(x=>[...x].reverse().join('')))],
 [`filter_dict_${c}`,`keep dictionary items with values at least ${c} and double them`,`conserve les éléments du dictionnaire valant au moins ${c} et les double`,'mapping',`return {key: value * 2 for key, value in mapping.items() if value >= ${c}}`,cases([[{a:1,b:c,c:c+1}],[{x:0}], [{}]],m=>Object.fromEntries(Object.entries(m).filter(([,v])=>v>=c).map(([x,v])=>[x,v*2])))],
 [`filter_unique_${c}`,`keep first occurrences of values above ${c}`,`conserve les premières occurrences des valeurs supérieures à ${c}`,'values',`return list(dict.fromkeys(value for value in values if value > ${c}))`,cases([[[c+1,c+1,c+2,c]],[[c]], [[]]],v=>[...new Set(v.filter(x=>x>c))])],
 [`filter_pairs_${c}`,`keep pairs whose sum exceeds ${c} and return their products`,`conserve les paires dont la somme dépasse ${c} et retourne leurs produits`,'pairs',`return [left * right for left, right in pairs if left + right > ${c}]`,cases([[[[1,2],[c,c],[0,0]]], [[[c,1]]], [[]]],p=>p.filter(([a,b])=>a+b>c).map(([a,b])=>a*b))],
 [`filter_nested_${c}`,`keep non-empty rows and add ${c} to every nested value`,`conserve les lignes non vides et ajoute ${c} à chaque valeur`,'matrix',`return [[value + ${c} for value in row] for row in matrix if row]`,cases([[[[1,2],[],[3]]], [[[]]], [[]]],m=>m.filter(r=>r.length).map(r=>r.map(x=>x+c)))],
 [`filter_truthy_${c}`,`keep truthy values and convert each to text with suffix ${c}`,`conserve les valeurs vraies et les convertit en texte avec le suffixe ${c}`,'values',`return [str(value) + ${py(String(c))} for value in values if value]`,cases([[[0,1,'', 'x',null]], [[true]], [[]]],v=>v.filter(Boolean).map(x=>String(x===true?'True':x)+c))],
];const [name,en,fr,params,body,testCases]=defs[family];const nodeType=family===5?'DictComp':family===6?'GeneratorExp':'ListComp';add({concept:'Filtering & Transformation',key:'filteringTransformation',track:'intermediate',name,en,fr,params,body,cases:testCases,nodes:[{nodeType}],focus:'the filter condition, transformation expression, evaluation order, and output collection type'});}

// Intermediate 8: Early exit.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`first_above_${c}`,`return the first number above ${c}, stopping immediately`,`retourne le premier nombre supérieur à ${c} en s’arrêtant immédiatement`,'values',`for value in values:\n        if value > ${c}:\n            return value\n    return None`,cases([[[1,c,c+2,c+3]],[[c]], [[]]],v=>v.find(x=>x>c)??null),[{nodeType:'For'},{nodeType:'Return',minCount:2}]],
 [`first_divisible_${c}`,`return the first number divisible by ${c+1}`,`retourne le premier nombre divisible par ${c+1}`,'values',`for value in values:\n        if value % ${c+1} == 0:\n            return value\n    return None`,cases([[[1,c+1,2*(c+1)]],[[1]], [[]]],v=>v.find(x=>x%(c+1)===0)??null),[{nodeType:'For'}]],
 [`contains_word_${c}`,`stop and return True at the first word of length ${c}`,`s’arrête et retourne True au premier mot de longueur ${c}`,'words',`for word in words:\n        if len(word) == ${c}:\n            return True\n    return False`,cases([[['a','x'.repeat(c)]],[['no']], [[]]],w=>w.some(x=>x.length===c)),[{nodeType:'For'}]],
 [`sum_until_${c}`,`sum numbers until ${c} appears, excluding it`,`additionne les nombres jusqu’à ${c}, sans l’inclure`,'values',`total = 0\n    for value in values:\n        if value == ${c}:\n            break\n        total += value\n    return total`,cases([[[1,2,c,9]],[[c,5]], [[1,2]]],v=>{let t=0;for(const x of v){if(x===c)break;t+=x;}return t;}),[{nodeType:'Break'}]],
 [`collect_until_negative_${c}`,`collect values plus ${c} until a negative value appears`,`collecte les valeurs plus ${c} jusqu’à un nombre négatif`,'values',`result = []\n    for value in values:\n        if value < 0:\n            break\n        result.append(value + ${c})\n    return result`,cases([[[1,2,-1,3]], [[-1]], [[]]],v=>{const o=[];for(const x of v){if(x<0)break;o.push(x+c);}return o;}),[{nodeType:'Break'}]],
 [`skip_multiples_${c}`,`sum values while skipping multiples of ${c+1}`,`additionne les valeurs en sautant les multiples de ${c+1}`,'values',`total = 0\n    for value in values:\n        if value % ${c+1} == 0:\n            continue\n        total += value\n    return total`,cases([[[1,c+1,2]],[[0]], [[]]],v=>v.filter(x=>x%(c+1)!==0).reduce((a,b)=>a+b,0)),[{nodeType:'Continue'}]],
 [`find_key_${c}`,`return the first dictionary key whose value equals ${c}`,`retourne la première clé dont la valeur vaut ${c}`,'mapping',`for key, value in mapping.items():\n        if value == ${c}:\n            return key\n    return ""`,cases([[{a:1,b:c,c:c}],[{x:0}],[{}]],m=>Object.keys(m).find(x=>m[x]===c)||''),[{nodeType:'For'}]],
 [`validate_all_early_${c}`,`return False immediately when a number is below ${c}`,`retourne False immédiatement lorsqu’un nombre est inférieur à ${c}`,'values',`for value in values:\n        if value < ${c}:\n            return False\n    return True`,cases([[[c,c+1]],[[c-1,c]], [[]]],v=>v.every(x=>x>=c)),[{nodeType:'For'}]],
 [`index_above_${c}`,`return the first index whose value exceeds ${c}`,`retourne le premier indice dont la valeur dépasse ${c}`,'values',`for index, value in enumerate(values):\n        if value > ${c}:\n            return index\n    return -1`,cases([[[1,c,c+1]],[[c]], [[]]],v=>v.findIndex(x=>x>c)),[{nodeType:'For'}]],
 [`prefix_before_${k}`,`return text before the first ${py(targets[k])}, stopping at that character`,`retourne le texte avant le premier ${py(targets[k])}`,'text',`result = ""\n    for char in text:\n        if char == ${py(targets[k])}:\n            break\n        result += char\n    return result`,cases([[`abc${targets[k]}def`],[targets[k]+'x'],['plain']],t=>t.split(targets[k])[0]),[{nodeType:'Break'}]],
];const [name,en,fr,params,body,testCases,nodes]=defs[family];add({concept:'Early Exit',key:'earlyExit',track:'intermediate',name,en,fr,params,body,cases:testCases,nodes,focus:'the stopping condition, whether the matching value is included, and code that must not run afterward'});}

// Intermediate 9: Multiple return values.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1;const defs=[
 [`return_sum_product_${c}`,`return sum plus ${c} and product times ${c}`,`retourne la somme plus ${c} et le produit fois ${c}`,'left, right',`return left + right + ${c}, left * right * ${c}`,cases([[2,3],[-1,4],[0,5]],(a,b)=>[a+b+c,a*b*c])],
 [`return_min_max_${c}`,`return minimum minus ${c} and maximum plus ${c}`,`retourne le minimum moins ${c} et le maximum plus ${c}`,'values',`return min(values) - ${c}, max(values) + ${c}`,cases([[[1,5,2]],[[-3,-1]], [[c]]],v=>[Math.min(...v)-c,Math.max(...v)+c])],
 [`return_even_odd_${c}`,`return even and odd counts with ${c} added to each`,`retourne les comptes pairs et impairs avec ${c} ajouté`,'values',`even = sum(value % 2 == 0 for value in values)\n    odd = len(values) - even\n    return even + ${c}, odd + ${c}`,cases([[[1,2,3,4]],[[0]], [[]]],v=>[v.filter(x=>x%2===0).length+c,v.filter(x=>x%2!==0).length+c])],
 [`return_head_tail_${c}`,`return the first ${c} items and remaining items`,`retourne les ${c} premiers éléments et le reste`,'values',`return values[:${c}], values[${c}:]`,cases([[[1,2,3,4,5]],[[1]], [[]]],v=>[v.slice(0,c),v.slice(c)])],
 [`return_quotient_remainder_${c}`,`return quotient and remainder when dividing by ${c+1}`,`retourne quotient et reste lors de la division par ${c+1}`,'value',`return divmod(value, ${c+1})`,cases([[10],[0],[-5]],v=>[Math.floor(v/(c+1)),((v%(c+1))+(c+1))%(c+1)])],
 [`return_words_chars_${c}`,`return word count plus ${c} and character count`,`retourne le nombre de mots plus ${c} et le nombre de caractères`,'text',`return len(text.split()) + ${c}, len(text)`,cases([['one two'],[''],['Python code']],t=>[(t.trim()?t.trim().split(/\s+/).length:0)+c,t.length])],
 [`return_positive_negative_${c}`,`return positive and negative lists after offset ${c}`,`retourne les listes positives et négatives après décalage ${c}`,'values',`adjusted = [value + ${c} for value in values]\n    return [value for value in adjusted if value >= 0], [value for value in adjusted if value < 0]`,cases([[[-5,0,5]],[[-c]], [[]]],v=>{const a=v.map(x=>x+c);return [a.filter(x=>x>=0),a.filter(x=>x<0)];})],
 [`return_key_value_${k}`,`return whether ${py('k'+k)} exists and its value or ${c}`,`retourne si ${py('k'+k)} existe et sa valeur ou ${c}`,'mapping',`key = ${py('k'+k)}\n    return key in mapping, mapping.get(key, ${c})`,cases([[{['k'+k]:9}],[{x:1}],[{}]],m=>[Object.hasOwn(m,'k'+k),Object.hasOwn(m,'k'+k)?m['k'+k]:c])],
 [`return_mean_total_${c}`,`return total plus ${c} and average plus ${c}`,`retourne le total plus ${c} et la moyenne plus ${c}`,'values',`total = sum(values)\n    return total + ${c}, total / len(values) + ${c}`,cases([[[1,2,3]],[[5]], [[-1,1]]],v=>[v.reduce((a,b)=>a+b,0)+c,v.reduce((a,b)=>a+b,0)/v.length+c])],
 [`return_first_last_${c}`,`return first and last characters repeated ${c} time(s)`,`retourne les premier et dernier caractères répétés ${c} fois`,'text',`return text[0] * ${c}, text[-1] * ${c}`,cases([['python'],['a'],['code']],t=>[t[0].repeat(c),t.at(-1).repeat(c)])],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Multiple Return Value',key:'multipleReturns',track:'intermediate',name,en,fr,params,body,cases:testCases,nodes:family===4?undefined:[{nodeType:'Tuple'}],calls:family===4?['divmod']:undefined,focus:'tuple construction, the order and type of each returned component, and unpacking at the caller'});}

// Intermediate 10: Data cleaning.
for(let index=0;index<PACK_SIZE;index+=1){const family=Math.floor(index/10),k=index%10,c=k+1,target=targets[k];const defs=[
 [`clean_spaces_${c}`,`strip text and collapse whitespace, variant ${c}`,`nettoie le texte et réduit les espaces, variante ${c}`,'text','return " ".join(text.split())',cases([['  one   two  '],['\tPython\ncode '],['']],t=>t.trim()?t.trim().split(/\s+/).join(' '):'')],
 [`clean_case_${c}`,`strip and casefold text, variant ${c}`,`nettoie et normalise la casse, variante ${c}`,'text','return text.strip().casefold()',cases([['  Python  '],['HELLO'],['']],t=>t.trim().toLowerCase())],
 [`clean_remove_${k}`,`remove ${py(target)} after trimming text`,`supprime ${py(target)} après nettoyage du texte`,'text',`return text.strip().replace(${py(target)}, "")`,cases([[` ${target}hello${target} `],[' plain '],['']],t=>t.trim().split(target).join(''))],
 [`clean_words_${c}`,`trim, lowercase, and keep unique words with at least ${c} characters`,`nettoie, met en minuscules et conserve les mots uniques d’au moins ${c} caractères`,'text',`return list(dict.fromkeys(word.lower() for word in text.split() if len(word) >= ${c}))`,cases([[' Python python code CODE '],['a bb ccc'],['']],t=>[...new Set((t.trim()?t.trim().split(/\s+/):[]).filter(x=>x.length>=c).map(x=>x.toLowerCase()))])],
 [`clean_numbers_${c}`,`remove None values and clamp remaining numbers to at least ${c}`,`supprime None et limite les nombres restants à au moins ${c}`,'values',`return [max(value, ${c}) for value in values if value is not None]`,cases([[[null,1,10]],[[c-1,c]], [[]]],v=>v.filter(x=>x!==null).map(x=>Math.max(x,c)))],
 [`clean_strings_${c}`,`strip list strings and discard entries shorter than ${c}`,`nettoie les chaînes d’une liste et retire celles plus courtes que ${c}`,'values',`return [value.strip() for value in values if len(value.strip()) >= ${c}]`,cases([[[' a ',' python ','  ']], [['x'.repeat(c)]], [[]]],v=>v.map(x=>x.trim()).filter(x=>x.length>=c))],
 [`clean_mapping_${c}`,`strip dictionary keys and add ${c} to numeric values`,`nettoie les clés du dictionnaire et ajoute ${c} aux valeurs numériques`,'mapping',`return {str(key).strip(): value + ${c} for key, value in mapping.items()}`,cases([[{' a ':1,b:2}],[{'x ':0}],[{}]],m=>Object.fromEntries(Object.entries(m).map(([x,v])=>[x.trim(),v+c])))],
 [`clean_phone_${c}`,`keep only phone digits and append digit ${k}`,`conserve uniquement les chiffres du téléphone et ajoute le chiffre ${k}`,'text',`return "".join(char for char in text if char.isdigit()) + ${py(String(k))}`,cases([['+1 (555) 20-30'],['abc123'],['']],t=>t.replace(/\D/g,'')+k)],
 [`clean_delimited_${k}`,`split on ${py(separators[k])}, trim fields, and discard empty fields`,`sépare sur ${py(separators[k])}, nettoie et retire les champs vides`,'text',`return [field.strip() for field in text.split(${py(separators[k])}) if field.strip()]`,cases([[` a ${separators[k]} ${separators[k]} b `],['plain'],['']],t=>t.split(separators[k]).map(x=>x.trim()).filter(Boolean))],
 [`clean_duplicates_${c}`,`case-insensitively remove duplicate words and append marker ${c}`,`supprime les doublons de mots sans tenir compte de la casse et ajoute le marqueur ${c}`,'words',`seen = set()\n    result = []\n    for word in words:\n        normalized = word.strip().casefold()\n        if normalized and normalized not in seen:\n            seen.add(normalized)\n            result.append(normalized)\n    result.append(${py(String(c))})\n    return result`,cases([[[' A ','a','B']],[['x']], [[]]],w=>[...new Set(w.map(x=>x.trim().toLowerCase()).filter(Boolean)),String(c)])],
];const [name,en,fr,params,body,testCases]=defs[family];add({concept:'Data Cleaning',key:'dataCleaning',track:'intermediate',name,en,fr,params,body,cases:testCases,focus:'normalization order, discarded invalid data, duplicate handling, and the cleaned output type'});}

const expectedConcepts = {
  Indexing: 100, 'String Method': 100, 'List Method': 100, 'Dictionary Method': 100,
  'Print vs Return': 100, 'Function Argument': 100, 'Boolean Logic': 100, 'Input Parsing': 100,
  'Range Practice': 100, 'Basic Validation': 100, 'Enumerate & Zip': 100,
  'Searching & Counting': 100, 'Nested Collection': 100, 'Sorting Key': 100,
  'String Parsing': 100, 'Accumulation Pattern': 100, 'Filtering & Transformation': 100,
  'Early Exit': 100, 'Multiple Return Value': 100, 'Data Cleaning': 100,
};
if (specs.length !== 2000) throw new Error(`Expected 2000 specs, found ${specs.length}`);
for (const [concept,count] of Object.entries(expectedConcepts)) {
  const actual=specs.filter(spec=>spec.concept===concept).length;
  if(actual!==count) throw new Error(`${concept}: expected ${count}, found ${actual}`);
}

const labelsFr={Indexing:'indexation','String Method':'méthodes de chaîne','List Method':'méthodes de liste','Dictionary Method':'méthodes de dictionnaire','Print vs Return':'print et return','Function Argument':'arguments de fonction','Boolean Logic':'logique booléenne','Input Parsing':'analyse des entrées','Range Practice':'range','Basic Validation':'validation de base','Enumerate & Zip':'enumerate et zip','Searching & Counting':'recherche et comptage','Nested Collection':'collections imbriquées','Sorting Key':'clés de tri','String Parsing':'analyse de chaînes','Accumulation Pattern':'accumulation','Filtering & Transformation':'filtrage et transformation','Early Exit':'sortie anticipée','Multiple Return Value':'retours multiples','Data Cleaning':'nettoyage des données'};
const exercises=[];const graders={};const french={};
const invoke=(spec,test)=>`${spec.name}(${test.args.map(py).concat(Object.entries(test.kwargs||{}).map(([key,value])=>`${key}=${py(value)}`)).join(', ')})`;
specs.forEach((spec,index)=>{
  const id=START_ID+index;
  const level=levelFor(spec.track,index%PACK_SIZE);
  const canonical=`def ${spec.name}(${spec.params}):\n    ${spec.body}`;
  const nested=canonical.split('\n').slice(1).map(line=>`    ${line}`).join('\n');
  const classBody=canonical.split('\n').map(line=>`    ${line}`).join('\n');
  const solution=`# Example 1: canonical function approach\n${canonical}\n\nprint(${invoke(spec,spec.cases[0])})  # Expected: ${py(spec.cases[0].expected)}\n\n# Example 2: helper function approach\ndef solve_problem_${id}(${spec.params}):\n    def calculate():\n${nested}\n    return calculate()\n\nprint(${invoke({...spec,name:`solve_problem_${id}`},spec.cases[1])})\n\n# Example 3: static method approach\nclass Problem${id}Solution:\n    @staticmethod\n${classBody}\n\nprint(Problem${id}Solution.${invoke(spec,spec.cases[2])})\n\n# Example 4: assigned result approach\nresult = ${invoke(spec,spec.cases[0])}\nprint(result)\n\n# Example 5: direct call\nprint(${invoke(spec,spec.cases[1])})`;
  exercises.push({id,title:`Problem ${id}`,description:`Write a Python function called \`${spec.name}\` that must ${spec.en}. Practice ${spec.concept.toLowerCase()}.\nDifficulty: ${level}.\nExamples:\n  ${invoke(spec,spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec,spec.cases[1])} -> ${py(spec.cases[1].expected)}`,initialCode:`def ${spec.name}(${spec.params}):\n    pass`,solution,hint:`Focus on ${spec.focus}. Trace all three hidden input shapes instead of copying one example.`,breakdown:`1. Identify every parameter and its type.\n2. Apply the required ${spec.concept.toLowerCase()} structure.\n3. Trace intermediate values in order.\n4. Check empty, boundary, or missing-value behavior.\n5. Return the required value without hard-coding the examples.`,category:`${spec.concept} ${level}`});
  const grader={functionNames:[spec.name],tests:spec.cases};
  if(spec.calls) grader.requiredCallPatterns=spec.calls.map(functionName=>({functionName,minArgs:0}));
  if(spec.nodes) grader.requiredNodePatterns=spec.nodes;
  if(spec.boolOps?.length) grader.requiredBoolOps=spec.boolOps;
  graders[id]=grader;
  french[id]={description:`Écrivez une fonction Python appelée \`${spec.name}\` qui ${spec.fr}. Entraînez-vous avec ${labelsFr[spec.concept]}.\nDifficulté : ${level==='Easy'?'Facile':'Intermédiaire'}.\nExemples :\n  ${invoke(spec,spec.cases[0])} -> ${py(spec.cases[0].expected)}\n  ${invoke(spec,spec.cases[1])} -> ${py(spec.cases[1].expected)}`,hint:`Concentrez-vous sur ${labelsFr[spec.concept]}, l’ordre des opérations et la forme exacte du résultat. Testez aussi les limites.`,breakdown:`1. Identifiez chaque paramètre et son type.\n2. Utilisez la structure demandée de ${labelsFr[spec.concept]}.\n3. Suivez les valeurs intermédiaires dans l’ordre.\n4. Vérifiez les entrées vides, limites ou manquantes.\n5. Retournez le résultat sans coder les exemples en dur.`};
});

fs.writeFileSync(path.join(root,'foundationIntermediateExercises.ts'),`import type { Exercise } from './types';\n\nexport const FOUNDATION_INTERMEDIATE_EXERCISES: Exercise[] = ${JSON.stringify(exercises,null,2)};\n`);
fs.writeFileSync(path.join(root,'foundationIntermediateGraders.ts'),`import type { AutoGrader } from './graders';\n\nexport const FOUNDATION_INTERMEDIATE_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders,null,2)};\n`);
fs.writeFileSync(path.join(root,'services/foundationIntermediateFr.ts'),`export const FOUNDATION_INTERMEDIATE_FR: Record<number, { description: string; hint: string; breakdown: string }> = ${JSON.stringify(french,null,2)};\n`);
console.log(`Generated ${specs.length} foundation/intermediate exercises (${START_ID}-${START_ID+specs.length-1}).`);

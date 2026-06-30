const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');

function readNumberFlag(name) {
  const prefix = `--${name}=`;
  const inline = process.argv.find(arg => arg.startsWith(prefix));
  const flagIndex = process.argv.indexOf(`--${name}`);
  const rawValue = inline ? inline.slice(prefix.length) : flagIndex >= 0 ? process.argv[flagIndex + 1] : null;
  if (!rawValue || rawValue.startsWith('--')) return null;
  const value = Number(rawValue);
  if (!Number.isFinite(value)) {
    console.error(`Invalid --${name} value: ${rawValue}`);
    process.exit(1);
  }
  return value;
}

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2020,
      esModuleInterop: true,
    },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {},
    module: { exports: {} },
    require: () => ({}),
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

function isSimpleCase(testCase) {
  const specialKeys = [
    'inputValues', 'setupRemove', 'setupDirs', 'setupFiles', 'setupSymlinks',
    'permissionDeniedPaths', 'getFiles', 'randomValues', 'randomFloatValues',
    'randomChoiceValues', 'randomSampleValues', 'randomShuffleValues',
    'callReturnedWith', 'callMethod', 'callMethodArgs', 'callMethodArgExpressions',
    'getAttrs', 'setAttrs', 'deleteAttrs', 'setItems', 'deleteItems',
    'argExpressions', 'argFunctionNames', 'functionListArgNames',
    'expectedException', 'kwargs', 'functionName',
  ];
  return !specialKeys.some(key => {
    const value = testCase?.[key];
    if (Array.isArray(value)) return value.length > 0;
    if (value && typeof value === 'object') return Object.keys(value).length > 0;
    return Boolean(value);
  });
}

function metamorphicRule(functionNames, tests) {
  if (!Array.isArray(tests) || tests.length === 0 || !tests.every(isSimpleCase)) return null;
  const firstArgs = Array.isArray(tests[0]?.args) ? tests[0].args : [];
  const names = new Set(functionNames || []);
  const firstExpected = tests[0]?.expected;
  if (firstArgs.length === 2) {
    const [left, right] = firstArgs;
    if (['add_numbers', 'add_number', 'add_num'].some(name => names.has(name)) && [left, right].every(value => typeof value === 'number')) return 'add_numbers';
    if (names.has('merge_lists') && Array.isArray(left) && Array.isArray(right)) return 'merge_lists';
    if (names.has('is_anagram') && typeof left === 'string' && typeof right === 'string') return 'anagram';
    if (names.has('common_char') && typeof left === 'string' && typeof right === 'string') return 'common_chars';
    if (names.has('common_keys_max_values') && left && right && typeof left === 'object' && typeof right === 'object' && !Array.isArray(left) && !Array.isArray(right)) return 'common_keys_max_values';
    if (names.has('gcd') && [left, right].every(Number.isInteger)) return 'gcd';
    if (names.has('lcm') && [left, right].every(Number.isInteger)) return 'lcm';
    return null;
  }
  if (firstArgs.length === 3) {
    if (names.has('max_of_three') && firstArgs.every(value => typeof value === 'number')) return 'max_of_three';
    return null;
  }
  if (firstArgs.length !== 1) return null;
  const sample = firstArgs[0];
  if (['calculate_square', 'cal_square'].some(name => names.has(name)) && typeof sample === 'number') return 'square';
  if (names.has('is_even') && Number.isInteger(sample)) return 'even';
  if (names.has('is_odd') && Number.isInteger(sample)) return 'odd';
  if (names.has('reverse_string') && typeof sample === 'string') return 'reverse_string';
  if (names.has('reverse') && typeof sample === 'string') return 'reverse';
  if (['reverse_words', 'reverse_word'].some(name => names.has(name)) && typeof sample === 'string') return 'reverse_words';
  if (names.has('remove_vowels') && typeof sample === 'string') return 'remove_vowels';
  if (names.has('find_vowels') && typeof sample === 'string') return 'find_vowels';
  if (names.has('count_vowels') && typeof sample === 'string') {
    return firstExpected && typeof firstExpected === 'object' && !Array.isArray(firstExpected)
      ? 'count_vowels_dict'
      : 'count_vowels_number';
  }
  if (Array.isArray(sample)) {
    if (names.has('find_max')) return 'find_max';
    if (['find_min', 'find_minimum'].some(name => names.has(name))) return 'find_min';
    if (['calculate_sum', 'cal_sum', 'sum_of_list'].some(name => names.has(name))) return 'sum_list';
    if (names.has('find_min_max')) return 'find_min_max';
    if (['largest_smallest', 'smallest_largest', 'smallest_biggest'].some(name => names.has(name))) return 'largest_smallest_variant';
    if (['calculate_average', 'cal_average', 'find_average', 'find_average_lst'].some(name => names.has(name))) return 'average';
    if (['square_list', 'square_lst', 'square_elements'].some(name => names.has(name))) return 'square_list';
    if (['ascending_order_numbers', 'sort_list', 'sort_lst'].some(name => names.has(name))) return 'sort_ascending';
    if (names.has('big_small')) return 'sort_numeric_strings_desc';
    if (['reverse_list', 'reverse_lst'].some(name => names.has(name))) return 'reverse_list';
    if (['remove_duplicates', 'remove_duplicate'].some(name => names.has(name)) && ![...names].some(name => name.includes('case_insensitive'))) return 'remove_duplicates_list';
    if (names.has('has_duplicates')) return 'has_duplicates';
  }
  if (['remove_spaces', 'remove_space'].some(name => names.has(name)) && typeof sample === 'string') return 'remove_spaces';
  if (names.has('capitalize_words') && typeof sample === 'string') return 'capitalize_words';
  if (names.has('count_words') && typeof sample === 'string') {
    return firstExpected && typeof firstExpected === 'object' && !Array.isArray(firstExpected)
      ? 'count_words_dict'
      : 'count_words_number';
  }
  if (names.has('alphabetically_ordered') && typeof sample === 'string') return 'sort_words';
  if (names.has('correct') && typeof sample === 'string') return 'correct_spacing';
  if (['remove_duplicates', 'remove_duplicate'].some(name => names.has(name)) && typeof sample === 'string') {
    if (typeof firstExpected === 'string') return 'remove_duplicates_string';
    if (Array.isArray(firstExpected) && sample.includes(' ')) {
      const uniqueWords = [];
      for (const word of sample.split(/\s+/).filter(Boolean)) {
        if (!uniqueWords.includes(word)) uniqueWords.push(word);
      }
      return JSON.stringify(firstExpected) === JSON.stringify(uniqueWords) ? 'unique_words' : 'duplicate_words';
    }
    if (Array.isArray(firstExpected)) return 'unique_chars_list';
  }
  if (names.has('count_uppercase') && typeof sample === 'string') return 'count_uppercase';
  if (names.has('factorial') && Number.isInteger(sample)) return 'factorial';
  if (names.has('is_palindrome') && typeof sample === 'string') return 'palindrome';
  if (names.has('palindromes') && typeof sample === 'string') return 'palindrome';
  if (names.has('is_prime') && Number.isInteger(sample)) return 'prime';
  if (names.has('prime_factors') && Number.isInteger(sample)) return 'prime_factors';
  if (names.has('is_perfect_square') && !names.has('is_perfect_number') && Number.isInteger(sample)) return 'perfect_square';
  if (names.has('is_perfect_number') && Number.isInteger(sample)) return 'perfect_number';
  if (names.has('reverse_number') && Number.isInteger(sample)) return 'reverse_number';
  if (names.has('is_armstrong') && Number.isInteger(sample)) return 'armstrong';
  if (names.has('fibonacci') && Number.isInteger(sample) && Array.isArray(firstExpected)) return 'fibonacci';
  if (names.has('sum_even_indices') && Array.isArray(sample)) return 'sum_even_indices';
  if (names.has('all_odd_numbers') && Array.isArray(sample)) return 'sum_odd_numbers';
  if (names.has('is_even_index_sum') && Array.isArray(sample)) return 'even_index_sum_bool';
  if (['largest_element', 'max_in_list'].some(name => names.has(name)) && Array.isArray(sample)) return 'largest_element';
  if (names.has('max_value_key') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'max_value_key';
  if (names.has('merge_list_of_dicts') && Array.isArray(sample)) return 'merge_list_of_dicts';
  if (names.has('remove_duplicates_from_values') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'dedupe_dict_values';
  if (names.has('average_values') && Array.isArray(sample)) return 'average_dict_values';
  return null;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const exerciseById = new Map(EXERCISES.map(exercise => [exercise.id, exercise]));
const showAll = process.argv.includes('--all') || process.argv.includes('--show');
const maxUncoveredCommon = readNumberFlag('max-uncovered-common');
const minCovered = readNumberFlag('min-covered');

const functionGraders = [];
const covered = [];
const uncoveredCommon = [];
const ruleCounts = new Map();
const commonSignals = [
  'square', 'even', 'odd', 'reverse', 'vowel', 'max', 'min', 'sum',
  'space', 'capitalize', 'factorial', 'palindrome', 'duplicate', 'sort',
  'average', 'prime', 'fibonacci', 'gcd', 'lcm',
];

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  if (grader.mode === 'script') continue;
  const functionNames = Array.isArray(grader.functionNames) ? grader.functionNames : [];
  if (!functionNames.length) continue;
  functionGraders.push(id);
  const rule = metamorphicRule(functionNames, grader.tests);
  if (rule) {
    covered.push({ id, rule, functionNames });
    ruleCounts.set(rule, (ruleCounts.get(rule) || 0) + 1);
    continue;
  }
  const searchable = `${functionNames.join(' ')} ${exerciseById.get(id)?.title || ''} ${exerciseById.get(id)?.description || ''}`.toLowerCase();
  if (commonSignals.some(signal => searchable.includes(signal))) {
    uncoveredCommon.push({ id, functionNames, title: exerciseById.get(id)?.title || `Problem ${id}` });
  }
}

console.log('Metamorphic grader audit');
console.log(`Function graders: ${functionGraders.length}`);
console.log(`Covered by generated metamorphic tests: ${covered.length}`);
console.log(`Uncovered common-pattern function graders: ${uncoveredCommon.length}`);
console.log(`Rule distribution: ${[...ruleCounts.entries()].sort((a, b) => a[0].localeCompare(b[0])).map(([rule, total]) => `${rule}:${total}`).join(', ')}`);

if (showAll) {
  console.log(`Covered IDs: ${covered.map(item => `${item.id}:${item.rule}`).join(', ')}`);
  console.log(`Uncovered common-pattern IDs: ${uncoveredCommon.map(item => item.id).join(', ')}`);
  console.log('First uncovered common-pattern graders:');
  for (const item of uncoveredCommon.slice(0, 50)) {
    console.log(`${item.id}: ${item.title} [${item.functionNames.join(', ')}]`);
  }
}

const failures = [];
if (minCovered !== null && covered.length < minCovered) {
  failures.push(`covered metamorphic graders ${covered.length} below min ${minCovered}`);
}
if (maxUncoveredCommon !== null && uncoveredCommon.length > maxUncoveredCommon) {
  failures.push(`uncovered common-pattern graders ${uncoveredCommon.length} exceeds max ${maxUncoveredCommon}`);
}
if (failures.length) {
  console.error(`Metamorphic audit failed: ${failures.join('; ')}`);
  process.exit(1);
}

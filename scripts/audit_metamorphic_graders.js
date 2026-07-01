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

function isGeneratedInputCase(testCase) {
  if (!Array.isArray(testCase?.args) || testCase.args.length !== 0) return false;
  if (!Array.isArray(testCase?.inputValues) || testCase.inputValues.length === 0) return false;
  const specialKeys = [
    'setupRemove', 'setupDirs', 'setupFiles', 'setupSymlinks',
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

function inputGeneratedRule(functionNames, tests) {
  if (!Array.isArray(tests) || tests.length === 0 || !tests.every(isGeneratedInputCase)) return null;
  const names = new Set(functionNames || []);
  const firstExpected = tests[0]?.expected;
  const has = (...items) => items.some(name => names.has(name));
  if (has('area_rectangle')) return 'input_area_rectangle';
  if (has('even_odd')) return 'input_even_odd';
  if (has('fibonacci_series')) return 'input_fibonacci_series';
  if (has('max_number', 'max_of_three', 'max_of_list')) return 'input_maximum';
  if (has('is_palindrome')) return 'input_palindrome';
  if (has('count_vowels')) return 'input_count_vowels';
  if (has('factorial')) return 'input_factorial';
  if (has('sum_of_all_numbers')) return 'input_sum_numbers';
  if (has('is_leap_year')) return 'input_leap_year';
  if (has('length_string')) return 'input_length_string';
  if (has('are_anagrams', 'pal')) return 'input_anagram';
  if (has('decimal_to_binary')) return 'input_decimal_to_binary';
  if (has('square_root')) return 'input_square_root';
  if (has('digits_string', 'sum_digits')) return 'input_digit_sum';
  if (has('sum_of_odd_numbers', 'sum_of_all_odd', 'sum_of_odd')) return 'input_odd_sum';
  if (has('remove_duplicates', 'remove_duplicate') && Array.isArray(firstExpected)) return 'input_unique_characters';
  if (has('int_str')) return 'input_split_strings';
  if (has('type_smallest_biggest', 'small_big')) return 'input_sort_numbers';
  if (has('common', 'intersection')) return 'input_intersection';
  if (has('find_last_element', 'find_second_last_element')) return 'input_second_last';
  if (has('third_largest')) return 'input_third_largest';
  if (has('find_min', 'find_min_num')) return 'input_minimum';
  if (has('largest_element')) return 'input_longest_word';
  if (has('second_largest_element')) return 'input_second_longest_word';
  if (has('centimeters_inches')) return 'input_cm_to_inches';
  if (has('find_min_max')) return 'input_min_max';
  if (has('remove_vowels')) return 'input_remove_vowels';
  if (has('group_by_first_letter')) return 'input_group_by_first_letter';
  if (has('second_largest_number')) return 'input_second_largest_number';
  if (has('greet')) return 'input_greet';
  if (has('count_occurrences')) return 'input_count_occurrences';
  return null;
}

function metamorphicRule(functionNames, tests) {
  const inputRule = inputGeneratedRule(functionNames, tests);
  if (inputRule) return inputRule;
  if (!Array.isArray(tests) || tests.length === 0 || !tests.every(isSimpleCase)) return null;
  const firstArgs = Array.isArray(tests[0]?.args) ? tests[0].args : [];
  const names = new Set(functionNames || []);
  const firstExpected = tests[0]?.expected;
  if (firstArgs.length === 2) {
    const [left, right] = firstArgs;
    if (['add_numbers', 'add_number', 'add_num'].some(name => names.has(name)) && [left, right].every(value => typeof value === 'number')) return 'add_numbers';
    if (names.has('merge_lists') && Array.isArray(left) && Array.isArray(right)) return 'merge_lists';
    if (names.has('sum_of_2_lst') && Array.isArray(left) && Array.isArray(right)) return 'sum_two_lists';
    if (['maxium_element_wise', 'maximum_element_wise'].some(name => names.has(name)) && Array.isArray(left) && Array.isArray(right)) return 'elementwise_max';
    if (names.has('euclidean_distance') && Array.isArray(left) && Array.isArray(right)) return 'euclidean_distance';
    if (names.has('is_anagram') && typeof left === 'string' && typeof right === 'string') return 'anagram';
    if (names.has('common_char') && typeof left === 'string' && typeof right === 'string') return 'common_chars';
    if (names.has('common_keys_max_values') && left && right && typeof left === 'object' && typeof right === 'object' && !Array.isArray(left) && !Array.isArray(right)) return 'common_keys_max_values';
    if (names.has('gcd') && [left, right].every(Number.isInteger)) return 'gcd';
    if (names.has('calculate_gcd') && [left, right].every(Number.isInteger)) return 'gcd';
    if (names.has('lcm') && [left, right].every(Number.isInteger)) return 'lcm';
    if (names.has('sum_of_squares') && [left, right].every(value => typeof value === 'number')) return 'sum_of_squares';
    if (names.has('sum_of_primes') && [left, right].every(Number.isInteger)) return 'sum_of_primes';
    if (['calculate_sum', 'sum_of_two'].some(name => names.has(name)) && [left, right].every(value => typeof value === 'number')) return 'add_numbers_nested';
    if (names.has('sort_dicts_by_key') && Array.isArray(left) && typeof right === 'string') return 'sort_dicts_by_key';
    if (names.has('length_of_value') && Array.isArray(left) && typeof right === 'string') return 'sort_dicts_by_value_length';
    if (names.has('find_person') && Array.isArray(left) && typeof right === 'string') return 'max_dict_value_length';
    if (names.has('longest_string_letter') && Array.isArray(left) && typeof right === 'string') return 'longest_string_ending_letter';
    if (names.has('count_floating_numbers') && Array.isArray(left)) return 'count_value';
    if (names.has('calculate_integers') && [left, right].every(value => typeof value === 'number')) return 'product_sum_division';
    if (names.has('calculate_percentage') && Array.isArray(left) && typeof right === 'number') return 'percentages';
    if (names.has('example_function') && [left, right].every(value => typeof value === 'number')) return 'sum_sentence';
    if (names.has('format_calculation') && [left, right].every(value => typeof value === 'number')) return 'format_sum_sentence';
    if (names.has('calculate_sum_range') && [left, right].every(Number.isInteger)) return 'sum_inclusive_range';
    if (names.has('get_even_range') && [left, right].every(Number.isInteger)) return 'even_range';
    if (names.has('get_odd_range') && [left, right].every(Number.isInteger)) return 'odd_range';
    if (names.has('add_lists') && Array.isArray(left) && Array.isArray(right)) return 'add_lists';
    if (names.has('filter_by_length') && Array.isArray(left) && Number.isInteger(right)) return 'filter_by_min_length';
    if (names.has('calculate_lcm') && [left, right].every(Number.isInteger)) return 'calculate_lcm';
    if (names.has('calculate_weighted_average') && Array.isArray(left) && Array.isArray(right)) return 'weighted_average';
    if (names.has('get_pairs_summing_to') && Array.isArray(left) && typeof right === 'number') return 'pairs_summing_to';
    if (names.has('get_words_with_vowel_count') && typeof left === 'string' && Number.isInteger(right)) return 'words_with_vowel_count';
    if (names.has('main') && Array.isArray(left) && Number.isInteger(right)) return 'sort_by_remainder';
    return null;
  }
  if (firstArgs.length === 3) {
    if (names.has('max_of_three') && firstArgs.every(value => typeof value === 'number')) return 'max_of_three';
    if (names.has('get_maximum') && firstArgs.every(value => typeof value === 'number')) return 'max_of_three';
    if (names.has('find_minimum') && firstArgs.every(value => typeof value === 'number')) return 'min_of_three';
    if (names.has('get_minimum') && firstArgs.every(value => typeof value === 'number')) return 'min_of_three';
    if (names.has('get_words_by_length_range') && typeof firstArgs[0] === 'string' && firstArgs.slice(1).every(Number.isInteger)) return 'words_by_length_range';
    if (names.has('check_in_range') && firstArgs.every(value => typeof value === 'number')) return 'in_range';
    if (names.has('format_time') && firstArgs.every(Number.isInteger)) return 'format_time';
    if (names.has('calculate_age') && firstArgs.every(Number.isInteger)) return 'calculate_age';
    if (names.has('get_numbers_in_range') && Array.isArray(firstArgs[0]) && firstArgs.slice(1).every(value => typeof value === 'number')) return 'numbers_in_range';
    if (names.has('get_strings_with_length_range') && Array.isArray(firstArgs[0]) && firstArgs.slice(1).every(Number.isInteger)) return 'strings_length_range';
    if (names.has('get_sublist_sum') && Array.isArray(firstArgs[0]) && firstArgs.slice(1).every(Number.isInteger)) return 'sublist_sum';
    if (names.has('get_numbers_summing_to_range') && Array.isArray(firstArgs[0]) && firstArgs.slice(1).every(value => typeof value === 'number')) return 'pairs_sum_range';
    if (names.has('get_elements_by_frequency_range') && Array.isArray(firstArgs[0]) && firstArgs.slice(1).every(Number.isInteger)) return 'elements_by_frequency_range';
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
    if (names.has('l_s')) return 'largest_smallest_reversed';
    if (['largest_smallest', 'smallest_largest', 'smallest_biggest'].some(name => names.has(name))) return 'largest_smallest_variant';
    if (names.has('seconded_largest_number')) return 'second_largest';
    if (names.has('fourth_largest_number')) return 'fourth_largest';
    if (names.has('smallest_and_third')) return 'smallest_and_third';
    if (['calculate_average', 'cal_average', 'find_average', 'find_average_lst'].some(name => names.has(name))) return 'average';
    if (names.has('average')) return 'average';
    if (['square_list', 'square_lst', 'square_elements'].some(name => names.has(name))) return 'square_list';
    if (names.has('square_numbers')) return 'square_numbers';
    if (names.has('square_roots')) return 'square_roots';
    if (['ascending_order_numbers', 'sort_list', 'sort_lst'].some(name => names.has(name))) return 'sort_ascending';
    if (names.has('big_small')) return 'sort_numeric_strings_desc';
    if (['reverse_list', 'reverse_lst'].some(name => names.has(name))) return 'reverse_list';
    if (names.has('reverse_strings')) return 'reverse_strings';
    if (names.has('strip_whitespace')) return 'strip_whitespace';
    if (names.has('number_and_square')) return 'number_and_square';
    if (['remove_duplicates', 'remove_duplicate'].some(name => names.has(name)) && [...names].some(name => name.includes('case_insensitive'))) return 'remove_duplicates_case_insensitive';
    if (['remove_duplicates', 'remove_duplicate'].some(name => names.has(name)) && ![...names].some(name => name.includes('case_insensitive'))) return 'remove_duplicates_list';
    if (names.has('has_duplicates')) return 'has_duplicates';
    if (names.has('filter_even_numbers')) return 'filter_even_numbers';
    if (names.has('filter_odd_numbers')) {
      return Array.isArray(firstExpected) && firstExpected.every(value => Number.isInteger(value) && value % 2 !== 0)
        ? 'keep_odd_numbers'
        : 'filter_odd_numbers';
    }
    if (names.has('filter_palindromes')) return 'filter_palindromes';
    if (names.has('filter_prime')) return 'filter_prime';
    if (names.has('sum_odd_indexed_elements')) return 'sum_odd_indexed_elements';
    if (names.has('sort_tuples_by_second')) return 'sort_tuples_by_second';
    if (names.has('lst_of_tuples') && Array.isArray(firstExpected) && firstExpected.every(value => Array.isArray(value))) return 'sort_tuples_by_abs_first';
    if (names.has('earliest_date')) return 'earliest_date';
    if (names.has('sort_dates')) return 'sort_dates';
    if (names.has('sort_strings_alphabetically')) return 'sort_strings_alphabetically';
    if (names.has('lst_tuples') && Array.isArray(firstExpected)) return 'sort_tuples_lexicographic';
    if (names.has('lst_of_numbers') && Array.isArray(firstExpected)) return 'sort_by_frequency';
    if (names.has('lst_names')) return 'sort_strings_by_length';
    if (names.has('temperture')) return 'sort_ascending';
    if (names.has('last_letter')) return 'sort_strings_by_last_character';
    if (names.has('sort_by_hire_date')) return 'sort_by_second_value';
    if (names.has('lst_of_sentences')) return 'sort_strings_by_length';
    if (names.has('frequency_first_letter')) return 'sort_by_first_letter_frequency';
    if (names.has('reverse_order')) return 'reverse_alphabetical';
    if (names.has('sort_scores')) return 'sort_ascending';
    if (names.has('sort_emails')) return 'sort_emails_by_domain';
    if (['sort_cities_by_population', 'sort_students_by_grades', 'sort_books_by_year'].some(name => names.has(name))) return 'sort_by_second_value';
    if (names.has('sort_movies_by_release_date')) return 'sort_dicts_by_release_date';
    if (names.has('sort_sentences_by_unique_words')) return 'sort_by_unique_word_count';
    if (names.has('lst_words') && Array.isArray(firstExpected) && JSON.stringify(firstExpected) === JSON.stringify(sample.map(value => String(value).split('').reverse().join('')))) return 'reverse_strings';
    if (names.has('lst_integers') && Array.isArray(firstExpected) && firstExpected.every(value => value === 'Even' || value === 'Odd')) return 'even_odd_labels';
    if (names.has('negate_booleans')) return 'negate_booleans';
    if (names.has('lst_sentence') && Array.isArray(firstExpected) && firstExpected.every(value => typeof value === 'string')) {
      return firstExpected.some(value => String(value).includes(' ')) ? null : sample.some(value => String(value).includes(' '))
        ? 'remove_spaces_list'
        : 'capitalize_words_list';
    }
    if (names.has('factorial_lst')) return 'factorial_list';
    if (names.has('reverse_words_in_sentences')) return 'reverse_each_word_in_sentences';
    if (names.has('square_floats')) return 'square_list';
    if (names.has('lst_squares_and_cubes')) return 'squares_and_cubes';
    if (names.has('calculate_square_roots')) return 'square_roots';
  }
  if (['remove_spaces', 'remove_space'].some(name => names.has(name)) && typeof sample === 'string') return 'remove_spaces';
  if (names.has('vowels_consonates') && typeof sample === 'string') return 'vowel_consonant_counts';
  if (names.has('get_surname') && typeof sample === 'string') return 'surname';
  if (names.has('capitalize_words') && typeof sample === 'string') return 'capitalize_words';
  if (names.has('capitalize_words') && Array.isArray(sample)) return 'capitalize_words_list';
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
  if (names.has('factorial_while') && Number.isInteger(sample)) return 'factorial';
  if (names.has('factorial_recursive') && Number.isInteger(sample)) return 'factorial';
  if (names.has('is_palindrome') && typeof sample === 'string') return 'palindrome';
  if (names.has('is_palindrome') && Number.isInteger(sample)) return 'palindrome_number';
  if (names.has('palindromes') && typeof sample === 'string') return 'palindrome';
  if (names.has('is_prime') && Number.isInteger(sample)) return 'prime';
  if (names.has('prime_factors') && Number.isInteger(sample)) return 'prime_factors';
  if (names.has('is_perfect_square') && !names.has('is_perfect_number') && Number.isInteger(sample)) return 'perfect_square';
  if (names.has('is_perfect_number') && Number.isInteger(sample)) return 'perfect_number';
  if (names.has('reverse_number') && Number.isInteger(sample)) return 'reverse_number';
  if (names.has('sum_of_digits') && Number.isInteger(sample)) return 'sum_digits';
  if (names.has('is_armstrong') && Number.isInteger(sample)) return 'armstrong';
  if (names.has('fibonacci') && Number.isInteger(sample) && Array.isArray(firstExpected)) return 'fibonacci';
  if (names.has('get_fibonacci_sequence') && Number.isInteger(sample)) return 'fibonacci';
  if (names.has('fibonacci') && Number.isInteger(sample) && typeof firstExpected === 'number') return 'fibonacci_nth';
  if (names.has('fibonacci_sequence') && Number.isInteger(sample)) return 'fibonacci_sequence_printed';
  if (names.has('sum_n') && Number.isInteger(sample)) return 'sum_to_n';
  if (names.has('print_reverse') && Number.isInteger(sample)) return 'print_reverse_numbers';
  if (names.has('square_generator') && Number.isInteger(sample)) return 'generator_squares_zero_based';
  if (names.has('fibonacci_generator') && Number.isInteger(sample)) return 'generator_fibonacci_up_to_n';
  if (names.has('even_number_generator') && Number.isInteger(sample)) return 'generator_even_numbers';
  if (names.has('square_even_generator') && Number.isInteger(sample)) return 'generator_even_squares';
  if (names.has('prime_generator') && Number.isInteger(sample)) return 'generator_first_primes';
  if (names.has('factorial_generator') && Number.isInteger(sample)) return 'generator_factorials';
  if (names.has('square_number_generator') && Number.isInteger(sample)) return 'generator_squares_one_based';
  if (names.has('even_fibonacci_generator') && Number.isInteger(sample)) return 'generator_even_fibonacci';
  if (names.has('check_even_odd') && Number.isInteger(sample)) return 'even_odd_word';
  if (names.has('get_season') && Number.isInteger(sample)) return 'season_from_month';
  if (names.has('check_all_conditions') && Number.isInteger(sample)) return 'positive_even_divisible_by_3';
  if (names.has('check_palindrome_number') && Number.isInteger(sample)) return 'palindrome_number';
  if (names.has('check_perfect_square') && Number.isInteger(sample)) return 'perfect_square';
  if (names.has('prime_numbers_up_to_n') && Number.isInteger(sample)) return 'primes_up_to_n';
  if (names.has('even_and_greater_than_10') && Number.isInteger(sample)) return 'even_and_gt_10';
  if (names.has('is_perfect_square_and_armstrong') && Number.isInteger(sample)) return 'perfect_square_and_armstrong';
  if (names.has('sum_even_indices') && Array.isArray(sample)) return 'sum_even_indices';
  if (names.has('all_odd_numbers') && Array.isArray(sample)) return 'sum_odd_numbers';
  if (names.has('is_even_index_sum') && Array.isArray(sample)) return 'even_index_sum_bool';
  if (['largest_element', 'max_in_list'].some(name => names.has(name)) && Array.isArray(sample)) return 'largest_element';
  if (['max_of_three', 'max_of_list'].some(name => names.has(name)) && Array.isArray(sample)) return 'max_list';
  if (names.has('sum_elements') && Array.isArray(sample)) return 'sum_elements';
  if (names.has('list_sum') && Array.isArray(sample)) return 'list_sum';
  if (names.has('find_longest_word') && Array.isArray(sample)) return typeof firstExpected === 'number' ? 'longest_word_length' : 'longest_word';
  if (names.has('longest_word') && Array.isArray(sample)) return 'longest_word';
  if (names.has('longest_string') && Array.isArray(sample)) return 'longest_word';
  if (names.has('min_len') && Array.isArray(sample)) return 'shortest_word';
  if (names.has('find_max_and_index') && Array.isArray(sample)) return 'max_and_index';
  if (names.has('max_value_key') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'max_value_key';
  if (names.has('max_key') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'max_key_numeric_string';
  if (names.has('key_max') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'max_key_lexicographic';
  if (names.has('reverse_keys') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'reverse_keys';
  if (['palindromic_keys', 'palindrome_keys'].some(name => names.has(name)) && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'palindromic_keys';
  if (names.has('merge_list_of_dicts') && Array.isArray(sample)) return 'merge_list_of_dicts';
  if (names.has('remove_duplicates_from_values') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'dedupe_dict_values';
  if (names.has('average_values') && Array.isArray(sample)) return 'average_dict_values';
  if (names.has('average_values') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'average_dict_numeric_values';
  if (names.has('average_of_list') && Array.isArray(sample)) return 'average';
  if (names.has('total') && Array.isArray(sample)) return 'sum_and_product';
  if (names.has('check_even') && Number.isInteger(sample)) return 'even';
  if (names.has('even_or_odd') && Number.isInteger(sample)) return typeof firstExpected === 'string' && String(sample) && firstExpected.includes(String(sample)) ? 'even_odd_sentence' : 'even_odd_word';
  if (names.has('check_prime') && Number.isInteger(sample)) return 'prime';
  if (names.has('calculate_factorial') && Number.isInteger(sample)) return 'factorial';
  if (names.has('check_palindrome') && typeof sample === 'string') return 'palindrome';
  if (['is_sorted', 'check_sorted'].some(name => names.has(name)) && Array.isArray(sample)) return 'is_sorted';
  if (names.has('min_max') && Array.isArray(sample)) return 'find_min_max';
  if (names.has('generate_squares') && Number.isInteger(sample)) return 'generate_squares';
  if (names.has('calculate_square_root') && typeof sample === 'number') return 'square_root';
  if (names.has('perimeter_of_square') && typeof sample === 'number') return 'square_perimeter';
  if (names.has('calculate_perimeter_square') && typeof sample === 'number') return 'square_perimeter';
  if (names.has('square_of_number') && typeof sample === 'number') return 'square';
  if (names.has('closest_to_zero') && Array.isArray(sample)) return 'closest_to_zero';
  if (names.has('print_odd_index_elements') && Array.isArray(sample)) return 'print_odd_index_elements';
  if (names.has('index_element_if_vowel') && Array.isArray(sample)) return 'index_element_if_vowel';
  if (names.has('print_index_squared') && Array.isArray(sample)) return 'print_index_squared';
  if (names.has('replace_based_on_index') && Array.isArray(sample)) return 'replace_based_on_index';
  if (names.has('enumerate_lst') && Array.isArray(sample) && typeof firstExpected === 'string' && !firstExpected.toLowerCase().includes('index')) return 'enumerate_even_indices';
  if (['sort_strings_by_length', 'len_lst'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_strings_by_length';
  if (names.has('sort_list_descending') && Array.isArray(sample)) return 'sort_descending';
  if (names.has('sort_by_absolute_value') && Array.isArray(sample)) return 'sort_by_absolute_value';
  if (names.has('sort_complex_numbers') && Array.isArray(sample)) return 'sort_by_absolute_value';
  if (names.has('sort_fractions') && Array.isArray(sample)) return 'sort_numeric';
  if (['sort_tuples_by_sum', 'sum_of_tuple'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_tuples_by_sum';
  if (names.has('sort_points_by_distance') && Array.isArray(sample)) return 'sort_points_by_distance';
  if (names.has('sort_words_by_distinct_letters') && Array.isArray(sample)) return 'sort_words_by_distinct_letters';
  if (['sort_by_vowel_count', 'sort_words_by_vowel_count'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_by_vowel_count';
  if (['sort_strings_by_last_character', 'list_of_strings_lst'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_strings_by_last_character';
  if (names.has('sort_number_uppercases') && Array.isArray(sample)) return 'sort_by_uppercase_count';
  if (names.has('find_highest_ascii_word') && Array.isArray(sample)) return 'max_ascii_word';
  if (names.has('filter_string') && Array.isArray(sample)) return 'filter_len_three';
  if (names.has('max_string_alpha') && Array.isArray(sample)) return 'max_string_alpha';
  if (names.has('reverse') && Array.isArray(sample)) return 'reverse_list';
  if (names.has('reverse_order') && Array.isArray(sample)) return 'reverse_alphabetical';
  if (names.has('floating_point') && Array.isArray(sample)) return 'sort_float_ascending';
  if (names.has('first_element_decending_order') && Array.isArray(sample)) return 'sort_first_element_desc';
  if (names.has('number_of_consonants') && Array.isArray(sample)) return typeof firstExpected === 'string' ? 'min_consonants_word' : 'sort_by_consonants';
  if (names.has('min_string') && Array.isArray(sample)) return 'shortest_word';
  if (names.has('main') && Array.isArray(sample) && Array.isArray(firstExpected) && firstExpected.every(value => Number.isInteger(value))) return 'sort_by_remainder';
  if (names.has('sort_by_year') && Array.isArray(sample)) return 'sort_by_year';
  if (names.has('sort_by_a_count') && Array.isArray(sample)) return 'sort_by_a_count';
  if (names.has('sort_by_first_element_desc') && Array.isArray(sample)) return 'sort_first_element_desc';
  if (names.has('sort_by_length') && Array.isArray(sample)) return 'sort_strings_by_length';
  if (names.has('sort_by_multiple_criteria') && Array.isArray(sample)) return 'sort_by_multiple_criteria';
  if (names.has('calculate_statistics') && Array.isArray(sample)) return 'statistics_summary';
  if (names.has('sum_of_elements') && Array.isArray(sample)) return 'sum_list';
  if (names.has('sum_of_even') && Array.isArray(sample)) return 'sum_even_numbers';
  if (names.has('create_square_root_tuples') && Array.isArray(sample)) return 'square_root_tuples';
  if (names.has('average_of_odds') && Array.isArray(sample)) return 'average_odd_numbers';
  if (names.has('square_odd_numbers') && Array.isArray(sample)) return 'square_odd_numbers';
  if (names.has('sum_of_cubes') && Array.isArray(sample)) return 'sum_cubes';
  if (names.has('consecutive_pair_sum') && Array.isArray(sample)) return 'generator_consecutive_pair_sum';
  if (names.has('odd_filter_generator') && Array.isArray(sample)) return 'generator_even_filter';
  if (names.has('cumulative_sum_generator') && Array.isArray(sample)) return 'generator_cumulative_sum';
  if (names.has('reverse_list_generator') && Array.isArray(sample)) return 'generator_reverse_list';
  if (names.has('sum_with_index_generator') && Array.isArray(sample)) return 'generator_sum_with_index';
  if (names.has('palindrome_generator') && Array.isArray(sample)) return 'generator_palindromes';
  if (names.has('even_index_generator') && Array.isArray(sample)) return 'generator_even_index_elements';
  if (names.has('sum_numbers') && Array.isArray(sample)) return 'sum_list';
  if (names.has('calculate_sum_of_list') && Array.isArray(sample)) return 'sum_list';
  if (names.has('get_average_of_list') && Array.isArray(sample)) return 'average';
  if (names.has('get_middle_element') && Array.isArray(sample)) return 'middle_element';
  if (names.has('get_even_numbers') && Array.isArray(sample)) return 'keep_even_numbers';
  if (names.has('get_even_numbers_comprehension') && Array.isArray(sample)) return 'keep_even_numbers';
  if (names.has('get_odd_numbers') && Array.isArray(sample)) return 'keep_odd_numbers';
  if (names.has('get_squared_numbers') && Array.isArray(sample)) return 'square_list';
  if (names.has('remove_duplicates_from_list') && Array.isArray(sample)) return 'remove_duplicates_list';
  if (names.has('remove_duplicates_preserve_order') && Array.isArray(sample)) return 'remove_duplicates_list';
  if (names.has('sort_list_ascending') && Array.isArray(sample)) return 'sort_ascending';
  if (names.has('get_index_of_max') && Array.isArray(sample)) return 'index_of_max';
  if (names.has('get_index_of_min') && Array.isArray(sample)) return 'index_of_min';
  if (names.has('get_min_max') && Array.isArray(sample)) return 'find_min_max';
  if (names.has('filter_and_transform') && Array.isArray(sample)) return 'filter_even_double';
  if (names.has('find_duplicate_elements') && Array.isArray(sample)) return 'find_duplicates';
  if (names.has('get_even_indices') && Array.isArray(sample)) return 'even_index_elements';
  if (names.has('get_odd_indices') && Array.isArray(sample)) return 'odd_index_elements';
  if (['sort_sqaure', 'sqaure_numbers_lst'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_by_square';
  if (names.has('length_of_first_element') && Array.isArray(sample)) return 'sort_by_first_element_length';
  if (names.has('number_of_spaces') && Array.isArray(sample)) return 'sort_by_space_count';
  if (names.has('most_vowels') && Array.isArray(sample)) return 'max_vowels_word';
  if (names.has('sort_lst_integers') && Array.isArray(sample)) return 'sort_by_digit_count';
  if (names.has('sort_tuples_by_difference') && Array.isArray(sample)) return 'sort_tuples_by_difference';
  if (names.has('sort_strings_by_ascii') && Array.isArray(sample)) return 'sort_strings_by_ascii';
  if (names.has('sort_lists_by_sum') && Array.isArray(sample)) return 'sort_lists_by_sum';
  if (names.has('sort_files_by_extension') && Array.isArray(sample)) return 'sort_files_by_extension';
  if (names.has('sort_second_letter') && Array.isArray(sample)) return 'sort_second_letter';
  if (['people_age', 'sort_people_by_age'].some(name => names.has(name)) && Array.isArray(sample)) return 'sort_people_by_age';
  if (names.has('sort_by_binary_representation') && Array.isArray(sample)) return 'sort_by_binary_representation';
  if (names.has('sort_keys_by_value') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'sort_keys_by_value';
  if (['name_age', 'sports_by_popularity'].some(name => names.has(name)) && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'sort_keys_by_value';
  if (['sorted_students_grades', 'movies', 'sorted_movie_titles'].some(name => names.has(name)) && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'sort_keys_alphabetically';
  if (names.has('students_grades') && sample && typeof sample === 'object' && !Array.isArray(sample) && typeof firstExpected === 'string') return 'print_keys_alphabetically';
  if (names.has('colors_hex') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'reverse_keys';
  if (names.has('sort_dic') && sample && typeof sample === 'object' && !Array.isArray(sample)) {
    const sortedByKey = Object.fromEntries(Object.entries(sample).sort(([a], [b]) => a.localeCompare(b)));
    if (JSON.stringify(firstExpected) === JSON.stringify(sortedByKey)) return 'sort_dict_by_key';
    const sortedByValueDesc = Object.fromEntries(Object.entries(sample).sort((a, b) => b[1] - a[1]));
    if (JSON.stringify(firstExpected) === JSON.stringify(sortedByValueDesc)) return 'sort_dict_by_value_desc';
  }
  if (names.has('remove_duplicates_values') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'dedupe_dict_scalar_values';
  if (names.has('largest_value') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'key_of_largest_value';
  if (names.has('smallest_value') && sample && typeof sample === 'object' && !Array.isArray(sample)) return 'key_of_smallest_value';
  if (names.has('sort_fractions_by_decimal') && Array.isArray(sample)) return 'sort_numeric';
  if (names.has('count_spaces') && typeof sample === 'string') return 'count_spaces';
  if (names.has('even_length_word_generator') && typeof sample === 'string') return 'generator_even_length_words';
  if (names.has('fibonacci_up_to_n') && Number.isInteger(sample)) return 'fibonacci_up_to_n_printed';
  if (['square_pattern', 'print_square_pattern'].some(name => names.has(name)) && Number.isInteger(sample)) {
    const firstLine = String(firstExpected ?? '').split('\n')[0];
    return new Set(firstLine.replace(/\s/g, '').split('')).has('*') ? 'star_square_pattern' : 'number_square_pattern';
  }
  if (names.has('print_hollow_square') && Number.isInteger(sample)) return 'hollow_square_pattern';
  if (names.has('print_reverse_pyramid') && Number.isInteger(sample)) return 'reverse_number_pyramid';
  if (names.has('print_cross') && Number.isInteger(sample)) return 'cross_pattern';
  if (names.has('print_reverse_hill_pattern') && Number.isInteger(sample)) return 'reverse_hill_pattern';
  if (names.has('print_reverse_star_pattern') && Number.isInteger(sample)) return 'reverse_star_pattern';
  if (names.has('print_number_square') && Number.isInteger(sample)) return 'sequential_number_square';
  if (names.has('get_middle_char') && typeof sample === 'string') return 'middle_char';
  if (names.has('get_first_word') && typeof sample === 'string') return 'first_word';
  if (names.has('get_last_word') && typeof sample === 'string') return 'last_word';
  if (names.has('count_characters') && typeof sample === 'string' && typeof firstExpected === 'number') return 'count_non_space_chars';
  if (names.has('check_vowel') && typeof sample === 'string') return 'is_vowel';
  if (names.has('strip_whitespace') && typeof sample === 'string') return 'strip_whitespace_string';
  if (names.has('capitalize_first_letter') && typeof sample === 'string') return 'capitalize_first_letter';
  if (names.has('capitalize_all_words') && typeof sample === 'string') return 'capitalize_words';
  if (names.has('get_longest_word') && typeof sample === 'string') return 'longest_word_from_sentence';
  if (names.has('get_shortest_word') && typeof sample === 'string') return 'shortest_word_from_sentence';
  if (names.has('remove_vowels_from_string') && typeof sample === 'string') return 'remove_vowels';
  if (names.has('remove_consonants_from_string') && typeof sample === 'string') return 'remove_consonants';
  if (names.has('count_vowels_in_string') && typeof sample === 'string') return 'count_vowels_number';
  if (names.has('swap_first_last_words') && typeof sample === 'string') return 'swap_first_last_words';
  if (names.has('get_middle_word') && typeof sample === 'string') return 'middle_word';
  if (names.has('get_words_starting_with_vowel') && typeof sample === 'string') return 'words_starting_with_vowel';
  if (names.has('count_vowels_and_consonants') && typeof sample === 'string') return 'vowel_consonant_counts_tuple';
  if (names.has('check_palindrome_and_length') && typeof sample === 'string') return 'palindrome_and_length';
  if (names.has('filters_even_numbers') && Array.isArray(sample)) return 'keep_even_numbers';
  if (names.has('palindromes') && Array.isArray(sample)) return 'filter_palindromes';
  if (names.has('sum_of_lst') && Array.isArray(sample)) return firstExpected === sample.reduce((a, b) => a * b, 1) ? 'product_list' : 'sum_list';
  if (names.has('capitalize_string') && Array.isArray(sample)) return 'capitalize_words_list';
  if (names.has('number_lst') && Array.isArray(sample)) return 'find_min';
  if (names.has('lst_numbers') && Array.isArray(sample) && typeof firstExpected === 'number') return 'sum_squares';
  if (names.has('apply_lsts') && Array.isArray(sample)) return 'square_then_filter_odd';
  if (names.has('sum_nested_list') && Array.isArray(sample)) return 'sum_nested_list';
  if (names.has('fibonacci_n_numbers') && Number.isInteger(sample)) return 'fibonacci';
  if (names.has('lst_string') && Array.isArray(sample) && Array.isArray(firstExpected) && firstExpected.every(Number.isInteger)) return 'map_count_vowels';
  if (names.has('sum_even_numbers') && Array.isArray(sample)) return 'sum_even_numbers';
  if (names.has('get_sum_of_squares') && Array.isArray(sample)) return 'sum_squares';
  if (names.has('get_product_of_even') && Array.isArray(sample)) return 'product_even_numbers';
  if (names.has('get_sum_of_odd') && Array.isArray(sample)) return 'sum_odd_numbers';
  if (names.has('get_elements_greater_than_average') && Array.isArray(sample)) return 'elements_gt_average';
  if (names.has('get_elements_less_than_average') && Array.isArray(sample)) return 'elements_lt_average';
  if (names.has('calculate_median') && Array.isArray(sample)) return 'median';
  if (names.has('calculate_weighted_average') && Array.isArray(sample)) return 'weighted_average';
  if (names.has('get_strings_sorted_by_length') && Array.isArray(sample)) return 'sort_strings_by_length';
  if (names.has('get_pairs_summing_to') && Array.isArray(sample)) return 'pairs_summing_to';
  if (names.has('get_numbers_summing_to_range') && Array.isArray(sample)) return 'pairs_sum_range';
  if (names.has('get_frequency_dict') && Array.isArray(sample)) return 'frequency_dict';
  if (names.has('get_strings_with_all_vowels') && Array.isArray(sample)) return 'strings_with_all_vowels';
  if (names.has('get_elements_with_max_frequency') && Array.isArray(sample)) return 'elements_with_max_frequency';
  if (names.has('get_elements_by_frequency_range') && Array.isArray(sample)) return 'elements_by_frequency_range';
  if (names.has('calculate_statistical_summary') && Array.isArray(sample)) return 'statistical_summary';
  if (names.has('get_comprehensive_statistics') && Array.isArray(sample)) return 'comprehensive_statistics';
  if (names.has('lst_num') && Array.isArray(sample)) return 'cumulative_sum';
  if (names.has('filter_primes') && Array.isArray(sample)) return 'filter_prime';
  if (names.has('sort_string_len') && Array.isArray(sample)) return 'sort_strings_by_length';
  if (names.has('lst_tuples_second') && Array.isArray(sample)) return 'sort_tuples_by_second';
  if (names.has('sort_last_names') && Array.isArray(sample)) return 'sort_last_names';
  if (names.has('sort_ignore_case') && Array.isArray(sample)) return 'sort_ignore_case';
  if (names.has('list_floats') && Array.isArray(sample)) return 'sort_descending';
  if (names.has('lst_words') && Array.isArray(sample) && Array.isArray(firstExpected) && JSON.stringify(firstExpected) === JSON.stringify([...sample].sort((a, b) => {
    const countVowels = word => String(word).toLowerCase().split('').filter(char => 'aeiou'.includes(char)).length;
    return countVowels(a) - countVowels(b);
  }))) return 'sort_by_vowel_count';
  if (names.has('lst_integers') && Array.isArray(sample) && Array.isArray(firstExpected) && JSON.stringify(firstExpected) === JSON.stringify([...sample].sort((a, b) => {
    const digitSum = value => String(Math.abs(value)).split('').reduce((total, digit) => total + Number(digit), 0);
    return digitSum(a) - digitSum(b);
  }))) return 'sort_by_digit_sum';
  if (names.has('lst_products') && Array.isArray(sample)) return 'sort_products_by_price';
  if (names.has('count_vowels_per_word') && typeof sample === 'string') return 'vowels_per_word';
  if (names.has('get_words_with_vowel_count') && typeof sample === 'string') return 'words_with_vowel_count';
  if (names.has('count_character_types') && typeof sample === 'string') return 'character_type_counts';
  if (names.has('get_words_by_vowel_count') && typeof sample === 'string') return 'words_by_vowel_count';
  if (names.has('get_words_sorted_by_vowels') && typeof sample === 'string') return 'words_sorted_by_vowels';
  return null;
}

function namedMetamorphicRule(functionNames, tests) {
  if (!Array.isArray(tests) || tests.length === 0) return null;
  if (!tests.every(testCase => {
    if (!testCase?.functionName) return false;
    const copy = { ...testCase };
    delete copy.functionName;
    return isSimpleCase(copy);
  })) return null;
  const names = new Set(functionNames || []);
  const hasAll = (...items) => items.every(name => names.has(name));
  if (hasAll('sum_list', 'add')) return 'helper_sum_and_add';
  if (hasAll('sum', 'multiply')) return 'helper_sum_and_multiply';
  if (hasAll('max_func', 'max_in_list')) return 'helper_reduce_max';
  if (hasAll('is_even', 'filter_even_numbers')) return 'helper_even_filter';
  if (hasAll('word_list', 'capitalize_first_letter')) return 'helper_capitalize_words';
  if (hasAll('lst_numbers', 'find_max')) return 'helper_find_max';
  if (hasAll('string_lst', 'reverse_string')) return 'helper_reverse_strings';
  if (hasAll('lst_words', 'count_vowels')) return 'helper_max_vowels';
  if (hasAll('lst_of_word', 'is_palindrome')) return 'helper_filter_palindromes';
  if (hasAll('lst_numbers', 'sqaure_number')) return 'helper_square_numbers';
  if (hasAll('find_gcd', 'gcd_of_pairs')) return 'helper_gcd_pairs';
  if (hasAll('lst_words', 'sort_lst')) return 'helper_sort_lists';
  if (hasAll('lst_sites', 'remove_duplicates')) return 'helper_remove_duplicates';
  if (hasAll('filter_primes', 'is_prime')) return 'helper_filter_primes';
  if (hasAll('lst_of_numbers', 'calculate_factorial')) return 'helper_factorial_list';
  if (hasAll('sort_dict_by_value', 'get_value')) return 'helper_sort_dict_values';
  if (hasAll('main', 'generate_fibonacci')) return 'helper_fibonacci';
  if (hasAll('main', 'calculate_average')) return 'helper_average';
  if (hasAll('main', 'remove_whitespace')) return 'helper_remove_whitespace';
  if (hasAll('main', 'check_even_odd')) return 'helper_even_odd';
  if (hasAll('main', 'sum_of_list')) return 'helper_sum_list';
  if (hasAll('main', 'merge_sorted_lists')) return 'helper_merge_sorted';
  if (hasAll('main', 'get_even_numbers')) return 'helper_get_even_numbers';
  if (hasAll('main', 'sort_values', 'sort_key')) return 'helper_sort_values';
  if (hasAll('main', 'square_odd_number_generator')) return 'helper_square_odd_generator';
  return null;
}

function kwargsMetamorphicRule(functionNames, tests) {
  if (!Array.isArray(tests) || tests.length === 0 || !tests.every(testCase => {
    const kwargs = testCase?.kwargs;
    if (!kwargs || typeof kwargs !== 'object' || Array.isArray(kwargs)) return false;
    const copy = { ...testCase, kwargs: {} };
    return isSimpleCase(copy);
  })) return null;
  const names = new Set(functionNames || []);
  if (names.has('sum_kwargs')) return 'kwargs_sum_numeric';
  if (names.has('even_kwargs')) return 'kwargs_even_values';
  if (names.has('sorted_kwargs')) return 'kwargs_sorted_keys';
  if (names.has('reverse_kwargs')) return 'kwargs_reverse_dict';
  if (names.has('max_numeric')) return 'kwargs_max_numeric';
  if (names.has('even_or_odd_kwargs')) return 'kwargs_count_even_odd';
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
  const rule = metamorphicRule(functionNames, grader.tests) || namedMetamorphicRule(functionNames, grader.tests) || kwargsMetamorphicRule(functionNames, grader.tests);
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

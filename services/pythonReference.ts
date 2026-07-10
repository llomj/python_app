// ────────────────────────────────────────────────────────────────────────────
// Python Reference — comprehensive lookup for methods, builtins, keywords, concepts
// Used by the built-in Problem AI when WebLLM is not available
// ────────────────────────────────────────────────────────────────────────────

import { lookupConcept } from './pythonConceptLibrary';

interface RefEntry {
  name: string
  type: string        // 'str', 'list', 'dict', 'set', 'tuple', 'builtin', 'keyword', 'concept'
  signature: string
  desc: string
  example: string
}

// ── FLAT LOOKUP: methodName -> entry ───────────────────────────────────────
const _ref: Record<string, RefEntry[]> = {};

const _ = (name: string, type: string, signature: string, desc: string, example: string): void => {
  (_ref[name] ||= []).push({ name, type, signature, desc, example });
};

const allReferenceEntries = (): RefEntry[] => Object.values(_ref).flat();

// ── STRING METHODS ─────────────────────────────────────────────────────────
_('capitalize', 'str', 'str.capitalize()', 'Returns a copy with the first character upper-cased and the rest lower-cased.', `"hello world".capitalize()  # "Hello world"`);
_('casefold', 'str', 'str.casefold()', 'Returns a case-folded copy for caseless matching (more aggressive than lower()).', `"Straße".casefold()  # "strasse"`);
_('center', 'str', 'str.center(width[, fillchar])', 'Returns the string centered in a string of length width, padded with fillchar.', `"hi".center(7, '-')  # "--hi---"`);
_('count', 'str', 'str.count(sub[, start[, end]])', 'Returns the number of non-overlapping occurrences of sub in the string.', `"hello".count('l')  # 2`);
_('encode', 'str', 'str.encode(encoding="utf-8", errors="strict")', 'Returns the bytes-encoded version of the string.', `"hé".encode()  # b'h\\xe9'`);
_('endswith', 'str', 'str.endswith(suffix[, start[, end]])', 'Returns True if the string ends with the given suffix.', `"hello.py".endswith('.py')  # True`);
_('expandtabs', 'str', 'str.expandtabs(tabsize=8)', 'Replaces tab characters with spaces up to the given tab size.', `"a\\tb".expandtabs(4)  # "a   b"`);
_('find', 'str', 'str.find(sub[, start[, end]])', 'Returns the lowest index where sub is found, or -1 if not found.', `"hello".find('l')   # 2\n"hello".find('z')  # -1`);
_('format', 'str', 'str.format(*args, **kwargs)', 'Formats the string using replacement fields marked with {}.', `"Hello {}!".format("World")  # "Hello World!"`);
_('format_map', 'str', 'str.format_map(mapping)', 'Similar to format() but uses a mapping (dict) directly.', `"{name}".format_map({"name": "Bob"})  # "Bob"`);
_('index', 'str', 'str.index(sub[, start[, end]])', 'Like find() but raises ValueError if sub is not found.', `"hello".index('l')  # 2`);
_('isalnum', 'str', 'str.isalnum()', 'Returns True if all characters are alphanumeric and there is at least one character.', `"abc123".isalnum()  # True\n"abc!".isalnum()   # False`);
_('isalpha', 'str', 'str.isalpha()', 'Returns True if all characters are alphabetic and there is at least one character.', `"hello".isalpha()  # True\n"h3llo".isalpha() # False`);
_('isascii', 'str', 'str.isascii()', 'Returns True if all characters in the string are ASCII.', `"hello".isascii()  # True\n"héllo".isascii() # False`);
_('isdecimal', 'str', 'str.isdecimal()', 'Returns True if all characters are decimal characters.', `"123".isdecimal()  # True\n"½".isdecimal()   # False`);
_('isdigit', 'str', 'str.isdigit()', 'Returns True if all characters are digits.', `"123".isdigit()  # True\n"5".isdigit()    # True`);
_('isidentifier', 'str', 'str.isidentifier()', 'Returns True if the string is a valid Python identifier.', `"my_var".isidentifier()  # True\n"2var".isidentifier()  # False`);
_('islower', 'str', 'str.islower()', 'Returns True if all cased characters are lowercase.', `"hello".islower()  # True\n"Hello".islower() # False`);
_('isnumeric', 'str', 'str.isnumeric()', 'Returns True if all characters are numeric (includes fractions, Roman numerals).', `"123".isnumeric()  # True\n"½".isnumeric()   # True`);
_('isprintable', 'str', 'str.isprintable()', 'Returns True if all characters are printable or the string is empty.', `"hello\\n".isprintable()  # False`);
_('isspace', 'str', 'str.isspace()', 'Returns True if there are only whitespace characters and at least one character.', `"   ".isspace()  # True`);
_('istitle', 'str', 'str.istitle()', 'Returns True if the string is title-cased (capital first letter per word).', `"Hello World".istitle()  # True`);
_('isupper', 'str', 'str.isupper()', 'Returns True if all cased characters are uppercase.', `"HELLO".isupper()  # True`);
_('join', 'str', 'str.join(iterable)', 'Concatenates the elements of iterable into one string, using the string as separator.', `", ".join(["a","b","c"])  # "a, b, c"`);
_('ljust', 'str', 'str.ljust(width[, fillchar])', 'Left-justifies the string in a string of length width, padding with fillchar.', `"hi".ljust(5, '-')  # "hi---"`);
_('lower', 'str', 'str.lower()', 'Returns a copy with all cased characters converted to lowercase.', `"Hello".lower()  # "hello"`);
_('lstrip', 'str', 'str.lstrip([chars])', 'Removes leading characters (whitespace by default).', `"  hello".lstrip()     # "hello"\n"..hi".lstrip('.') # "hi"`);
_('maketrans', 'str', 'str.maketrans(x[, y[, z]])', 'Returns a translation table for translate().', `t = str.maketrans("ae", "XZ")\n"hello".translate(t)  # "hXllo"`);
_('partition', 'str', 'str.partition(sep)', 'Splits the string at the first occurrence of sep. Returns (head, sep, tail).', `"hello world".partition(" ")  # ("hello", " ", "world")`);
_('removeprefix', 'str', 'str.removeprefix(prefix)', 'Removes the prefix if present, otherwise returns the original string. (Python 3.9+)', `"HelloWorld".removeprefix("Hello")  # "World"`);
_('removesuffix', 'str', 'str.removesuffix(suffix)', 'Removes the suffix if present, otherwise returns the original. (Python 3.9+)', `"HelloWorld".removesuffix("World")  # "Hello"`);
_('replace', 'str', 'str.replace(old, new[, count])', 'Returns a copy with all occurrences of old replaced by new. Count limits replacements.', `"hello".replace('l', 'x')       # "hexxo"\n"hello".replace('l', 'x', 1)  # "hexlo"`);
_('rfind', 'str', 'str.rfind(sub[, start[, end]])', 'Returns the highest index where sub is found, or -1 if not found.', `"hello".rfind('l')  # 3`);
_('rindex', 'str', 'str.rindex(sub[, start[, end]])', 'Like rfind() but raises ValueError if sub is not found.', `"hello".rindex('l')  # 3`);
_('rjust', 'str', 'str.rjust(width[, fillchar])', 'Right-justifies the string in a string of length width, padding with fillchar.', `"hi".rjust(5, '-')  # "---hi"`);
_('rpartition', 'str', 'str.rpartition(sep)', 'Splits at the last occurrence of sep. Returns (head, sep, tail).', `"hello world".rpartition(" ")  # ("hello", " ", "world")`);
_('rsplit', 'str', 'str.rsplit(sep=None, maxsplit=-1)', 'Splits from the right. Returns a list of words.', `"a b c".rsplit(' ', 1)  # ["a b", "c"]`);
_('rstrip', 'str', 'str.rstrip([chars])', 'Removes trailing characters (whitespace by default).', `"hello  ".rstrip()  # "hello"`);
_('split', 'str', 'str.split(sep=None, maxsplit=-1)', 'Splits the string into a list. If sep is None, splits on whitespace.', `"a b c".split()        # ["a", "b", "c"]\n"a,b".split(',')      # ["a", "b"]\n"a b c".split(' ', 1) # ["a", "b c"]`);
_('splitlines', 'str', 'str.splitlines([keepends])', 'Splits on line boundaries into a list of lines.', `"a\\nb".splitlines()  # ["a", "b"]`);
_('startswith', 'str', 'str.startswith(prefix[, start[, end]])', 'Returns True if the string starts with the given prefix.', `"hello".startswith('he')  # True`);
_('strip', 'str', 'str.strip([chars])', 'Removes leading and trailing characters (whitespace by default).', `"  hello  ".strip()  # "hello"\n"..hi..".strip('.') # "hi"`);
_('swapcase', 'str', 'str.swapcase()', 'Returns a copy with uppercase converted to lowercase and vice versa.', `"Hello".swapcase()  # "hELLO"`);
_('title', 'str', 'str.title()', 'Returns a title-cased version (capital first letter per word).', `"hello world".title()  # "Hello World"`);
_('translate', 'str', 'str.translate(table)', 'Returns a copy where each character has been mapped through the given translation table.', `t = str.maketrans("ae", "XZ")\n"hello".translate(t)  # "hXllo"`);
_('upper', 'str', 'str.upper()', 'Returns a copy with all cased characters converted to uppercase.', `"Hello".upper()  # "HELLO"`);
_('zfill', 'str', 'str.zfill(width)', 'Returns a copy left-padded with ASCII zeros to make the string length width.', `"42".zfill(5)  # "00042"`);

// ── LIST METHODS ───────────────────────────────────────────────────────────
_('append', 'list', 'list.append(x)', 'Adds item x to the end of the list. Modifies in place, returns None.', `nums = [1, 2]\nnums.append(3)\n# nums is now [1, 2, 3]`);
_('clear', 'list', 'list.clear()', 'Removes all items from the list. Modifies in place.', `nums = [1, 2]\nnums.clear()\n# nums is now []`);
_('copy', 'list', 'list.copy()', 'Returns a shallow copy of the list.', `nums = [1, 2]\nnums2 = nums.copy()`);
_('count', 'list', 'list.count(x)', 'Returns the number of times x appears in the list.', `[1, 2, 2, 3].count(2)  # 2`);
_('extend', 'list', 'list.extend(iterable)', 'Extends the list by appending all items from the iterable.', `nums = [1, 2]\nnums.extend([3, 4])\n# nums is now [1, 2, 3, 4]`);
_('index', 'list', 'list.index(x[, start[, end]])', 'Returns the index of the first item equal to x. Raises ValueError if not found.', `[10, 20, 30].index(20)  # 1`);
_('insert', 'list', 'list.insert(i, x)', 'Inserts item x at index i. Shifts the rest right.', `nums = [1, 3]\nnums.insert(1, 2)\n# nums is now [1, 2, 3]`);
_('pop', 'list', 'list.pop([i])', 'Removes and returns the item at index i (default: last item).', `nums = [10, 20, 30]\nnums.pop()   # returns 30, nums is [10, 20]\nnums.pop(0) # returns 10, nums is [20]`);
_('remove', 'list', 'list.remove(x)', 'Removes the first occurrence of x. Raises ValueError if not found.', `nums = [1, 2, 3, 2]\nnums.remove(2)\n# nums is now [1, 3, 2]`);
_('reverse', 'list', 'list.reverse()', 'Reverses the list in place. Returns None.', `nums = [1, 2, 3]\nnums.reverse()\n# nums is now [3, 2, 1]`);
_('sort', 'list', 'list.sort(*, key=None, reverse=False)', 'Sorts the list in place. Key is a function, reverse flips order.', `nums = [3, 1, 2]\nnums.sort()\n# nums is now [1, 2, 3]\n\nnums.sort(reverse=True)\n# nums is now [3, 2, 1]`);

// ── DICT METHODS ───────────────────────────────────────────────────────────
_('clear', 'dict', 'dict.clear()', 'Removes all items from the dictionary.', `d = {"a": 1}\nd.clear()\n# d is now {}`);
_('copy', 'dict', 'dict.copy()', 'Returns a shallow copy of the dictionary.', `d = {"a": 1}\nd2 = d.copy()`);
_('fromkeys', 'dict', 'dict.fromkeys(iterable[, value])', 'Creates a new dict with keys from iterable, all set to value (default None).', `dict.fromkeys(["a","b"], 0)  # {"a": 0, "b": 0}`);
_('get', 'dict', 'dict.get(key[, default])', 'Returns the value for key if it exists, otherwise default (None). Never raises KeyError.', `d = {"a": 1}\nd.get("a")      # 1\nd.get("x")      # None\nd.get("x", 0)   # 0`);
_('items', 'dict', 'dict.items()', 'Returns a view of (key, value) pairs. Use in for loops.', `d = {"a": 1, "b": 2}\nfor k, v in d.items(): print(k, v)`);
_('keys', 'dict', 'dict.keys()', 'Returns a view of all keys in the dictionary.', `d = {"a": 1, "b": 2}\nlist(d.keys())  # ["a", "b"]`);
_('pop', 'dict', 'dict.pop(key[, default])', 'Removes and returns the value for key. Returns default if key missing (instead of error).', `d = {"a": 1}\nd.pop("a")  # 1, d is now {}`);
_('popitem', 'dict', 'dict.popitem()', 'Removes and returns the last inserted (key, value) pair as a tuple. Raises KeyError if empty.', `d = {"a": 1}\nd.popitem()  # ("a", 1)`);
_('setdefault', 'dict', 'dict.setdefault(key[, default])', 'Returns the value for key. If key missing, inserts default and returns it.', `d = {"a": 1}\nd.setdefault("a", 99)  # 1 (existing)\nd.setdefault("b", 0)   # 0 (inserted)`);
_('update', 'dict', 'dict.update([other])', 'Updates the dict with key/value pairs from other. Overwrites existing keys.', `d = {"a": 1}\nd.update({"b": 2})\n# d is now {"a": 1, "b": 2}`);
_('values', 'dict', 'dict.values()', 'Returns a view of all values in the dictionary.', `d = {"a": 1, "b": 2}\nlist(d.values())  # [1, 2]`);

// ── SET METHODS ────────────────────────────────────────────────────────────
_('add', 'set', 'set.add(x)', 'Adds element x to the set. If x already present, does nothing.', `s = {1, 2}\ns.add(3)\n# s is now {1, 2, 3}`);
_('clear', 'set', 'set.clear()', 'Removes all elements from the set.', `s = {1, 2}\ns.clear()\n# s is now set()`);
_('copy', 'set', 'set.copy()', 'Returns a shallow copy of the set.', `s = {1, 2}\ns2 = s.copy()`);
_('difference', 'set', 'set.difference(*others)', 'Returns a new set with elements in the set that are not in the others.', `{1, 2, 3}.difference({2, 4})  # {1, 3}`);
_('difference_update', 'set', 'set.difference_update(*others)', 'Removes elements found in others. Modifies in place.', `s = {1, 2, 3}\ns.difference_update({2, 4})\n# s is now {1, 3}`);
_('discard', 'set', 'set.discard(x)', 'Removes x from the set if present. Does NOT raise an error if missing.', `s = {1, 2}\ns.discard(99)  # no error`);
_('intersection', 'set', 'set.intersection(*others)', 'Returns a new set with elements common to the set and all others.', `{1, 2, 3}.intersection({2, 4})  # {2}`);
_('intersection_update', 'set', 'set.intersection_update(*others)', 'Keeps only elements found in the set and all others. Modifies in place.', `s = {1, 2, 3}\ns.intersection_update({2, 4})\n# s is now {2}`);
_('isdisjoint', 'set', 'set.isdisjoint(other)', 'Returns True if the set has no elements in common with other.', `{1, 2}.isdisjoint({3, 4})  # True`);
_('issubset', 'set', 'set.issubset(other)', 'Returns True if every element of the set is in other.', `{1, 2}.issubset({1, 2, 3})  # True`);
_('issuperset', 'set', 'set.issuperset(other)', 'Returns True if every element of other is in the set.', `{1, 2, 3}.issuperset({1, 2})  # True`);
_('pop', 'set', 'set.pop()', 'Removes and returns an arbitrary element. Raises KeyError if empty.', `s = {10, 20}\ns.pop()  # 10 or 20 (arbitrary)`);
_('remove', 'set', 'set.remove(x)', 'Removes x from the set. Raises KeyError if x not found.', `s = {1, 2}\ns.remove(2)`);
_('symmetric_difference', 'set', 'set.symmetric_difference(other)', 'Returns a new set with elements in either set but not both.', `{1, 2, 3}.symmetric_difference({2, 4})  # {1, 3, 4}`);
_('symmetric_difference_update', 'set', 'set.symmetric_difference_update(other)', 'Updates the set to keep only elements in either set but not both.', `s = {1, 2, 3}\ns.symmetric_difference_update({2, 4})\n# s is now {1, 3, 4}`);
_('union', 'set', 'set.union(*others)', 'Returns a new set with elements from the set and all others.', `{1, 2}.union({3, 4})  # {1, 2, 3, 4}`);
_('update', 'set', 'set.update(*others)', 'Adds all elements from others. Modifies in place.', `s = {1, 2}\ns.update({3, 4})\n# s is now {1, 2, 3, 4}`);

// ── TUPLE METHODS ──────────────────────────────────────────────────────────
_('count', 'tuple', 'tuple.count(x)', 'Returns the number of times x appears in the tuple. Returns 0 if not found.', `t = (1, 2, 2, 3, 2, 4)
t.count(2)    # 3 (three occurrences of 2)
t.count(5)    # 0 (not found)
t.count(1)    # 1`);
_('index', 'tuple', 'tuple.index(x[, start[, end]])', 'Returns the index of the first item equal to x. Can specify start and end to search a slice. Raises ValueError if not found.', `t = (10, 20, 30, 20, 40)
t.index(20)       # 1 (first occurrence)
t.index(20, 2)    # 3 (search from index 2 onward)
t.index(20, 2, 4) # 3 (search between index 2-4)
# t.index(99)     # ValueError: not in tuple`);

// ── BUILT-IN FUNCTIONS ─────────────────────────────────────────────────────
_('abs', 'builtin', 'abs(x)', 'Returns the absolute value of a number.', `abs(-5)    # 5\nabs(3+4j)  # 5.0`);
_('aiter', 'builtin', 'aiter(async_iterable)', 'Returns an asynchronous iterator for an asynchronous iterable.', `iterator = aiter(async_items)`);
_('all', 'builtin', 'all(iterable)', 'Returns True if every element of the iterable is truthy.', `all([True, 1, "a"])   # True\nall([True, 0, "a"])   # False`);
_('anext', 'builtin', 'await anext(async_iterator[, default])', 'Returns the next item from an asynchronous iterator.', `item = await anext(async_iterator, None)`);
_('any', 'builtin', 'any(iterable)', 'Returns True if any element of the iterable is truthy.', `any([False, 0, "a"])  # True\nany([False, 0, ""])   # False`);
_('ascii', 'builtin', 'ascii(object)', 'Returns a printable string with non-ASCII chars escaped (like repr but always escapes).', `ascii("héllo")  # "'h\\xe9llo'"`);
_('bin', 'builtin', 'bin(x)', 'Converts an integer to a binary string prefixed with "0b".', `bin(5)   # "0b101"\nbin(255) # "0b11111111"`);
_('bool', 'builtin', 'bool([x])', 'Converts a value to a Boolean (True/False).', `bool(1)    # True\nbool(0)    # False\nbool([])   # False\nbool("a")  # True`);
_('breakpoint', 'builtin', 'breakpoint(*args, **kwargs)', 'Drops you into the debugger at that line (pdb by default).', `for i in range(10):\n    breakpoint()  # opens debugger here`);
_('bytearray', 'builtin', 'bytearray([source[, encoding[, errors]]])', 'Returns a mutable array of bytes.', `bytearray("hi", "utf-8")  # bytearray(b'hi')`);
_('bytes', 'builtin', 'bytes([source[, encoding[, errors]]])', 'Returns an immutable bytes object.', `bytes("hi", "utf-8")  # b'hi'`);
_('callable', 'builtin', 'callable(object)', 'Returns True if the object can be called (like a function or class).', `callable(print)  # True\ncallable(42)    # False`);
_('chr', 'builtin', 'chr(i)', 'Returns the Unicode string for integer i (inverse of ord()).', `chr(97)  # "a"\nchr(8364) # "€"`);
_('classmethod', 'builtin', '@classmethod', 'Marks a method that receives the class (cls) instead of instance (self).', `class MyClass:\n    @classmethod\n    def create(cls): return cls()`);
_('compile', 'builtin', 'compile(source, filename, mode)', 'Compiles source into a code object for exec() or eval().', `code = compile("x = 5", "<string>", "exec")\nexec(code)`);
_('complex', 'builtin', 'complex(real[, imag])', 'Creates a complex number.', `complex(3, 4)  # (3+4j)`);
_('delattr', 'builtin', 'delattr(object, name)', 'Deletes the named attribute from an object.', `delattr(obj, "x")  # same as del obj.x`);
_('dict', 'builtin', 'dict([mapping_or_iterable])', 'Creates a new dictionary.', `dict(a=1, b=2)            # {"a": 1, "b": 2}\ndict([("a",1), ("b",2)])  # {"a": 1, "b": 2}`);
_('dir', 'builtin', 'dir([object])', 'Returns a sorted list of names in the current scope or on the object.', `dir("hello")  # all string methods listed`);
_('divmod', 'builtin', 'divmod(a, b)', 'Returns (quotient, remainder) as a tuple.', `divmod(10, 3)  # (3, 1)`);
_('enumerate', 'builtin', 'enumerate(iterable, start=0)', 'Returns (index, value) pairs for an iterable.', `for i, v in enumerate(["a","b"]): print(i, v)\n# 0 a\\n1 b`);
_('eval', 'builtin', 'eval(expression[, globals[, locals]])', 'Evaluates a string as a Python expression. Use with caution.', `eval("2 + 3")  # 5`);
_('exec', 'builtin', 'exec(code[, globals[, locals]])', 'Executes dynamically created Python code.', `exec("x = 5\\nprint(x)")  # prints 5`);
_('filter', 'builtin', 'filter(function, iterable)', 'Returns an iterator yielding items where function(item) is True.', `list(filter(lambda x: x > 0, [-1, 2, -3, 4]))  # [2, 4]`);
_('float', 'builtin', 'float([x])', 'Converts a string or number to a float.', `float("3.14")  # 3.14\nfloat(5)       # 5.0`);
_('format', 'builtin', 'format(value[, format_spec])', 'Formats a value using a format specifier.', `format(3.14159, ".2f")  # "3.14"\nformat(255, "x")       # "ff"`);
_('frozenset', 'builtin', 'frozenset([iterable])', 'Returns an immutable (unmodifiable) set.', `frozenset([1, 2, 3])`);
_('getattr', 'builtin', 'getattr(object, name[, default])', 'Gets the named attribute from an object. Safe form of obj.attr.', `getattr(obj, "x", 0)  # obj.x or 0 if missing`);
_('globals', 'builtin', 'globals()', 'Returns the global namespace dictionary.', `globals()["x"] = 5  # creates global x`);
_('hasattr', 'builtin', 'hasattr(object, name)', 'Returns True if the object has the named attribute.', `hasattr("hello", "upper")  # True`);
_('hash', 'builtin', 'hash(object)', 'Returns the hash value of an object (int used for dict lookups).', `hash("hello")  # some integer`);
_('help', 'builtin', 'help([object])', 'Launches the interactive help viewer for the given object.', `help(list.append)  # shows docs for list.append`);
_('hex', 'builtin', 'hex(x)', 'Converts an integer to a hex string prefixed with "0x".', `hex(255)  # "0xff"\nhex(16)   # "0x10"`);
_('id', 'builtin', 'id(object)', 'Returns a unique integer ID for an object (memory address in CPython).', `id("hello")  # 140234567890123`);
_('input', 'builtin', 'input([prompt])', 'Reads a line from stdin, returns it as a string.', `name = input("Enter name: ")`);
_('int', 'builtin', 'int([x[, base]])', 'Converts a string or number to an integer.', `int("42")     # 42\nint("ff", 16) # 255\nint(3.9)      # 3 (truncates)`);
_('isinstance', 'builtin', 'isinstance(object, classinfo)', 'Returns True if object is an instance of the given class(es).', `isinstance(5, int)              # True\nisinstance("a", (str, list))    # True`);
_('issubclass', 'builtin', 'issubclass(class, classinfo)', 'Returns True if class is a subclass of classinfo.', `issubclass(bool, int)  # True`);
_('iter', 'builtin', 'iter(object[, sentinel])', 'Returns an iterator for the object.', `it = iter([1, 2, 3])\nnext(it)  # 1`);
_('len', 'builtin', 'len(s)', 'Returns the length (number of items) of a sequence or collection.', `len("hello")  # 5\nlen([1,2,3])  # 3`);
_('list', 'builtin', 'list([iterable])', 'Creates a list from an iterable, or an empty list if no argument.', `list("abc")     # ["a", "b", "c"]\nlist(range(3))  # [0, 1, 2]`);
_('locals', 'builtin', 'locals()', 'Returns the local namespace dictionary.', `x = 5\nlocals()["x"]  # 5`);
_('map', 'builtin', 'map(function, iterable, ...)', 'Returns an iterator applying function to every item.', `list(map(lambda x: x*2, [1, 2, 3]))  # [2, 4, 6]`);
_('max', 'builtin', 'max(iterable, *[, key, default])', 'Returns the largest item in the iterable.', `max([3, 1, 7])        # 7\nmax("abc")            # "c"\nmax([], default=0)    # 0`);
_('memoryview', 'builtin', 'memoryview(object)', 'Returns a memory-view object from a bytes-like object.', `memoryview(b"hello")`);
_('min', 'builtin', 'min(iterable, *[, key, default])', 'Returns the smallest item in the iterable.', `min([3, 1, 7])  # 1`);
_('next', 'builtin', 'next(iterator[, default])', 'Returns the next item from an iterator. If exhausted, returns default.', `it = iter([1, 2])\nnext(it)  # 1\nnext(it)  # 2\nnext(it, "done")  # "done"`);
_('object', 'builtin', 'object()', 'Returns a featureless base object. Parent of all classes.', `obj = object()`);
_('oct', 'builtin', 'oct(x)', 'Converts an integer to an octal string prefixed with "0o".', `oct(8)  # "0o10"\noct(64) # "0o100"`);
_('open', 'builtin', 'open(file, mode="r", ...)', 'Opens a file and returns a file object.', `with open("file.txt") as f:\n    data = f.read()`);
_('ord', 'builtin', 'ord(c)', 'Returns the Unicode code point of a character (inverse of chr()).', `ord("a")  # 97\nord("€")  # 8364`);
_('pow', 'builtin', 'pow(x, y[, mod])', 'Returns x**y. With mod, returns (x**y) % z efficiently.', `pow(2, 3)     # 8\npow(2, 3, 5)  # 3  (8 % 5)`);
_('print', 'builtin', 'print(*objects, sep=" ", end="\\n", file=None, flush=False)', 'Prints objects to the text stream.', `print("Hello", "World")  # Hello World\nprint("a", "b", sep="-") # a-b`);
_('property', 'builtin', '@property / property(getter, setter, deleter, doc)', 'Creates a managed attribute with get/set/delete hooks.', `class C:\n    @property\n    def x(self): return self._x`);
_('range', 'builtin', 'range(stop) / range(start, stop[, step])', 'Returns an immutable sequence of numbers. Stop is exclusive.', `list(range(5))      # [0, 1, 2, 3, 4]\nlist(range(2, 5))    # [2, 3, 4]\nlist(range(0, 10, 2)) # [0, 2, 4, 6, 8]`);
_('repr', 'builtin', 'repr(object)', 'Returns a string containing a printable representation of an object.', `repr("hello")  # "'hello'"\nrepr([1,2])    # "[1, 2]"`);
_('reversed', 'builtin', 'reversed(seq)', 'Returns a reverse iterator over the sequence.', `list(reversed([1, 2, 3]))  # [3, 2, 1]`);
_('round', 'builtin', 'round(number[, ndigits])', 'Rounds a number to a given precision in decimal digits.', `round(3.14159, 2)  # 3.14\nround(3.5)         # 4`);
_('set', 'builtin', 'set([iterable])', 'Creates a set from an iterable, or empty set if no argument.', `set([1, 2, 2, 3])  # {1, 2, 3}\nset("hello")       # {"h", "e", "l", "o"}`);
_('setattr', 'builtin', 'setattr(object, name, value)', 'Sets the named attribute on an object.', `setattr(obj, "x", 5)  # same as obj.x = 5`);
_('slice', 'builtin', 'slice(start, stop[, step])', 'Returns a slice object representing a range of indices.', `s = slice(1, 5, 2)\n"hello"[s]  # "el"`);
_('sorted', 'builtin', 'sorted(iterable, *, key=None, reverse=False)', 'Returns a new sorted list from the items in iterable.', `sorted([3, 1, 2])                    # [1, 2, 3]\nsorted("cba")                        # ["a", "b", "c"]\nsorted([-2, 1, -3], key=abs)         # [1, -2, -3]`);
_('staticmethod', 'builtin', '@staticmethod', 'Marks a method that does not receive self or cls.', `class C:\n    @staticmethod\n    def f(x): return x*2`);
_('str', 'builtin', 'str([object])', 'Returns a string version of the object.', `str(42)    # "42"\nstr([1,2]) # "[1, 2]"`);
_('sum', 'builtin', 'sum(iterable, start=0)', 'Sums all items of the iterable, starting from start.', `sum([1, 2, 3])      # 6\nsum([1, 2, 3], 10)  # 16`);
_('super', 'builtin', 'super([type[, object-or-type]])', 'Returns a proxy object for calling parent class methods.', `class Child(Parent):\n    def __init__(self):\n        super().__init__()`);
_('tuple', 'builtin', 'tuple([iterable])', 'Creates a tuple from an iterable, or empty tuple if no argument.', `tuple([1, 2, 3])  # (1, 2, 3)\ntuple("ab")       # ("a", "b")`);
_('type', 'builtin', 'type(object) / type(name, bases, dict)', 'Returns the type of an object, or creates a new class.', `type(5)       # <class 'int'>\ntype("hello")  # <class 'str'>`);
_('vars', 'builtin', 'vars([object])', 'Returns __dict__ of a module, class, instance, or local scope.', `vars()  # local namespace dict`);
_('zip', 'builtin', 'zip(*iterables, strict=False)', 'Returns an iterator of tuples, pairing up elements from each iterable.', `list(zip([1,2], ["a","b"]))  # [(1, "a"), (2, "b")]\ndict(zip(["k1","k2"], [1,2])) # {"k1": 1, "k2": 2}`);
_('__import__', 'builtin', '__import__(name, globals=None, locals=None, fromlist=(), level=0)', 'Low-level function used by the import statement. Most code should use import instead.', `math = __import__("math")\nmath.sqrt(16)  # 4.0`);

// ── KEYWORD / BUILT-IN CONSTANTS ──────────────────────────────────────────
_('True', 'keyword', 'True', 'Boolean true value. The integer 1.', `True == 1  # True`);
_('False', 'keyword', 'False', 'Boolean false value. The integer 0.', `False == 0  # True`);
_('None', 'keyword', 'None', 'Represents the absence of a value. Not the same as 0 or False.', `x = None\nif x is None: print("no value")`);
_('and', 'keyword', 'and', 'Logical AND. Returns True only if both operands are truthy.', `True and False  # False\n5 > 0 and "a" < "b"  # True`);
_('or', 'keyword', 'or', 'Logical OR. Returns True if at least one operand is truthy.', `False or True  # True\n0 or 42        # 42 (short-circuits)`);
_('not', 'keyword', 'not', 'Logical NOT. Returns the inverse truth value.', `not True   # False\nnot 0      # True\nnot "abc"  # False`);
_('is', 'keyword', 'is', 'Identity comparison. True if both sides refer to the same object.', `x = [1]\ny = [1]\nx is y     # False (different objects)\nx is x     # True`);
_('in', 'keyword', 'in', 'Membership test. True if the value is found in the container.', `"a" in "abc"  # True\n3 in [1,2,4]  # False\n"x" in {"x": 1}  # True (checks keys)`);
_('if', 'keyword', 'if condition:', 'Starts a conditional block. Executes body only if condition is truthy.', `if x > 0:\n    print("positive")`);
_('elif', 'keyword', 'elif condition:', 'Else-if. Additional condition after if/elif.', `if x > 0:\n    print("pos")\nelif x == 0:\n    print("zero")`);
_('else', 'keyword', 'else:', 'Final branch when no prior condition was true.', `if x > 0:\n    print("pos")\nelse:\n    print("neg or zero")`);
_('for', 'keyword', 'for var in iterable:', 'Loops over each item in an iterable.', `for i in range(3):\n    print(i)  # 0 1 2`);
_('while', 'keyword', 'while condition:', 'Repeats the body as long as condition is truthy.', `i = 0\nwhile i < 3:\n    print(i)\n    i += 1`);
_('break', 'keyword', 'break', 'Exits the current loop immediately.', `for i in range(10):\n    if i == 3: break\n    # i will be 0, 1, 2 only`);
_('continue', 'keyword', 'continue', 'Skips the rest of the loop body and jumps to the next iteration.', `for i in range(5):\n    if i == 2: continue\n    print(i)  # 0 1 3 4 (no 2)`);
_('def', 'keyword', 'def name(params):', 'Defines a function.', `def greet(name):\n    return f"Hello {name}"`);
_('return', 'keyword', 'return [value]', 'Exits a function and sends a value back to the caller. Without value, returns None.', `def add(a, b):\n    return a + b\nx = add(2, 3)  # x = 5`);
_('class', 'keyword', 'class Name:', 'Defines a class.', `class Dog:\n    def bark(self):\n        print("woof")`);
_('import', 'keyword', 'import module', 'Imports a module into the current namespace.', `import math\nprint(math.sqrt(16))  # 4.0`);
_('from', 'keyword', 'from module import name', 'Imports a specific name from a module.', `from math import sqrt\nprint(sqrt(16))  # 4.0`);
_('as', 'keyword', 'import module as alias', 'Imports with a custom name/alias.', `import numpy as np`);
_('pass', 'keyword', 'pass', 'Does nothing. Used as a placeholder where syntax requires a statement.', `if True:\n    pass  # placeholder`);
_('del', 'keyword', 'del target', 'Deletes a variable, list element, or dict key.', `x = [1, 2, 3]\ndel x[1]    # x is now [1, 3]\ndel x       # x is gone`);
_('try', 'keyword', 'try:', 'Starts a try block for exception handling.', `try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print("cannot divide by zero")`);
_('except', 'keyword', 'except [ExceptionType]:', 'Catches exceptions raised in the try block.', `try:\n    int("abc")\nexcept ValueError:\n    print("not a number")`);
_('finally', 'keyword', 'finally:', 'Always runs after try/except, even if an exception occurred.', `try:\n    f = open("file")\nfinally:\n    f.close()  # always runs`);
_('raise', 'keyword', 'raise [Exception]', 'Manually raises an exception.', `raise ValueError("bad value")`);
_('assert', 'keyword', 'assert condition [, message]', 'Tests a condition. Raises AssertionError if False.', `assert x > 0, "x must be positive"`);
_('yield', 'keyword', 'yield [value]', 'Pauses a generator function and yields a value to the caller.', `def gen():\n    yield 1\n    yield 2`);
_('lambda', 'keyword', 'lambda args: expression', 'Creates a small anonymous function.', `add = lambda a, b: a + b\nadd(2, 3)  # 5`);
_('nonlocal', 'keyword', 'nonlocal name', 'Declares a variable refers to an enclosing (non-global) scope. Used in nested functions.', `def outer():\n    x = 0\n    def inner():\n        nonlocal x\n        x += 1\n    inner()`);
_('global', 'keyword', 'global name', 'Declares a variable refers to the module scope (global).', `x = 0\ndef set_x():\n    global x\n    x = 5`);
_('with', 'keyword', 'with expr as var:', 'Context manager — auto-closes/cleans up resources.', `with open("file.txt") as f:\n    data = f.read()`);
_('async', 'keyword', 'async def', 'Marks a function as asynchronous (returns a coroutine).', `async def fetch():\n    return await some_api()`);
_('await', 'keyword', 'await coroutine', 'Pauses execution until a coroutine completes.', `data = await fetch()`);
_('match', 'keyword', 'match subject:', 'Starts a match-case (structural pattern matching) block. Python 3.10+.', `match value:\n    case 1: print("one")\n    case _: print("other")`);
_('case', 'keyword', 'case pattern:', 'A pattern branch inside a match block.', `match x:\n    case int(): print("int")\n    case str(): print("str")`);

// ── CONCEPTS ──────────────────────────────────────────────────────────────
_('variable', 'concept', 'variable = value', 'A name that stores a reference to an object. Variables are created by assignment. No type declaration needed.', `x = 5\nname = "Alice"\nmy_list = [1, 2, 3]`);
_('identifier', 'concept', '—', 'A name used to identify a variable, function, class, or module. Rules: letters, digits, underscores; cannot start with digit; case-sensitive.', `valid: my_var, _private, Var2\ninvalid: 2var, my-var, for (keyword)`);
_('indentation', 'concept', '—', 'Python uses indentation (spaces or tabs) to define code blocks. Standard is 4 spaces. Mixing tabs and spaces is an error.', `def greet(name):\n    return f"Hello {name}"  # 4 spaces before return`);
_('function', 'concept', 'def name(parameters):', 'A reusable block of code. A function can receive arguments, run statements, and return a result to the caller. Use functions when you want named, reusable logic instead of repeating code.', `def square(number):\n    return number ** 2\n\nanswer = square(5)\nprint(answer)  # 25`);
_('module', 'concept', 'import module_name', 'A Python file or installed package you can import. Modules organize reusable code. For example, math is a module for mathematical tools, and your own file helper.py can also be imported as a module.', `import math\nprint(math.sqrt(16))  # 4.0\n\nfrom math import pi\nprint(pi)`);
_('library', 'concept', 'collection of modules/packages', 'A library is a collection of reusable code, usually made of modules and packages. Python includes a standard library, and you can install third-party libraries such as requests, pandas, or numpy.', `import random\nprint(random.randint(1, 10))\n\n# random is from Python's standard library`);
_('object-oriented programming', 'concept', 'class / object / attribute / method', 'Object-oriented programming groups data and behavior together. A class is a blueprint, an object is an instance of that blueprint, attributes store data, and methods are functions attached to the object.', `class Dog:\n    def __init__(self, name):\n        self.name = name  # attribute\n\n    def bark(self):      # method\n        return f"{self.name} says woof"\n\npet = Dog("Noll")\nprint(pet.bark())`);
_('attribute', 'concept', 'object.attribute', 'An attribute is a value stored on an object. You access it with dot notation. Methods are also attributes, but they are callable functions attached to an object.', `class User:\n    def __init__(self, name):\n        self.name = name\n\nuser = User("Noll")\nprint(user.name)  # attribute access`);
_('lambda expression', 'concept', 'lambda arguments: expression', 'A lambda is a small anonymous function written as one expression. Python evaluates the expression after the colon when the lambda is called. Use it for short callbacks, sorting keys, map/filter, or quick transformations.', `double = lambda x: x * 2\nprint(double(4))  # 8\n\nnums = [3, 1, 2]\nprint(sorted(nums, key=lambda x: -x))  # [3, 2, 1]`);
_('slicing', 'concept', 'sequence[start:stop:step]', 'Extracts a portion of a sequence (string, list, tuple). Start INCLUSIVE, stop EXCLUSIVE. Negative indices count from the end.', `s = "python"\ns[0:3]    # "pyt"  (indices 0,1,2 — 3 is EXCLUDED)\ns[-3:]    # "hon"  (last 3)\ns[::-1]   # "nohtyp" (reverse)\ns[::2]    # "pto"  (every other)`);
_('return vs print', 'concept', '—', 'return sends a value back to the caller (usable in code). print displays text to the console (not usable in code).', `def add(a, b):\n    return a + b    # caller can capture this\n\nx = add(2, 3)  # x = 5\n\nprint(5)  # shows "5" in console, but nothing captures it`);
_('closure', 'concept', '—', 'A nested function that remembers variables from its enclosing scope even after the outer function finishes.', `def make_multiplier(n):\n    def multiplier(x):\n        return x * n  # "n" is remembered\n    return multiplier\n\ndouble = make_multiplier(2)\nprint(double(5))  # 10`);
_('decorator', 'concept', '@decorator', 'A function that takes another function and extends its behavior without modifying it directly.', `def timer(f):\n    def wrapper(*args):\n        print("start")\n        result = f(*args)\n        print("end")\n        return result\n    return wrapper\n\n@timer\ndef work():\n    print("working")\n\nwork()`);
_('generator', 'concept', 'yield', 'A function that uses yield to produce a sequence of values lazily (one at a time) instead of computing all at once.', `def count_to(n):\n    for i in range(n):\n        yield i\n\nfor x in count_to(3):\n    print(x)  # 0 1 2`);
_('comprehension', 'concept', '[expr for var in iterable if cond]', 'A concise way to create lists, dicts, or sets by transforming and filtering an iterable.', `squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]\nevens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]\nsquare_dict = {x: x**2 for x in range(3)}  # {0: 0, 1: 1, 2: 4}`);
_('order of operations', 'concept', 'PEMDAS / operator precedence', 'Python evaluates expressions in this order (highest to lowest): parentheses, exponentiation (**), unary +/-/not, *///%, +-, comparisons, not/and/or.', `result = 2 + 3 * 4    # 14  (* before +)\nresult = (2 + 3) * 4  # 20  (parentheses override)\nresult = 2 ** 3 * 4   # 32  (** before *)`);
_('method vs function', 'concept', '—', 'A method is a function that belongs to an object and is called on it (obj.method()). A function is standalone (func()). Methods automatically receive the object (self).', `"hello".upper()  # method — called on the string\nlen("hello")     # function — standalone\n\nlist("abc")      # function — standalone\n[1,2].append(3)  # method — called on the list`);
_('scope', 'concept', 'LEGB rule', 'Python looks up names in this order: Local, Enclosing, Global, Built-in. Variables defined in a function are local by default.', `x = 5  # global\ndef f():\n    x = 3  # local — different from global x\n    print(x)  # 3\nf()\nprint(x)  # 5`);
_('mutability', 'concept', 'mutable vs immutable', 'Mutable objects can be changed after creation (list, dict, set). Immutable cannot (int, float, str, tuple, frozenset).', `# Mutable\nnums = [1, 2]\nnums[0] = 99  # works\n\n# Immutable\ns = "hello"\ns[0] = "H"  # ERROR - strings are immutable`);
_('exception handling', 'concept', 'try/except', 'Catches and handles runtime errors gracefully instead of crashing.', `try:\n    x = int(input("Enter number: "))\nexcept ValueError:\n    print("That\'s not a number!")\nexcept ZeroDivisionError:\n    print("Can\'t divide by zero")\nexcept Exception as e:\n    print(f"Something else: {e}")`);
_('f-string', 'concept', 'f"text {expression}"', 'Embeds expressions inside string literals using {}. Python 3.6+.', `name = "Alice"\nage = 30\nprint(f"{name} is {age} years old")\nprint(f"{7 * 6}")  # "42"`);
_('list data type', 'concept', 'list = [1, 2, 3]', 'A list is an ordered, mutable collection of items. Items can be any type. Lists use square brackets and support indexing, slicing, and methods like append(), pop(), sort().', `nums = [1, 2, 3, 2]
nums.append(4)
nums[0]  # 1
nums[-1] # 4
nums.count(2)  # 2
nums[1:3]  # [2, 3]
for x in nums: print(x)`);
_('dictionary data type', 'concept', 'd = {"key": "value"}', 'A dictionary stores key-value pairs. Keys are unique and must be immutable (strings, numbers, tuples). Values can be anything. Access values via d[key]. Insertion-ordered since Python 3.7.', `d = {"name": "Alice", "age": 30}
d["name"]  # "Alice"
d.get("age", 0)  # 30
d["city"] = "Paris"  # add new key
for k, v in d.items(): print(k, v)
"name" in d  # True`);
_('tuple data type', 'concept', 't = (1, 2, 3)', 'A tuple is an ordered, IMMUTABLE sequence. Once created it cannot change. Use for fixed data that should not be modified. Can be used as dictionary keys.', `t = (1, 2, 3)
t[0]  # 1
t[1:3]  # (2, 3)
# t[0] = 99  # ERROR - tuples are immutable
point = (10, 20)
x, y = point  # tuple unpacking`);
_('set data type', 'concept', 's = {1, 2, 3}', 'A set is an unordered collection of UNIQUE, immutable items. Duplicates are automatically removed. Supports math operations: union, intersection, difference.', `s = {1, 2, 2, 3}
# s is {1, 2, 3}  (duplicates removed)
s.add(4)
{1, 2}.union({3, 4})  # {1, 2, 3, 4}
{1, 2, 3}.intersection({2, 4})  # {2}`);
_('string data type', 'concept', 's = "hello"', 'A string is an immutable sequence of Unicode characters. Can use single or double quotes. Supports methods like upper(), split(), replace(), find(), and slicing.', `s = "hello world"
s.upper()  # "HELLO WORLD"
s.split()  # ["hello", "world"]
s.replace("world", "there")  # "hello there"
s[0]   # "h"
s[-1]  # "d"
len(s)  # 11`);
_('list vs dict', 'concept', '—', 'A list stores ordered items by index (0, 1, 2...). A dict stores key-value pairs unordered (pre-3.7) or insertion-ordered (3.7+). Use lists for sequences you index by position; use dicts when you need to look up values by a name/key.', `# List: position matters
seq = ["a", "b", "c"]
seq[0]  # "a"

# Dict: name matters
mapping = {"name": "Alice", "age": 30}
mapping["name"]  # "Alice"`);
_('condition (if/else)', 'concept', 'if / elif / else', 'Conditional statements let code take different paths based on whether an expression is True or False. if runs its block when the condition is True. elif checks another condition if the previous if was False. else runs when no previous condition matched.', `score = 85\nif score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")  # runs: 85 >= 80\nelse:\n    print("C")`);

_('for loop', 'concept', 'for var in iterable:', 'A for loop iterates over every item in a sequence (list, tuple, string, range, dict, set). The loop variable takes each value one at a time, and the indented block runs once per item. Use for loops when you know the collection of items to process.', `fruits = ["apple", "banana", "cherry"]\nfor fruit in fruits:\n    print(fruit)\n\n# Range: repeat N times\nfor i in range(3):\n    print(i)  # 0 1 2\n\n# String: iterate characters\nfor char in "hi":\n    print(char)  # "h" "i"`);

_('while loop', 'concept', 'while condition:', 'A while loop repeats its indented block as long as the condition remains True. The condition is checked before every iteration. Use while loops when you do not know in advance how many times to repeat — the loop runs until something changes the condition.', `count = 0\nwhile count < 3:\n    print(count)\n    count += 1  # must update or loop forever\n\n# Infinite loop (danger!)\n# while True:\n#     print("runs forever")`);

_('for loop vs while loop', 'concept', '—', 'A for loop iterates over a known sequence (list, range, string). A while loop repeats until a condition becomes False. Use for when the number of iterations is known; use while when it depends on a condition that changes inside the loop.', `# For: fixed number of times
for i in range(5):
    print(i)

# While: conditional
x = 0
while x < 5:
    print(x)
    x += 1`);

// ── ADDITIONAL CONCEPTS ──────────────────────────────────────────────────────
_('args and kwargs', 'concept', '*args / **kwargs', '*args captures extra positional arguments as a tuple. **kwargs captures extra keyword arguments as a dict. Common in function definitions and decorators.', `def f(*args, **kwargs):
    print(args)   # tuple of positional args
    print(kwargs) # dict of keyword args

f(1, 2, x=3)
# args=(1, 2)
# kwargs={"x": 3}`);
_('unpacking', 'concept', '*iterable / **dict', 'The * operator unpacks iterables into positional arguments. The ** operator unpacks dicts into keyword arguments. Works in function calls, list/tuple/dict literals.', `nums = [1, 2, 3]
print(*nums)  # 1 2 3  (same as print(1, 2, 3))

first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]

combined = [*[1,2], *[3,4]]  # [1, 2, 3, 4]
d = {**{"a": 1}, **{"b": 2}}  # {"a": 1, "b": 2}`);
_('file I/O', 'concept', 'open() / with statement', 'Use open() to read/write files. Always close files — best done with a with block (context manager) which auto-closes.', `with open("file.txt", "r") as f:
    content = f.read()       # whole file as string
    lines = f.readlines()    # list of lines

with open("out.txt", "w") as f:
    f.write("Hello World")

# Modes: "r" read, "w" write (overwrite), "a" append,
# "rb" read binary, "wb" write binary, "r+" read+write`);
_('JSON', 'concept', 'json module', 'The json module converts between Python objects and JSON strings. json.dumps() serializes, json.loads() deserializes.', `import json

data = {"name": "Alice", "scores": [90, 85]}
json_str = json.dumps(data)       # '{"name": "Alice", "scores": [90, 85]}'
parsed = json.loads(json_str)     # back to Python dict

with open("data.json") as f:
    data = json.load(f)           # read from file

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)  # write with formatting`);
_('datetime', 'concept', 'datetime module', 'The datetime module provides date, time, timedelta, and timezone classes for working with dates and times.', `from datetime import datetime, timedelta, date

now = datetime.now()                # current date+time
today = date.today()                # current date
d = datetime(2024, 12, 25, 10, 30) # specific date

d.year   # 2024
d.month  # 12
d.strftime("%Y-%m-%d")  # "2024-12-25"

future = now + timedelta(days=7)    # 1 week from now
delta = future - now                 # timedelta object`);
_('regular expressions', 'concept', 're module', 'The re module provides full regular expression support. Use re.search() to find anywhere, re.match() to check start, re.findall() for all matches, re.sub() for replace, re.split() for split.', `import re

text = "My email: alice@example.com, phone: 555-1234"

# Search — first match anywhere
m = re.search(r"\\w+@\\w+\\.\\w+", text)
m.group()  # "alice@example.com"

# Find all — every match as list
re.findall(r"\\d+", text)  # ["555", "1234"]

# Match — must match at START (often use re.search instead)
re.match(r"\\d+", text)    # None (text doesn't start with digit)

# Full match — entire string must match
re.fullmatch(r"\\d+", "123")  # match object

# Substitution
re.sub(r"\\d+", "XXX", text)  # "My email: alice@example.com, phone: XXX-XXXX"

# Split
re.split(r"[,: ]+", text)  # ["My", "email", "alice@example.com", "phone", "555-1234"]

# Compile for reuse
pat = re.compile(r"\\b\\w+@\\w+\\.\\w+\\b")
pat.findall(text)

# ── COMMON PATTERNS ──
# \\d       digit (0-9)
# \\w       word char (letter, digit, underscore)
# \\s       whitespace (space, tab, newline)
# .         any char except newline
# +         one or more
# *         zero or more
# ?         optional (zero or one)
# {3,5}     between 3 and 5
# ^         start of string
# $         end of string
# \\b       word boundary
# [abc]     any of a, b, c
# [^abc]    NOT a, b, c
# |         OR
# (...)     capture group
# (?:...)   non-capturing group
# (?=...)   lookahead
# (?!...)   negative lookahead

# ── FLAGS ──
# re.IGNORECASE / re.I     case insensitive
# re.MULTILINE / re.M     ^$ match line boundaries
# re.DOTALL / re.S         . matches newlines too
# re.VERBOSE / re.X        allow spaces and comments in pattern

# ── COMPLETE EXAMPLES ──
# Email:     r"\\b\\w+@\\w+\\.\\w+\\b"
# Phone:     r"\\b\\d{3}[-.]\\d{3}[-.]\\d{4}\\b"
# URL:       r"https?://\\w+(\\.\\w+)+"
# Date:      r"\\b\\d{4}-\\d{2}-\\d{2}\\b"
# Words:     r"\\b\\w+\\b"
# Hex color: r"#[0-9a-fA-F]{6}\\b"`);
_('magic methods', 'concept', '__method__()', 'Magic (dunder) methods let you define behavior for built-in operations like len(), str(), +, [], and iteration.', `class MyClass:
    def __init__(self, x):     # constructor
        self.x = x
    def __str__(self):         # str(obj) / print(obj)
        return f"MyClass({self.x})"
    def __repr__(self):        # repr(obj) / debugging
        return f"MyClass({self.x})"
    def __len__(self):         # len(obj)
        return self.x
    def __getitem__(self, i):  # obj[i]
        return self.x * i
    def __add__(self, other):  # obj + other
        return MyClass(self.x + other.x)

obj = MyClass(5)
print(obj)        # MyClass(5)  (via __str__)
len(obj)          # 5           (via __len__)`);
_('context managers', 'concept', 'with statement / __enter__ __exit__', 'Context managers auto-setup and auto-cleanup resources using the with statement. The most common use is file handling.', `with open("file.txt") as f:  # auto-closes on exit
    data = f.read()

# Custom context manager (class way):
class Managed:
    def __enter__(self):
        print("setup")
        return self
    def __exit__(self, *args):
        print("cleanup")

with Managed() as m:
    print("working")

# Custom (contextlib way):
from contextlib import contextmanager
@contextmanager
def managed():
    print("setup")
    yield
    print("cleanup")`);
_('iterators and iterables', 'concept', '__iter__ / __next__ / iter() / next()', 'An iterable has __iter__() returning an iterator. An iterator has __next__() returning items one at a time, raising StopIteration when done.', `# Most collections are iterable:
for x in [1, 2, 3]: ...
it = iter([1, 2, 3])  # get iterator
next(it)  # 1
next(it)  # 2

# Custom iterator:
class Count:
    def __init__(self, n):
        self.i, self.n = 0, n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1
        return self.i

for x in Count(3): print(x)  # 1 2 3`);
_('PEP 8 style', 'concept', 'PEP 8', 'PEP 8 is Python\'s official style guide. Key rules: 4 spaces per indent, 79-char line limit, snake_case for functions/vars, CamelCase for classes, two blank lines around top-level defs.', `# Good
def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

class ShoppingCart:
    pass`);
_('docstrings', 'concept', '""" """', 'Docstrings document modules, classes, functions, and methods. Enclosed in triple quotes. Access via help() or .__doc__.', `def add(a, b):
    """Add two numbers and return the result."""
    return a + b

help(add)         # shows docstring
print(add.__doc__) # "Add two numbers and return the result."`);
_('collections module', 'concept', 'defaultdict / Counter / deque / namedtuple', 'The collections module provides specialized container data types beyond list, dict, set.', `from collections import defaultdict, Counter, deque, namedtuple

# defaultdict — auto-defaults missing keys
d = defaultdict(int)
d["count"] += 1  # no KeyError, auto-starts at 0

# Counter — count hashable items
Counter("abbccc")  # {"a": 1, "b": 2, "c": 3}

# deque — double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)  # [0, 1, 2, 3]
dq.pop()          # 3

# namedtuple — lightweight class
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x   # 10
p[0]  # 10`);
_('shallow vs deep copy', 'concept', 'copy.copy() / copy.deepcopy()', 'A shallow copy copies the outer object but shares nested objects. A deep copy recursively copies everything. Use copy module.', `import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 99  # also changes original[0][0]!
deep[0][0] = 99     # does NOT change original

# List slicing [:] creates a shallow copy
nums = [1, 2, 3]
nums[:]   # shallow copy of list`);
_('property decorator', 'concept', '@property', '@property turns a method into a computed/read-only attribute. With setter/deleter, you can add validation on attribute access.', `class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):  # computed — no setter needed
        return 3.14 * self._radius ** 2

c = Circle(5)
c.radius = 10  # uses setter (with validation)
print(c.area)  # computed on access`);
_('instance vs class vs static methods', 'concept', 'instance method / @classmethod / @staticmethod', 'Instance methods receive self (the instance). Class methods receive cls (the class). Static methods receive neither — they are just functions in the class namespace.', `class MyClass:
    def instance_method(self):
        return f"called on {self}"

    @classmethod
    def class_method(cls):
        return f"called on {cls}"

    @staticmethod
    def static_method(x):
        return x * 2

obj = MyClass()
obj.instance_method()   # receives obj as self
MyClass.class_method() # receives MyClass as cls
MyClass.static_method(5) # no self/cls`);
_('GIL', 'concept', 'Global Interpreter Lock', 'The GIL is a mutex in CPython that lets only one thread execute Python bytecode at a time. It makes CPU-bound multithreading ineffective but I/O-bound threading works fine. For true parallelism, use multiprocessing.', `# I/O-bound: threads OK (waiting for network/disk)
# CPU-bound: use multiprocessing
from multiprocessing import Process

def worker(n):
    total = sum(range(n))

p = Process(target=worker, args=(10**7,))
p.start()
p.join()`);
_('pathlib', 'concept', 'Path / pathlib module', 'pathlib provides an object-oriented way to handle filesystem paths instead of string manipulation. Use Path() for paths.', `from pathlib import Path

p = Path("/home/user/file.txt")
p.name        # "file.txt"
p.stem        # "file"
p.suffix      # ".txt"
p.parent      # /home/user
p.exists()    # True/False
p.is_file()   # True/False

write: Path("out.txt").write_text("hello")
read:  Path("data.txt").read_text()

# Glob files
for py in Path(".").glob("*.py"):
    print(py)`);
_('enum', 'concept', 'Enum / IntEnum', 'Enum creates a set of symbolic named constants with auto-assigned values. More readable than plain strings or integers for fixed choices.', `from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

Color.RED        # <Color.RED: 1>
Color.RED.name   # "RED"
Color.RED.value  # 1

# Iteration:
for c in Color:
    print(c.name, c.value)

# Comparison:
Color.RED is Color.RED  # True
Color.RED == Color.RED  # True`);
_('duck typing and EAFP', 'concept', '"If it walks like a duck..."', 'Python uses duck typing: an object\'s behavior matters more than its type. "If it walks like a duck and quacks like a duck, it is a duck." EAFP (Easier to Ask Forgiveness than Permission) means try/except instead of checking types upfront.', `# Duck typing — any object with .speak() works
def make_sound(animal):
    animal.speak()  # don't care what type, just call it

class Dog:
    def speak(self): print("woof")

class Cat:
    def speak(self): print("meow")

make_sound(Dog())  # woof
make_sound(Cat())  # meow

# EAFP — try first, ask forgiveness later
try:
    result = obj.method()
except AttributeError:
    result = default

# vs LBYL (Look Before You Leap) — not idiomatic
if hasattr(obj, "method"):
    result = obj.method()`);
_('match statement', 'concept', 'match / case', 'Structural pattern matching (Python 3.10+). Matches values against patterns — more powerful than if/elif chains. Supports literals, types, guards, and unpacking.', `def process(value):
    match value:
        case 0:
            print("zero")
        case 1 | 2:
            print("one or two")
        case int(n) if n > 0:
            print(f"positive int: {n}")
        case (x, y):
            print(f"tuple: {x}, {y}")
        case {"name": n, "age": a}:
            print(f"{n} is {a}")
        case _:
            print("something else")`);
_('type hints deep', 'concept', 'type annotations', 'Type hints annotate function signatures and variables. They are NOT enforced at runtime — they help editors and tools catch bugs. Python 3.5+ with typing module, many built-ins in 3.10+.', `from typing import Optional, Union, Callable, Any

# Basic
def greet(name: str) -> str:
    return f"Hello {name}"

# Optional = value or None
def find(id: int) -> Optional[str]: ...

# Union = one of multiple types (use | in 3.10+)
x: int | str = 5   # Python 3.10+

# Callable
def run(f: Callable[[int], str], x: int) -> str:
    return f(x)

# Generic
def first[T](items: list[T]) -> T:  # Python 3.12+
    return items[0]`);

// ── PUBLIC API ─────────────────────────────────────────────────────────────

/** All string method names, alphabetical */
export const allStringMethods = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'str').map(e => e.name).sort();

/** All list method names, alphabetical */
export const allListMethods = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'list').map(e => e.name).sort();

/** All dict method names, alphabetical */
export const allDictMethods = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'dict').map(e => e.name).sort();

/** All set method names, alphabetical */
export const allSetMethods = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'set').map(e => e.name).sort();

/** All tuple method names, alphabetical */
export const allTupleMethods = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'tuple').map(e => e.name).sort();

/** All built-in function names, alphabetical */
export const allBuiltins = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'builtin').map(e => e.name).sort();

/** All method names across ALL types, alphabetical (deduplicated) */
export const allMethodsFlat = (): string[] => {
  const names = new Set<string>();
  for (const e of allReferenceEntries()) {
    if (e.type !== 'builtin' && e.type !== 'keyword' && e.type !== 'concept') {
      names.add(e.name);
    }
  }
  return Array.from(names).sort();
};

/** All keyword names, alphabetical */
export const allKeywords = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'keyword').map(e => e.name).sort();

/** All concept names, alphabetical */
export const allConcepts = (): string[] =>
  allReferenceEntries().filter(e => e.type === 'concept').map(e => e.name).sort();

/** Look up a single term (method name, built-in name, or concept). */
export const lookup = (name: string, preferredType?: string): RefEntry | undefined => {
  const clean = name.toLowerCase().replace(/[^a-z0-9_]/g, '');
  // Remove leading type prefix like "str." or "list." before lookup
  const withoutPrefix = clean.replace(/^(str|list|dict|set|tuple|int|float|bool)\./, '');
  const entries = _ref[clean] || _ref[withoutPrefix] || [];
  return (preferredType ? entries.find(entry => entry.type === preferredType) : undefined) || entries[0];
};

/** Format a single entry as human-readable text */
export const formatEntry = (entry: RefEntry): string => {
  const lines = [
    `\`${entry.signature}\``,
    '',
    entry.desc,
    '',
    '```python',
    entry.example,
    '```',
  ];
  return lines.join('\n');
};

/** Format all entries of a given type as a numbered list */
export const formatAllOfType = (type: string): string => {
  const entries = allReferenceEntries().filter(e => e.type === type).sort((a, b) => a.name.localeCompare(b.name));
  return entries.map((e, i) => `${i + 1}. \`${e.name}\` — ${e.desc}`).join('\n');
};

const mutationRuleAnswer = (): string => [
  '**Methods vs built-in functions: mutating rule**',
  '',
  '1. Core rule',
  'Methods that modify an existing mutable object usually return `None`.',
  '',
  'Examples: `list.append()`, `list.extend()`, `list.sort()`, `list.reverse()`, `dict.update()`, `set.add()`.',
  '',
  'They change the original object instead of creating and returning a new one. Python does this to make mutation obvious.',
  '',
  '```python',
  'numbers = [1, 2, 3]',
  'result = numbers.reverse()',
  '',
  'print(numbers)  # [3, 2, 1]',
  'print(result)   # None',
  '```',
  '',
  '2. `reverse()` vs `reversed()`',
  '| Tool | Kind | Original changed? | Return value |',
  '|---|---|---:|---|',
  '| `list.reverse()` | list method | Yes | `None` |',
  '| `reversed(iterable)` | built-in function | No | reverse iterator |',
  '',
  '```python',
  'numbers = [1, 2, 3]',
  'numbers.reverse()',
  'print(numbers)  # [3, 2, 1]',
  '',
  'numbers = [1, 2, 3]',
  'it = reversed(numbers)',
  'print(numbers)       # [1, 2, 3]',
  'print(list(it))      # [3, 2, 1]',
  '```',
  '',
  '3. `sort()` vs `sorted()`',
  '| Tool | Kind | Original changed? | Return value |',
  '|---|---|---:|---|',
  '| `list.sort()` | list method | Yes | `None` |',
  '| `sorted(iterable)` | built-in function | No | new sorted list |',
  '',
  '```python',
  'numbers = [3, 1, 2]',
  'new_list = sorted(numbers)',
  'print(new_list)  # [1, 2, 3]',
  'print(numbers)   # [3, 1, 2]',
  '',
  'numbers.sort()',
  'print(numbers)   # [1, 2, 3]',
  '```',
  '',
  '4. What is an iterator?',
  'An iterator produces one value at a time. `reversed(numbers)` does not immediately make a full list; use `list(reversed(numbers))` if you want the full reversed list.',
  '',
  '```python',
  'it = reversed([10, 20, 30])',
  'print(next(it))  # 30',
  'print(next(it))  # 20',
  'print(next(it))  # 10',
  '```',
  '',
  '5. Practical rule',
  'Use the method when you want to change the original object. Use the built-in function when you want a new result and want to keep the original unchanged.',
].join('\n');

const buildMutationComparisonAnswer = (question: string): string | null => {
  const q = question.toLowerCase();
  const asksMutatingReturnNone = /\b(return|returns|why|none)\b/.test(q) &&
    /\b(append|extend|insert|remove|clear|sort|reverse|update|add|discard|difference_update|intersection_update|symmetric_difference_update)\s*\(/.test(q);
  const asksSortSorted = /\bsort\s*\(\)|\bsorted\s*\(/.test(q) && /\b(difference|different|vs|versus|compare|return|none|original|change|method|built.?in)\b/.test(q);
  const asksReverseReversed = /\breverse\s*\(\)|\breversed\s*\(/.test(q) && /\b(difference|different|vs|versus|compare|return|none|iterator|original|change|method|built.?in)\b/.test(q);
  const asksMethodBuiltinMutation = /\bmethod\b.*\bbuilt.?in\b|\bbuilt.?in\b.*\bmethod\b|\bmodify|mutat|in.?place\b/.test(q) &&
    /\b(return none|none|sort|sorted|reverse|reversed|append|update|add)\b/.test(q);

  if (asksMutatingReturnNone || asksSortSorted || asksReverseReversed || asksMethodBuiltinMutation) {
    return mutationRuleAnswer();
  }

  return null;
};

/** Build a full reference answer for a general Python question */
export const answerGeneralPythonQuestion = (question: string): string | null => {
  const q = question.toLowerCase().trim();
  const preferredMethodType = /\b(?:string|str)\b/.test(q) ? 'str'
    : /\blist\b/.test(q) ? 'list'
      : /\b(?:dict|dictionary)\b/.test(q) ? 'dict'
        : /\bset\b/.test(q) ? 'set'
          : /\btuple\b/.test(q) ? 'tuple'
            : undefined;

  const mutationAnswer = buildMutationComparisonAnswer(question);
  if (mutationAnswer) return mutationAnswer;

  // ── Bare word / short phrase lookup (concept library first) ──────────
  const wordCount = q.split(/\s+/).length;
  if (wordCount <= 4) {
    // Concept library takes priority for bare-word definitions
    const bareConcept = lookupConcept(q);
    if (bareConcept.source === 'entry' && bareConcept.entry) {
      const e = bareConcept.entry;
      return `**${e.name}**\n\n🔹 **Easy:** ${e.easy}\n\n🔹 **Intermediate:** ${e.intermediate}\n\n🔹 **Advanced:** ${e.advanced}${e.examples.length ? `\n\n**Examples:**\n${e.examples.map(ex => `\`\`\`python\n${ex.code}\n\`\`\``).join('\n')}` : ''}${e.commonMistakes.length ? `\n\n**Common Mistakes:**\n${e.commonMistakes.map(m => `• ${m}`).join('\n')}` : ''}${e.related.length ? `\n\n**Related:** ${e.related.map(r => `\`${r}\``).join(', ')}` : ''}`;
    }
    if (bareConcept.source === 'category') {
      return `**${q}**\n\n${bareConcept.categoryFallback.intermediate}\n\n**Deep Dive:**\n${bareConcept.categoryFallback.advanced}`;
    }
    // Fall back to method/builtin reference
    const bareEntry = lookup(q, preferredMethodType);
    if (bareEntry) {
      let label = bareEntry.type.charAt(0).toUpperCase() + bareEntry.type.slice(1);
      if (bareEntry.type === 'builtin') label = 'Built-in function';
      return `**${label}: \`${bareEntry.name}()\`**\n\n${bareEntry.desc}\n\n\`\`\`python\n${bareEntry.example}\n\`\`\``;
    }
  }

  // ── Listing all methods ──────────────────────────────────────────────
  if (/(?:^|\b)(?:list|show|get|give)\s+(?:me\s+)?(?:all\s+)?(?:python\s+)?methods?\b|\ball\s+(?:python\s+)?methods?\b|methods?.*\blist\b/i.test(q) && !/\blist\b.*\bdata\b|\bwhat\b.*\blist\b|\bhow\b.*\blist\b/i.test(q)) {
    return 'Here are all Python methods (grouped by type):\n\n' +
      '**String methods (47):**\n' + allStringMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\n**List methods (11):**\n' + allListMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\n**Dict methods (11):**\n' + allDictMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\n**Set methods (17):**\n' + allSetMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\n**Tuple methods (2):**\n' + allTupleMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\nAsk me about any individual method for details!';
  }

  // ── Listing string methods ───────────────────────────────────────────
  if (/(?:list|show|all).*string.*method|string.*method.*(?:list|all)/i.test(q)) {
    return '**String methods (47 total):**\n' +
      allStringMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\nAsk about a specific method like `upper()`, `split()`, or `replace()` for details.';
  }

  // ── Listing list methods ─────────────────────────────────────────────
  if (/(?:list|show|all).*\blist\b.*method|\blist\b.*method.*(?:list|all)/i.test(q) && /\bmethod\b/i.test(q)) {
    return '**List methods (11 total):**\n' +
      allListMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\nAsk about a specific method like `append()`, `pop()`, or `sort()` for details.';
  }

  // ── Listing dict methods ─────────────────────────────────────────────
  if (/(?:list|show|all).*dict(?:ionary)?.*method|dict(?:ionary)?.*method/i.test(q)) {
    return '**Dictionary methods (11 total):**\n' +
      allDictMethods().map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\nAsk about a specific method like `get()`, `keys()`, or `items()` for details.';
  }

  // ── Listing built-in functions ───────────────────────────────────────
  if (/(?:list|show|how many|all).*built.?in.*(?:func|method)|built.?in.*(?:list|all|func)/i.test(q)) {
    const names = allBuiltins();
    return `**Python built-in functions (${names.length} total):**\n` +
      names.map((n, i) => `${i + 1}. \`${n}()\``).join('\n') +
      '\n\nAsk about a specific built-in for details!';
  }

  // ── Listing keywords ─────────────────────────────────────────────────
  if (/(?:list|show|how many|all).*keyword|keyword.*(?:list|all)/i.test(q)) {
    const keywords = allKeywords();
    return `**Python keywords (${keywords.length} total):**\n` +
      keywords.map((n, i) => `${i + 1}. \`${n}\``).join('\n') +
      '\n\nAsk about any keyword for details!';
  }

  // ── Listing concepts ─────────────────────────────────────────────────
  if (/what concepts|list concepts|all concepts|concepts (?:you|can).*explain/i.test(q)) {
    return '**Python concepts I can explain:**\n' +
      allConcepts().map((n, i) => `${i + 1}. ${n}`).join('\n') +
      '\n\nAsk me to explain any of these!';
  }

  // ── What does X do / explain X ──────────────────────────────────────
  const normalizedNameQ = q
    .replace(/\bwhat'?s\b/gi, 'what is')
    .replace(/\bhow'?s\b/gi, 'how is')
    .replace(/\bwhere'?s\b/gi, 'where is');
  const typedMethodMatch = normalizedNameQ.match(/\b(string|str|list|dict|dictionary|set|tuple)\s+([a-z_][a-z0-9_]*)\s*(?:\(\))?\s+method\b/i);
  if (typedMethodMatch) {
    const type = typedMethodMatch[1].toLowerCase().replace('string', 'str').replace('dictionary', 'dict');
    const entry = lookup(typedMethodMatch[2], type);
    if (entry) {
      return `**${type} method: \`${entry.signature}\`**\n\n${entry.desc}\n\n\`\`\`python\n${entry.example}\n\`\`\``;
    }
  }
  const nameMatch = normalizedNameQ.match(/(?:what|how|explain|tell me about|describe)\s+(?:is|does|about|a|the)?\s*(?:a |an |the |a |an )?(\w+(?:\(\))?)\s*(?:method|function|keyword|built.in)?\s*(?:do|work|mean)?/i);
  if (nameMatch) {
    const rawName = nameMatch[1].replace(/[()]/g, '').toLowerCase();
    const dataTypeConcept = allReferenceEntries().find(e =>
      e.type === 'concept' && e.name.toLowerCase() === `${rawName} data type`
    );
    if (dataTypeConcept && /\b(?:data type|list|dict(?:ionary)?|tuple|set|string)\b/i.test(normalizedNameQ)) {
      return `**${dataTypeConcept.name}**\n\n${dataTypeConcept.desc}\n\n\`\`\`python\n${dataTypeConcept.example}\n\`\`\``;
    }
    // Concept library takes priority for definitions
    const cl2 = lookupConcept(rawName);
    if (cl2.source === 'entry' && cl2.entry) {
      const e = cl2.entry;
      return `**${e.name}**\n\n🔹 **Easy:** ${e.easy}\n\n🔹 **Intermediate:** ${e.intermediate}\n\n🔹 **Advanced:** ${e.advanced}${e.examples.length ? `\n\n**Examples:**\n${e.examples.map(ex => `\`\`\`python\n${ex.code}\n\`\`\``).join('\n')}` : ''}${e.commonMistakes.length ? `\n\n**Common Mistakes:**\n${e.commonMistakes.map(m => `• ${m}`).join('\n')}` : ''}`;
    }
    if (cl2.source === 'category') {
      return `**${rawName}**\n\n${cl2.categoryFallback.intermediate}\n\n**Deep Dive:**\n${cl2.categoryFallback.advanced}`;
    }
    // Fall back to method/builtin reference
    const entry = lookup(rawName, preferredMethodType);
    if (entry) {
      let label = entry.type.charAt(0).toUpperCase() + entry.type.slice(1);
      if (entry.type === 'builtin') label = 'Built-in function';
      return `**${label}: \`${entry.name}()\`**\n\n${entry.desc}\n\n\`\`\`python\n${entry.example}\n\`\`\``;
    }
  }

  // ── Direct "what is X" lookup ───────────────────────────────────────
  const simpleQ = q.replace(/what'?s\b/gi, 'what is');
  const simpleMatch = simpleQ.match(/what (is|are)\s*(a |an |the )?(\w[\w ]{0,30}?\w|\w)/i);
  if (simpleMatch) {
    let rawName = simpleMatch[3].toLowerCase().trim().replace(/\s+/g, ' ').replace(/^(a |an |the )/i, '');
    // Concept library takes priority
    const cl = lookupConcept(rawName);
    if (cl.source === 'entry' && cl.entry) {
      const e = cl.entry;
      return `**${e.name}**\n\n🔹 **Easy:** ${e.easy}\n\n🔹 **Intermediate:** ${e.intermediate}\n\n🔹 **Advanced:** ${e.advanced}${e.examples.length ? `\n\n**Examples:**\n${e.examples.map(ex => `\`\`\`python\n${ex.code}\n\`\`\``).join('\n')}` : ''}${e.commonMistakes.length ? `\n\n**Common Mistakes:**\n${e.commonMistakes.map(m => `• ${m}`).join('\n')}` : ''}`;
    }
    if (cl.source === 'category') {
      return `**${rawName}**\n\n${cl.categoryFallback.intermediate}\n\n**Deep Dive:**\n${cl.categoryFallback.advanced}`;
    }
    // Then try reference entries
    const conceptEntry = allReferenceEntries().find(e => {
      if (e.type !== 'concept') return false;
      const normalized = e.name.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/\s+/g, ' ');
      return normalized === rawName || normalized === rawName + ' data type';
    });
    if (conceptEntry) {
      return `**${conceptEntry.name}**\n\n${conceptEntry.desc}\n\n\`\`\`python\n${conceptEntry.example}\n\`\`\``;
    }
    // Then try method/builtin lookup
    const entry = lookup(rawName, preferredMethodType);
    if (entry) {
      let label = entry.type.charAt(0).toUpperCase() + entry.type.slice(1);
      if (entry.type === 'builtin') label = 'Built-in function';
      return `**${label}: \`${entry.name}\`**\n\n${entry.desc}\n\n\`\`\`python\n${entry.example}\n\`\`\``;
    }
  }

  // ── Concept matching ─────────────────────────────────────────────────
  for (const e of allReferenceEntries()) {
    if (e.type !== 'concept') continue;
    const normalizedConceptName = e.name.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/\s+/g, ' ').trim();
    const patterns: RegExp[] = normalizedConceptName
      ? [new RegExp(`\\b${normalizedConceptName.replace(/ /g, '\\s*')}\\b`, 'i')]
      : [];
    // Special case aliases
    if (e.name === 'return vs print') patterns.push(/return.*print|print.*return|difference between return and print|what.+(?:return|print).+do/i);
    if (e.name === 'function') patterns.push(/what.*function|define.*function|def statement|function.*argument|function.*parameter|how.*function.*work/i);
    if (e.name === 'module') patterns.push(/what.*module|import.*module|module.*import|python.*module|\.py file.*import/i);
    if (e.name === 'library') patterns.push(/what.*library|standard library|third.?party library|library.*module|module.*library|package.*library/i);
    if (e.name === 'object-oriented programming') patterns.push(/oop|object.oriented|object orientated|class.*object|what.*object|what.*class|class.*blueprint|instance.*object/i);
    if (e.name === 'attribute') patterns.push(/what.*attribute|object attribute|dot notation|instance variable|self\.[a-z_]+/i);
    if (e.name === 'lambda expression') patterns.push(/lambda.*order|lambda.*operation|lambda.*work|anonymous function|lambda expression|what.*lambda|explain.*lambda/i);
    if (e.name === 'method vs function') patterns.push(/what.*method|method.*belong|method.*object|function.*method|method.*function/i);
    if (e.name === 'list vs dict') patterns.push(/list.*dict|dict.*list|difference between list and dict/i);
    if (e.name === 'condition (if/else)') patterns.push(/what.*(?:if|else|condition|conditional)|explain.*(?:if|else|condition|conditional)|how.*(?:if|else|condition|conditional).*work|if.*statement|elif|else.*statement/i);
    if (e.name === 'for loop') patterns.push(/what.*for loop|how.*for loop|explain.*for loop|tell me.*for loop|for.*loop.*work|for.*loop.*example|what.*loop/i);
    if (e.name === 'while loop') patterns.push(/what.*while loop|how.*while loop|explain.*while loop|tell me.*while loop|while.*loop.*work|while.*loop.*example|infinite.*loop/i);
    if (e.name === 'for loop vs while loop') patterns.push(/for.*while|while.*for|difference between for and while/i);
    if (e.name === 'slicing') patterns.push(/inclusive.*exclusive|exclusive.*inclusive|start.*stop.*step|indexing.*slicing/i);
    if (e.name === 'comprehension') patterns.push(/list comp|dict comp|set comp|generator expression|list comprehension/i);
    if (e.name === 'exception handling') patterns.push(/try.*except|catch.*error|handle.*exception|raise.*error/i);
    if (e.name === 'f-string') patterns.push(/f.string|format.*string|string.*format.*f/i);
    if (e.name === 'args and kwargs') patterns.push(/args|kwargs|variable.*argument|keyword.*argument|arbitrary.*argument/i);
    if (e.name === 'unpacking') patterns.push(/unpack|splat|\* operator|spread operator/i);
    if (e.name === 'file I/O') patterns.push(/file.*(read|write|open)|read.*file|write.*file|with.*open/i);
    if (e.name === 'JSON') patterns.push(/json|serialize|deserialize|json\.(dumps|loads)/i);
    if (e.name === 'regular expressions') patterns.push(/regex|regular expression|re\.|pattern.*match|findall|search.*string/i);
    if (e.name === 'datetime') patterns.push(/datetime|date.*time|timedelta|strftime|date.*format/i);
    if (e.name === 'magic methods') patterns.push(/magic.*method|dunder|__.*__|special.*method/i);
    if (e.name === 'context managers') patterns.push(/context.*manager|with.*statement|__enter__|__exit__|auto.*clean|auto.*close/i);
    if (e.name === 'iterators and iterables') patterns.push(/iterator|iterable|__iter__|__next__|StopIteration/i);
    if (e.name === 'PEP 8 style') patterns.push(/pep.?8|style.*guide|coding.*style|python.*style/i);
    if (e.name === 'docstrings') patterns.push(/docstring|document.*string|__doc__|help.*function|triple.*quote/i);
    if (e.name === 'collections module') patterns.push(/defaultdict|Counter|deque|namedtuple|collections.*module/i);
    if (e.name === 'closure') patterns.push(/nested.*function|inner.*function|function.*inside.*function|enclosing.*scope|remember.*variable/i);
    if (e.name === 'shallow vs deep copy') patterns.push(/shallow.*copy|deep.*copy|copy\.(copy|deepcopy)|copy.*module/i);
    if (e.name === 'property decorator') patterns.push(/@property|property.*decorator|getter|setter|computed.*attribute/i);
    if (e.name === 'instance vs class vs static methods') patterns.push(/classmethod|staticmethod|@classmethod|@staticmethod|instance.*method.*vs/i);
    if (e.name === 'GIL') patterns.push(/gil|global.*interpreter.*lock|thread.*limit|multiprocessing.*vs.*threading/i);
    if (e.name === 'pathlib') patterns.push(/pathlib|Path|filesystem.*path|file.*path/i);
    if (e.name === 'enum') patterns.push(/enum|Enum|IntEnum|named.*constant|auto\(\)/i);
    if (e.name === 'duck typing and EAFP') patterns.push(/duck.*typing|eafp|lbyl|ask.*forgiveness|look.*before.*leap/i);
    if (e.name === 'match statement') patterns.push(/match.*case|pattern.*match|structural.*pattern|switch.*statement/i);
    if (e.name === 'type hints deep') patterns.push(/type.*hint|type.*annot|typing.*module|optional.*type|union.*type|generic.*type/i);
    if (patterns.some(p => p.test(q))) {
      return `**${e.name}**\n\n${e.desc}\n\n\`\`\`python\n${e.example}\n\`\`\``;
    }
  }

  // ── Concept library catch-all ──────────────────────────────────────────
  // Strip common question prefixes and try each remaining word/phrase
  const cleaned = q
    .replace(/^(what|how|explain|tell me about|describe|define|what is|what are|what does|how does|how do|i don'?t understand|can you explain|give me|show me|what'?s|what does a|what is a|what is an|what is the)\s*/i, '')
    .replace(/^(a |an |the )/, '')
    .replace(/[?.!]+$/, '')
    .trim();
  const terms = [q, cleaned, ...cleaned.split(/\s+/)].filter(Boolean);
  for (const term of [...new Set(terms)]) {
    const cr = lookupConcept(term);
    if (cr.source !== 'none') {
      const name = cr.entry?.name ?? term;
      if (cr.entry) {
        const e = cr.entry;
        return `**${e.name}**\n\n🔹 **Easy:** ${e.easy}\n\n🔹 **Intermediate:** ${e.intermediate}\n\n🔹 **Advanced:** ${e.advanced}${e.examples.length ? `\n\n**Examples:**\n${e.examples.map(ex => `\`\`\`python\n${ex.code}\n\`\`\``).join('\n')}` : ''}${e.commonMistakes.length ? `\n\n**Common Mistakes:**\n${e.commonMistakes.map(m => `• ${m}`).join('\n')}` : ''}${e.related.length ? `\n\n**Related:** ${e.related.map(r => `\`${r}\``).join(', ')}` : ''}`;
      }
      if (cr.categoryFallback.found) {
        return `**${name}**\n\n${cr.categoryFallback.intermediate}\n\n**Deep Dive:**\n${cr.categoryFallback.advanced}`;
      }
    }
  }

  // ── No match — don't hallucinate ─────────────────────────────────────
  return null; // caller must handle "I don't know" message
};

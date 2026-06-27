# Script-Style Alternatives Generation — Summary

## What was done
- Generated **2 script-style alternatives** (Script approach + Direct approach) for **1,838 of 1,962** problems in `exercises.ts`.
- **3,676 new alternatives** inserted total.
- Script-style alts demonstrate how to **call/use** the function with concrete example values, as opposed to function-style alts which show different implementations.

## Approach
- **Primary**: Extract the first function with parameters, assign example values, call it, print result.
- **Fallback 1**: For class-based problems — instantiate the class and print the object.
- **Fallback 2**: For no-param interactive functions — replace `input()` calls with hardcoded values.
- Every inserted alternative validated with `ast.parse` before writing.

## Results

| Metric | Count |
|--------|-------|
| Problems processed | 1,962 |
| Script alts inserted | 3,676 |
| Problems with script alts | 1,838 (93.7%) |
| Failed (edge cases) | 143 (7.3%) |
| Missing IDs in file (gaps) | 19 |

## Remaining failures (143)
Mostly:
- Pure-script problems (no functions at all, just top-level loops/print)
- Interactive-only functions with complex `input()` logic
- Edge cases with odd formatting or unicode characters

## Files
- Generator: `gen_script_alts.py`
- Data file: `exercises.ts` (modified, 1.8M+)

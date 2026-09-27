# Calculator behavior contract

Use these decisions before writing tests. They describe the finished lab behavior, not guarantees about the starter.

## Accepted inputs

Numeric operands are Python int or float values, excluding bool. Strings, None, complex values and other unsupported types raise TypeError. Core checks use finite, modest-sized numbers; non-finite values, overflow and precision-sensitive production arithmetic are outside scope.

| Function | Required behavior | Examples / errors |
|---|---|---|
| add(a, b) | Numeric sum | add(2, 3) → 5; strings raise TypeError |
| subtract(a, b) | Numeric difference | subtract(2, 5) → -3 |
| multiply(a, b) | Numeric product | multiply(-2, 4) → -8 |
| divide(a, b) | Numeric quotient | divide(7, 2) → 3.5; zero divisor raises ValueError |
| power(a, b) | Numeric base, integer exponent | power(2, 3) → 8; exponent must be int excluding bool; noninteger type raises TypeError; negative exponent raises ValueError; exponent zero returns 1, including power(0, 0) |
| square_root(a) | Nonnegative real square root | square_root(9) → 3; zero → 0; negative input raises ValueError |
| calculate_stats(numbers) | Arithmetic mean of a nonempty list or tuple | [2, 4, 6] → 4; one value → itself; empty list/tuple raises ValueError; unsupported container or element type raises TypeError |

Validate argument types before value/domain rules. Error wording may vary; check the exception class rather than a specific sentence. Functions must not mutate supplied lists. Normal return types may be int or float when numerically equivalent; use approximate comparisons where floating-point rounding matters.

The name calculate_stats is inherited; this function only returns a mean. Renaming the public API or adding unrelated statistics is outside the core lab.

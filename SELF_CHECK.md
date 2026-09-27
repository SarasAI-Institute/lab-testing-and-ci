# Tests and CI self-check

- [ ] Successful cases for every public function match CONTRACT.md.
- [ ] Division by zero, negative square root, empty statistics and invalid types follow the documented exception contract.
- [ ] Booleans are rejected; exponent zero, negative exponents and noninteger exponent types are covered.
- [ ] Statistics handles a tuple and one-element collection and does not mutate the input list.
- [ ] At least one actual failing-test commit precedes its repair, and subsequent increments preserve the same process where behavior is missing.
- [ ] Existing correct behavior was preserved, including negative-square-root errors.
- [ ] Before/after checks show that my refactor preserved public behavior.
- [ ] The complete local suite passes and collects real tests; coverage output was inspected for missed behavior.
- [ ] GitHub Actions shows a real success, deliberate failure and recovery tied to my own commits.
- [ ] I can distinguish an automated check from an enforced merge gate.

If a test fails because its expectation contradicts CONTRACT.md, correct the test and explain why. If it exposes an implementation defect, fix the implementation. Do not weaken an assertion merely to turn the display green.

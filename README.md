# Module 4 mini-lab — Tests, Refactoring and CI

Use a small calculator to practice a repeatable red → green → refactor loop, then prove that your checks run in GitHub Actions. This is a toy numeric library, not a production finance tool.

## Your starting point

`calculator.py` contains some correct behavior and some behavior that does not meet [CONTRACT.md](CONTRACT.md). Tests and the CI workflow are your work. Do not assume every AI-reported issue is a real defect: negative square roots already raise ValueError in the starter.

## Local setup

Download **Code → Download ZIP** from this repository and extract it into a new folder, or clone it if you already use Git. Open that folder in your editor. Use Python 3.12 and Git, with the Codex or Claude Code setup you established in Module 1. No Codespaces, devcontainer or shared API key is needed.

From the lab folder, create and activate a virtual environment:

| Platform | Create | Activate |
|---|---|---|
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows PowerShell | `py -3.12 -m venv .venv` | `.venv\Scripts\Activate.ps1` |

All subsequent Python commands use `python` in that active environment. If you downloaded a ZIP, initialize a local Git repository and commit the supplied starter before working. If you cloned it, retain the starter commit. Commit small changes as you go.

Install the test tools:

```sh
python -m pip install -r requirements.txt
```

## Tasks

1. **Agree on the behavior.** Read CONTRACT.md. Run a few tiny probes. Distinguish a missing behavior from an already-correct behavior that needs a regression check. Running `python calculator.py` currently demonstrates a division-by-zero exception; that is part of the starting state.
2. **Write a meaningful failing test.** Add a test in `tests/test_calculator.py` for one unmet requirement. Run it, record why it failed and commit it before editing the implementation.
3. **Make that test pass.** Implement the smallest suitable change, run the whole suite and commit. Repeat for the remaining contract cases. Some new regression tests may pass immediately; record that honestly rather than manufacturing a failure.
4. **Refactor under protection.** Identify one concrete duplication or readability problem. Keep before/after passing results and confirm the public behavior remains unchanged.
5. **Run CI on your own repository.** Publish your working copy to a repository you own, following [CI_GUIDE.md](CI_GUIDE.md). Author a workflow that installs requirements and runs the suite on pushes and pull requests. Observe a real successful run, then a deliberate failure and recovery.
6. **Review.** Complete SELF_CHECK.md and REFLECTION.md. Explain one failing test, one repair and how you know CI actually ran.

Useful first prompt: “Compare this implementation with CONTRACT.md. List which behaviors need verification and propose one test that should fail for a specific unmet requirement. Do not modify the implementation yet.”

## Local verification

After you have written tests:

```sh
python -m pytest
python -m pytest --cov=calculator --cov-report=term-missing
```

The initial starter has no tests. A no-tests-collected result is not a passing suite. Aim to cover all named cases with meaningful assertions; there is no arbitrary minimum test count or coverage grade for this ungraded lab. PromptLab's own coverage requirement is separate.

Optional extension after the core: package the suite in a small Docker image and show that it runs from committed files. Docker is not needed to start this lab.

## Working with your coding assistant

Use either taught tool; this lab does not require two independent builds. Read the task yourself, supply relevant context, ask for one bounded step, inspect the diff and verify the result. Record a few real decisions in [REFLECTION.md](REFLECTION.md). Try an explanation or hypothesis before requesting implementation. Prompt examples are starting points to adapt, not answers to paste blindly.

This is **ungraded practice**. Keep your work and reflection; there is no submission, mandatory time limit or capstone credit. Apply the method separately to your ongoing PromptLab project. A working mini-lab does not replace capstone evidence.

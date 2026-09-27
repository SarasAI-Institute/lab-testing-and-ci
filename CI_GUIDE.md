# Prove the checks run in GitHub Actions

You need your own repository for hosted CI practice, but you do not submit it for grading. Keep your real local test-first history.

1. Create an empty repository in your account. If starting from a ZIP, initialize Git and commit locally before publishing. If you cloned the instructor starter, change your working copy's remote to your own repository's clone URL before pushing. Do not push to the instructor repository.
2. Author `.github/workflows/ci.yml` yourself. It should run on push and pull_request, check out the code, set up Python 3.12, install requirements.txt and execute `python -m pytest`. Ask your assistant to explain each action and permission it proposes. No API credentials or deployment secrets are needed.
3. Push and open your repository's Actions tab. Check that the run belongs to the commit you pushed and that it actually collected tests. Keep the successful run link.
4. On a temporary practice branch, deliberately change an assertion in a test that already runs so it expects a wrong result. Push, or open a pull request to your own main branch, and observe the failing run. Record the failed assertion and run link.
5. Restore the correct assertion in a new commit. Push and verify recovery. Preserve the history; do not merge intentionally broken code into your main branch.

A red Actions run demonstrates failed checks. It does **not** by itself prove GitHub blocks merging. Required checks and branch protection are separate repository settings, and availability depends on the repository/account arrangement. Investigate that separately if extending the lab; the PromptLab milestone covers the required merge gate.

If Actions is disabled or blocked by your account/organization, record the actual limitation and ask the instructor for the approved setup. Local pytest output is useful evidence of local behavior, but it is not a hosted CI run.

## Keep these references in your reflection

- Successful run and associated commit:
- Deliberate failed run and the assertion that failed:
- Recovery run and associated commit:
- What would stop a failing change from being merged in this repository, if anything?

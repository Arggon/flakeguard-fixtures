# FlakeGuard fixtures

Synthetic tests used to exercise the FlakeGuard action on a public repository.

- `test_injected_flake_by_run_parity` fails on odd workflow run numbers and passes on even
  ones, giving two runs of the same commit with different outcomes.
- `test_always_broken` always fails; the stable tests always pass; one test is skipped.
- The workflow uploads the JUnit XML artifact and runs the FlakeGuard action over the
  same-commit runs, then uploads the report.
- All data is synthetic. No secrets, customer data, or personal data. Artifacts are retained
  for one day.

Internal prototype. No support, no marketplace listing, no external users.

---
name: vtex-io-test
description: VTEX IO link validation workflow for app repositories. Use when users mention VTEX link errors, workspace checks, manifest/vendor mismatches, or ask to verify whether a VTEX app can be linked successfully.
---

# VTEX IO Test

Validate whether a VTEX IO app is ready to link in the current workspace.

## Workflow
1. Confirm repository root contains `manifest.json`.
2. Read `manifest.json` and note `vendor`, `name`, and builders used.
3. Run `vtex whoami` and verify:
   - Account/vendor context matches the app scope.
   - Current workspace is a development workspace (never `master`).
4. Run `vtex link` and inspect terminal output until completion.
5. Classify result:
   - Success: report linked app and workspace.
   - Warning only: report warnings and whether link completed.
   - Failure: report the first blocking error and likely fix path.

## Validation Rules
- Treat authentication/account mismatch as blocking.
- Treat linking in `master` as blocking.
- Distinguish non-blocking warnings from blocking errors.
- Include exact failing command and message snippet in the report.

## Response Standard
1. State pass/fail for link readiness.
2. List checks performed (`manifest`, `whoami`, `link`).
3. Provide next action (for example: switch workspace, login, fix manifest/vendor, retry link).

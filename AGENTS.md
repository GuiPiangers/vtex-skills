# Agent Instructions (VTEX IO Docs Repo)

## Scope

This repository is documentation for VTEX IO skills. Treat it as the source of truth for how to implement VTEX IO tasks.

## Required Reading Order

Before implementing anything, read:

1. `ARCHITECTURE.md`
2. `agents/vtex-specialist.md`
3. `skills/vtex-io-core/SKILL.md`

Then load only the specific guide files referenced by `skills/vtex-io-core/SKILL.md` that match the user request.

## Operating Rules

- VTEX-only scope: if the request is not related to VTEX IO / Store Framework / VTEX services, ask to re-scope.
- Prefer native VTEX blocks and patterns before proposing custom React/backend.
- Do not preload all docs; open files on-demand based on triggers.
- Keep edits minimal and production-safe; avoid unrelated refactors.
- When something is ambiguous, ask for account, workspace, target app(s), and impacted pages/blocks.


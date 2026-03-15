# VTEX IO Skills Documentation

This repository is a documentation and instruction set to help LLMs implement VTEX IO and Store Framework tasks consistently.

## Canonical Entry Points

When asked to build or change something, start here (in this order):

1. `ARCHITECTURE.md`
2. `agents/vtex-specialist.md`
3. `skills/vtex-io-core/SKILL.md` (then load only the referenced guides you need)

Skills live under `skills/<skill-name>/` and each skill defines its own loading protocol in `SKILL.md`.

## Tooling Support

This repo includes instruction files used by common editors/CLIs:

- Codex CLI: `AGENTS.md`
- Cursor: `.cursorrules`
- Gemini: `GEMINI.md`
- GitHub Copilot Chat: `.github/copilot-instructions.md`

If your tool does not auto-load these files, paste the "Canonical Entry Points" section into your system prompt and ask the model to open those files before coding.


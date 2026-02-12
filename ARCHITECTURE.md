# VTEX Agent Architecture

> Focused VTEX IO/Store Framework agent setup (VTEX-only scope)

---

## 📋 Overview

This repo is intentionally **VTEX-focused**. It keeps only:

- **1 Specialist Agent**: `vtex-specialist`
- **VTEX skills** for Store Framework, IO apps, and platform integrations
- **VTEX workflows** for common tasks (optional)

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          # This file
├── agents/                  # VTEX-only agent(s)
├── skills/                  # VTEX knowledge modules
├── workflows/               # VTEX slash commands (optional)
└── rules/                   # Global rules
```

---

## 🤖 Agents (1)

Specialist AI persona for VTEX.

| Agent             | Focus                                         | Skills Used                 |
| ----------------- | --------------------------------------------- | --------------------------- |
| `vtex-specialist` | VTEX IO, Store Framework, platform services   | vtex-io-core, clean-code    |

---

## 🧩 Skills

Only VTEX-relevant knowledge modules are kept.

### VTEX Core

| Skill         | Description |
| ------------- | ----------- |
| `vtex-io-core` | VTEX IO Store Framework, blocks, backend, styles |

### Quality (Optional)

| Skill        | Description |
| ------------ | ----------- |
| `clean-code` | General code quality guidelines |

---

## 🔄 Workflows (VTEX)

VTEX-focused slash commands (use only when it helps).

| Command          | Description              |
| ---------------- | ------------------------ |
| `/brainstorm`    | Socratic discovery       |
| `/create`        | Create new features      |
| `/debug`         | Debug issues             |
| `/deploy`        | Deploy application       |
| `/enhance`       | Improve existing code    |
| `/orchestrate`   | Multi-agent coordination |
| `/plan`          | Task breakdown           |
| `/preview`       | Preview changes          |
| `/status`        | Check project status     |
| `/test`          | Run tests                |
| `/ui-ux-pro-max` | Design with 50 styles    |

---

## 🎯 Skill Loading Protocol

```plaintext
User Request → VTEX scope check → Load `vtex-io-core` SKILL.md
                                         ↓
                                 Read referenced files
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata & instructions
├── references/        # (Optional) Templates, docs
└── assets/            # (Optional) Images, logos
```

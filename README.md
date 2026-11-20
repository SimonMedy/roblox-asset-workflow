# Roblox Asset Workflow

**A lightweight, open Agent Skill for creating beautiful, editable, game-ready Roblox 3D assets.**

Works with an agent that supports [Agent Skills](https://agentskills.io/specification), including **Claude Code, Codex, and Gemini CLI**. Supports workflows that use Blender, Blender MCP and Roblox Studio MCP **if you already have those tools installed**.

**Why:** Keep creative freedom while consistently shipping clean, reusable and optimizable geometry. No specific game, brand, art style or proprietary toolchain is assumed.

## Install from GitHub (Windows / macOS / Linux)

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

Use `-g` to install globally for your selected agents, or select agents explicitly:

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Node.js / npm are required for `npx`. The CLI asks you to choose agents and approves installation where required. This is a reusable **installation command**, not a command to run from inside the GitHub web page.

Alternatively for **Gemini CLI**:

```bash
gemini skills install https://github.com/SimonMedy/roblox-asset-workflow
```

To install into a Codex session through its built-in installer, ask `$skill-installer` to install the repository's skill. The cross-agent `npx skills` method is simplest for most users.

**Updates:** `npx skills update roblox-asset-workflow` (or `npx skills update -g` for all globally installed skills). Restart/reload an agent session if the skill does not appear.

### Just give the URL to your agent

> Install and use the Agent Skill at `https://github.com/SimonMedy/roblox-asset-workflow`. Review its `SKILL.md` and references first. If you can run commands, use `npx skills add SimonMedy/roblox-asset-workflow` and enable it; otherwise tell me what installation access is missing.

**An ordinary browser-only chat cannot necessarily install a skill or control Blender.** It needs compatible agent support and permissions.

## What it covers

| Area | Rules |
| --- | --- |
| Artistic freedom | Reference-faithful or fully original designs, without imposed styling |
| Asset quality | Close-up/orthographic inspection, clean shading, no unintended gaps |
| Editability | Editable `.blend` source, independent moving/swappable/recolorable parts and good pivots |
| Cosmetic-ready | UVs, tint masks, stable paint zones, full-body liveries, optionally animated skins |
| Roblox import | ≤20,000 triangles **per individual mesh**, hierarchy, maps, scale and import validation |
| Output profiles | **HQ** editable master, **GAME** standard export, optional **MOBILE** variation |
| Safety | Version snapshots, preserve accepted geometry, no silent physics/hitbox changes |
| Context efficiency | Compact `SKILL.md` + focused references loaded only as needed |

Being under the triangle cap does **not** prove an asset is optimized. Performance needs real Roblox profiling, especially on mobile and when many vehicles/objects appear at once. See the [Roblox general specifications](https://create.roblox.com/docs/art/modeling/specifications).

## Example prompts

**Create a vehicle**

> Use `roblox-asset-workflow` and Blender MCP. Model the attached car references as faithfully as possible. Keep the wheels independently editable, prepare clean UVs for full-body skins and retain a high-quality Blender master. Export a validated Roblox-ready version; compare all views, fix defects and report per-mesh triangle counts.

**Refine an existing model**

> Use `roblox-asset-workflow`. Lock the approved silhouette, correct the rear lamp fitment and panel gaps, inspect close-ups, preserve the previous version and deliver the next revision without redesign.

**Make an environment**

> Use `roblox-asset-workflow` to build a modular stylized arena in Blender. Design original architecture, verify seams and materials, keep cosmetic meshes separate from any existing gameplay collisions, and prepare Roblox exports.

## Repository layout

```text
roblox-asset-workflow/
├── SKILL.md                   # Core compact instructions and triggers
├── references/
│   ├── vehicles.md
│   ├── skins.md
│   ├── environments.md
│   ├── other-assets.md
│   └── roblox-export.md
├── scripts/
│   ├── audit_blender.py       # Optional modifier-aware mesh statistics
│   └── validate_skill.py     # Local package/links validation
├── docs/
│   └── PUBLISHING.md         # How to publish / update on GitHub
├── .github/workflows/
│   └── validate.yml          # GitHub Actions skill self-test
├── README.md
├── README_FR.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

## Verify the skill

```bash
python scripts/validate_skill.py
```

Optional Blender geometry stats:

```bash
blender -b your_asset.blend --python scripts/audit_blender.py -- --output audit.json
```

The Blender command requires Blender. The skill itself does not install Blender or any MCP. Its optional audit reads the scene; it does not upload or modify it.

## License and contributing

MIT licensed: reuse and adapt the **skill instructions/scripts**, even commercially. This license does **not** grant rights to third-party assets or model outputs you do not own.

Contributions welcome: fixes backed by Roblox documentation, clearer workflows, and validated Blender/Roblox examples. Please keep the core skill short and move specialized detail into `references/`.

See [PUBLISHING](docs/PUBLISHING.md) and [CHANGELOG](CHANGELOG.md).

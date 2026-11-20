# Roblox Asset Workflow

**An open Agent Skill for creating polished, editable Roblox 3D assets using Blender and optional Blender MCP integrations.**

[Guide français](README_FR.md) · [Agent Skills specification](https://agentskills.io/specification) · [Release history](CHANGELOG.md)

## Install

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

Globally in selected agents:

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Requires Node.js and a compatible agent. Blender, Blender MCP and Roblox Studio integrations are separate and optional. A browser chat alone cannot necessarily install skills or control Blender.

## What it does

- **Creative freedom and fidelity:** respect user references, preserve accepted designs, maintain editable masters.
- **Modularity:** separate swappable, paintable and animated pieces with useful pivots.
- **Cosmetics:** UVs, skin/paint masks, multiple colors and supportable effects.
- **Roblox handoff:** verify 20,000 triangles **per individual imported mesh**, not per whole asset; test actual imported result.
- **Profiles:** `HQ` Blender master, `GAME` Roblox export, optional `MOBILE` optimization.
- **QA:** inspect actual GAME geometry at export settings, macro/gameplay renders, optional internal magenta leak test for enclosed vehicles.
- **Safety:** versioned snapshots, retained scripts/textures, no silent physics changes.

## Validation and optional audits

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
blender -b your_asset.blend --python scripts/audit_blender.py -- --collection Vehicle_GAME --output asset-audit.json
python scripts/audit_glb.py path/to/Vehicle_GAME.glb --output glb-audit.json
```

`--collection` limits the Blender audit; hidden meshes are excluded unless `--include-hidden` is specified. Blender is required for the Blender audit only. Both audits are read-only and issue **warnings** about material splitting, UVs, non-unit scale and export risks. They do not replace actual Roblox Studio import, visual testing or profiling. An audit of a GLB is not an audit of a source `.blend` or an `.fbx` export.

## Skill structure

`SKILL.md` is the compact core. `references/` provides specialized, progressively loaded guidance for vehicles, skins, environments, other assets and Roblox export. Scripts live in `scripts/`; synthetic unit tests in `tests/`; GitHub Actions runs structure checks, Python compilation and tests.

## Examples

> Use `roblox-asset-workflow` and Blender MCP to model the attached vehicle references. Preserve wheel pivots and interchangeable pieces; inspect macro detail on the GAME export, check UVs/paint zones, validate the per-mesh triangle limit and report what was actually tested.

> Use `roblox-asset-workflow` to refine only my approved rear lights. Save a version before modifying geometry. Run the internal magenta leak test if the vehicle is enclosed, and do not modify established physics or hitboxes.

## License

MIT applies to these skill files and scripts, **not** third-party 3D models, brand marks or other assets without rights. See [LICENSE](LICENSE) and [publishing guide](docs/PUBLISHING.md). Contributions and documented fixes are welcome.

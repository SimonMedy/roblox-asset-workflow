# Roblox Asset Workflow

**An open Agent Skill for polished, editable Roblox assets** with Blender and optional Blender MCP / Roblox Studio integrations. Covers 3D, cosmetics, art direction, native VFX and SFX handoff. It is **not** yet a full-game coding/orchestration skill.

[Guide français](README_FR.md) · [Agent Skills specification](https://agentskills.io/specification) · [Release history](CHANGELOG.md)

## Install

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

Globally for selected agents:

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Requires Node.js and a compatible agent. Blender, Blender MCP and Roblox Studio integrations are **separate**, not installed by this skill.

## Capabilities

- **Art & fidelity:** original designs or user-reference fidelity, no unrequested redesign, editable snapshots.
- **3D delivery:** swappable parts/pivots, UV skins and textures, HQ master, GAME export and optional MOBILE variant.
- **Roblox geometry QA:** at most **20,000 triangles per individual standard imported mesh**; import and performance still require real validation.
- **Cosmetics:** static liveries and safely scriptable `SurfaceAppearance` emission, with accurate map-content security constraints.
- **Rarity & identity:** desirable Common items through distinct Mythic signatures; competitive match-camera readability over visual clutter.
- **Native VFX:** ParticleEmitter/flipbooks, Beam, Trail, MeshPart, emissive masks; inspect alpha and measure multi-client cost.
- **Audio planning:** original/licensed SFX layers, attack/loop/release, mix cues and Studio integration guidance.
- **Visual & gameplay gate:** `PASS` / `FAIL` / `UNVERIFIED` on applicable criteria, with honest test reporting.

## Progressive references

`SKILL.md` contains the compact contract and links to specialized files under `references/`. Only open the relevant references:

| Task | Reference |
| --- | --- |
| Vehicles and Blender finish | [vehicles.md](references/vehicles.md) |
| Skins, colors, emission | [skins.md](references/skins.md) |
| Cosmetic tiers and collections | [rarity-and-art-direction.md](references/rarity-and-art-direction.md) |
| Auras, boosts and flipbooks | [vfx-roblox.md](references/vfx-roblox.md) |
| SFX and music handoff | [audio-sfx.md](references/audio-sfx.md) |
| Environments and other props | [environments.md](references/environments.md), [other-assets.md](references/other-assets.md) |
| Roblox export and Pass/Fail | [roblox-export.md](references/roblox-export.md) |

## Verify and audit

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
blender -b your_asset.blend --python scripts/audit_blender.py -- --collection Vehicle_GAME --output asset-audit.json
python scripts/audit_glb.py path/to/Vehicle_GAME.glb --strict --output reports/glb-audit.json
```

`--collection` limits Blender audit; hidden objects are excluded by default (override with `--include-hidden`). The GLB preflight distinguishes blocking errors from review warnings. These audits are **read-only** and do not prove Roblox Studio appearance, networking or device performance.

## Example: one Voidstorm hero wheel

> Use `roblox-asset-workflow` to concept and build **one** Mythic Voidstorm wheel: distinct silhouette, restrained violet/black emissive detail, correct mount and UVs, gameplay-reactive Idle/Boost glow, and native Roblox VFX if relevant. Validate GAME import, close-up and match-camera readability, then report actual Studio/multiplayer/mobile tests before expanding the set. Do not change vehicle physics.

## License

MIT covers the skill files and scripts, **not third-party art, music or models**. See [LICENSE](LICENSE), [publishing guide](docs/PUBLISHING.md) and [changelog](CHANGELOG.md). Contributions with real asset/test evidence are welcome.

# Changelog

## 3.1.0 — 2026-11-20

- Added optional internal magenta vehicle leak test and explicit macro QA on the GAME export geometry.
- Recommended one material per customizable mesh, deliberate part splitting, UV0 within [0,1], and verification of imported hierarchy.
- Expanded glTF/Roblox pitfalls guidance for emission, axes, scale, UVs, primitives and extensions without imposing unverified importer behavior.
- Blender audit now supports `--collection` and `--include-hidden`, skips hidden objects by default, and warns about scale, multi-material and UV bounds.
- Added dependency-free `.glb` preflight audit plus synthetic unit tests; CI now runs them.
- Documented asset/version/export directory conventions for safe non-destructive work.

## 3.0.0 — 2026-11-20

- Repackaged as a standalone GitHub-ready Agent Skill with cross-agent install instructions.
- Preserved compact, creative-first core rules and optional progressive references.
- Added reusable vehicle, skins, environment and other-assets guidance.
- Clarified Roblox's **per-mesh** 20k-triangle limit and the distinction between HQ / GAME / optional MOBILE.
- Included a Blender scene audit and a dependency-free skill structure validator.
- Added GitHub CI, French/English READMEs, publishing guide and MIT license.

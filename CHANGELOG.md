# Changelog

## 3.2.0 — 2026-11-22

- Added progressive references for **rarity/art direction**, native Roblox **VFX** and **audio/SFX**; retained the compact `SKILL.md` core and all previous vehicle/geometry rules.
- Clarified `SurfaceAppearance` emissive mask security (`PluginSecurity`) versus scriptable `EmissiveStrength`/`EmissiveTint`, ColorMap modulation and fixed versus moving patterns.
- Added 3D/particle/Beam/Trail VFX selection, RGBA/flipbook workflow, measured multiplayer/mobile performance guidance and a single-hero vertical slice.
- Added a concise export **Visual & gameplay Pass / Fail / Unverified** gate and updated English/French READMEs.
- No arbitrary particle/draw-call cap or guarantee of Blender/Studio results; Python audit scripts remain unchanged.

## 3.1.2 — 2026-11-21

- Added precise vehicle finishing guidance based on evaluated GAME Subsurf geometry, one-to-one seams and unexpected internal boundary checks.
- Added a six-zone macro inspection checklist for headlights, lips/rockers, wheel liners, vents, mirrors and diffuser/reflections.
- Clarified recessed boost/exhaust/intake cavities, cosmetic tilt baked into vertices and functional VFX mount orientations.
- Prevented false-positive magenta leak tests by keeping emitters inside liner/underfloor cavities.
- Added Blender MCP viewport cleanup after Cycles batch renders; `SKILL.md` and audit scripts are unchanged.

## 3.1.1 — 2026-11-20

- GLB audit automatically creates the destination directory when `--output` is nested.
- GLB preflight now separates `errors` from non-blocking `warnings`: `--strict` fails only for errors such as over-budget meshes, broken indices and missing local texture files.
- Scan node TRS scales and matrices for negative/mirrored or non-unit transforms; warn for Studio inspection rather than claiming automatic failure.
- Strengthened GLB index checking and added synthetic regression tests for CLI strict behavior, output folders, texture availability and transforms.
- The skill's artistic and quality rules are unchanged; actual Blender/Roblox Studio validation remains necessary.

## 3.1.0 — 2026-11-20

- Added optional internal magenta vehicle leak test and explicit macro QA on the GAME export geometry.
- Recommended one material per customizable mesh, deliberate part splitting, UV0 within [0,1], and verification of imported hierarchy.
- Expanded glTF/Roblox pitfalls guidance for emission, axes/scale, UVs, primitives and extensions without imposing unverified importer behavior.
- Blender audit now supports `--collection` and `--include-hidden`, skips hidden meshes by default, and warns for scale, multi-material and UV bounds.
- Added dependency-free `.glb` preflight audit plus synthetic unit tests; CI now runs them.
- Documented asset/version/export directory conventions for safe non-destructive work.

## 3.0.0 — 2026-11-20

- Repackaged as a standalone GitHub-ready Agent Skill with cross-agent install instructions.
- Preserved compact, creative-first core rules and optional progressive references.
- Added reusable vehicle, skins, environment and other-assets guidance.
- Clarified Roblox's **per-mesh** 20k-triangle limit and HQ/GAME/optional MOBILE.
- Included Blender scene audit, dependency-free skill validator, GitHub CI, FR/EN docs and MIT license.

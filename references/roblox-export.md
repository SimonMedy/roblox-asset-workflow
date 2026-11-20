# Roblox export and performance rules

Authoritative baseline: https://create.roblox.com/docs/art/modeling/specifications and https://create.roblox.com/docs/studio/importer . Refresh if Roblox changes importer requirements.

## Required checks

1. **20,000 triangles maximum per individual imported mesh**, not per full model; avatar/UGC assets may use lower category-specific limits. Count after evaluated modifiers / triangulation; deliberately optimize before import instead of relying on automatic simplification. Leave a practical margin.
2. Geometry: consistent axes, scale and origin; outward normals, no stray objects, stable naming, clean shading; check non-manifold *only where the form should be closed*.
3. Export: `.glb`/`.gltf`/`.fbx` as appropriate; include/apply textures or package external texture files; retain hierarchy and intentionally separate parts (avoid importer merge when swappable pieces matter).
4. Materials: confirm the Roblox implementation supports exported ColorMap, NormalMap, RoughnessMap, MetalnessMap and optional emission. Normal maps must use the convention Roblox supports. Blender procedural nodes may need baking.
5. Test **reimport** of the exported file, then Roblox Studio/client where accessible. Inspect transformed pivots, shading, UV continuity, paint masks and material appearance under game lighting.
6. Performance: record total triangles, max per mesh, number of mesh objects, materials, textures/resolutions and repeated-asset counts. Estimate draw calls only with appropriate tooling and **measure frame time in an actual representative scene**; triangle limits alone cannot guarantee FPS.

## Output profiles (do not generate unnecessary duplicates)

- `HQ`: non-destructive editable Blender master; high resolution/complexity as needed. Preserve modifiers, separate components, scripts and editable source textures. Not necessarily ready to import.
- `GAME`: production Roblox export under per-mesh limit; geometry/detail appropriate at actual gameplay distance. Preserve silhouette, UVs and named swappable regions; validate hierarchy and PBR maps.
- `MOBILE`: optional lower-cost variation where mobile or low-end devices warrant it. Optimize texture memory, material count, transparency and hidden faces as well as triangle count; do not assume fewer triangles automatically means good mobile performance. Keep roots, pivots and attachment coordinates compatible; document UV differences if any.

Roblox automatic mesh LOD is different from automatically switching between user-authored `GAME` and `MOBILE` files. Custom swapping needs host code, and may be unnecessary.

## Optional Blender audit

`blender -b PATH_TO_ASSET.blend --python scripts/audit_blender.py -- --output asset-audit.json`

Runs on objects in the active Blender scene, evaluates their current modifiers, and reports triangle counts/material slots/UV layers. It does **not** prove what the Roblox importer finally generates: verify the imported result and the effect of export settings.

Further docs:
- https://create.roblox.com/docs/onboarding/artists
- https://create.roblox.com/docs/art/modeling/surface-appearance

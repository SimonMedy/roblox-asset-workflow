# Skins, color customization, paint masks and animation

Prepare assets for future cosmetics **without requiring a complete customization system now**.

## In Blender

1. UV-unwrap paintable surfaces intentionally: consistent texel density, low-distortion patches, seams in less-visible places. Export UV template and editable texture layers when useful.
2. Keep paint, glass, rubber, carbon/trim and light elements separable by material or mesh when functionally needed.
3. Prefer neutral/paint-friendly albedo and a mask for primary/secondary tint zones; preserve brand-neutral original artwork separately from texture data. Don't permanently bake the default paint color into the only source texture.
4. Bake unsupported Blender shader effects into supported textures. Keep mesh topology and UV interfaces stable for alternate liveries and optimized variants.

## In Roblox (implementation belongs to game code)

- **Live color picker:** tint `MeshPart.Color` or `SurfaceAppearance.Color` depending on material setup. For PBR paint-zone masking, see `SurfaceAppearance.AlphaMode = Enum.AlphaMode.TintMask` and an appropriate ColorMap alpha mask; verify in client.
- **Static full-body livery:** apply UV-aligned ColorMap/texture variants; preserve fixed lights, windows and other non-paint regions. Handle decal seam alignment explicitly.
- **Finish:** use metalness/roughness maps and materials; not every Blender material node exists in Roblox.
- **Animated color/emission:** simple tint changes and supported emission controls may be animated via script; validate exact properties and client/device rendering.
- **Moving-pattern skins:** Roblox does **not** expose arbitrary custom material shaders. Options include limited overlays, scrolling textures where supported, sequenced preauthored appearances, or `EditableImage`-based texture updates if available and permitted. These require prototyping and may cost significant memory/CPU/GPU bandwidth. Avoid promising arbitrary shader motion or cheap per-frame replacement of many high-resolution maps.

## QA and deliverable

- Validate two static liveries (one cross-panel pattern), at least two tint colors and a UV checkerboard to reveal stretching. Check L/R symmetry, seams, glass and trim unaffected, gameplay-camera readability.
- For animated requests, create **one** performance-tested prototype and a static fallback before building a full library.
- Deliver UV template, paint-mask map, material-zone naming and a note on which effects are **prepared only** vs **implemented and tested in Roblox**.

Roblox references:
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://create.roblox.com/docs/reference/engine/classes/SurfaceAppearance
- https://create.roblox.com/docs/reference/engine/classes/EditableImage

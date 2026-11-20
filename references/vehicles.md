# Vehicles, machines, modular equipment

Apply only when the task involves a vehicle or mechanical assembly.

## Form and design

- Establish the silhouette and wheelbase before microdetails. Match supplied reference angles and dimensions; invent only what is hidden or intentionally open to interpretation.
- Preserve approved design; inspect side/front/rear/top, wheel arches, hood, glass, underbody, seams, lights and spoilers. Prioritize readability at actual gameplay scale.
- Build independent geometry for anything the player or game may replace, animate, tint or illuminate. Keep fixed decorative elements merged only when beneficial for performance.

## Suggested hierarchy (adapt, do not enforce)

```text
VehicleRoot
  Body_Paintable
  Body_Trim
  Glass
  Wheel_FL | Wheel_FR | Wheel_RL | Wheel_RR
  Light_Front_L | Light_Front_R
  Light_Rear_L  | Light_Rear_R
  Interior
  Spoiler (optional replaceable part)
  Mount_Spoiler | Mount_Boost (attachment locators)
```

- **Wheels:** four independently addressable objects. Locate their origins at actual wheel rotation centers; preserve consistent vehicle-local axes. Separate tire/rim/caliper when customization demands it.
- **Cosmetics:** preserve paintable zones, trim/glass/light separation, stable UVs and clear attachment mounts. Swappable parts need compatible transforms and named connection points.
- **Materials:** use Blender materials as editable sources and bake supported PBR textures for Roblox when necessary. Do not rely on Blender-only shader nodes transferring to Roblox.
- **Physics:** an artist's mesh does not define gameplay hitboxes by default. Only the host integration agent with project context should bind visual models to physics.
- **Variants:** align HQ / GAME / optional MOBILE at the same dimensions, root orientation, wheel centers and mount positions. Share compatible skin UVs where practical.

## Internal magenta leak test (enclosed vehicles)

- Temporarily make the car interior intensely magenta/emissive or place bright magenta lights inside, darken exterior lighting, and inspect opaque-window seams, A/C pillars, skirts, wheel arches and diffuser from multiple outside angles. Unexpected magenta bleeding through panels reveals possible micro-gaps or flipped faces.
- Distinguish deliberate vents/transparency from defects. Repeat on **GAME subdivision/export-equivalent geometry**; remove test lights/materials before delivery. This helps find leaks but cannot guarantee complete watertightness.

Before handoff: provide a component inventory and identify which parts are swappable, tintable, emissive, or fixed.

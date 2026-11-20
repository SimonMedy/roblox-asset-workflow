#!/usr/bin/env python3
"""Read-only mesh overview for the active Blender scene (requires Blender Python).

Usage:
    blender -b asset.blend --python scripts/audit_blender.py -- --output audit.json

Counts evaluated geometry after enabled modifiers (n-gons triangulate to n-2).
It does not replace inspecting the actual Roblox-imported mesh or profiling GPU use.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import bpy
except ImportError as exc:
    raise SystemExit("Run through Blender, not normal Python: blender -b FILE.blend --python scripts/audit_blender.py") from exc

MESH_LIMIT = 20_000


def main() -> None:
    params = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description="Read-only Blender mesh triangle audit")
    parser.add_argument("--output", help="Optional JSON report path")
    args = parser.parse_args(params)

    scene = bpy.context.scene
    graph = bpy.context.evaluated_depsgraph_get()
    meshes = []
    warnings = []
    for obj in sorted(scene.objects, key=lambda o: o.name):
        if obj.type != "MESH":
            continue
        evaluated = obj.evaluated_get(graph)
        try:
            mesh = evaluated.to_mesh(preserve_all_data_layers=True, depsgraph=graph)
        except Exception as exc:  # Do not hide missing data or modifier failures.
            warnings.append(f"{obj.name}: could not evaluate mesh: {exc}")
            continue
        if mesh is None:
            warnings.append(f"{obj.name}: evaluated mesh returned None")
            continue
        try:
            triangles = sum(max(0, len(poly.vertices) - 2) for poly in mesh.polygons)
            record = {
                "name": obj.name,
                "triangles_evaluated": triangles,
                "vertices_evaluated": len(mesh.vertices),
                "uv_layers": len(mesh.uv_layers),
                "material_slots": len(obj.material_slots),
                "hide_render": bool(obj.hide_render),
                "scale": [round(float(v), 6) for v in obj.scale],
                "over_roblox_20k": triangles > MESH_LIMIT,
            }
            meshes.append(record)
            if record["over_roblox_20k"]:
                warnings.append(f"{obj.name}: {triangles} triangles exceeds {MESH_LIMIT} per mesh")
            if not mesh.uv_layers and record["material_slots"]:
                warnings.append(f"{obj.name}: material slots present, but no UV layer (may be intentional)")
        finally:
            evaluated.to_mesh_clear()

    data = {
        "asset_file": bpy.data.filepath,
        "scene": scene.name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "rule": "Roblox standard meshes: <=20000 triangles per individual mesh; avatar/UGC may differ",
        "method": "all mesh objects in active scene; evaluated modifiers; no export merging accounted for",
        "total_triangles": sum(m["triangles_evaluated"] for m in meshes),
        "max_triangles_per_mesh": max((m["triangles_evaluated"] for m in meshes), default=0),
        "mesh_count": len(meshes),
        "meshes": meshes,
        "warnings": warnings,
    }
    report = json.dumps(data, indent=2, ensure_ascii=False)
    if args.output:
        target = Path(args.output).expanduser().resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(report + "\n", encoding="utf-8")
        print(f"Asset audit saved: {target}")
    else:
        print(report)
    print(f"Mesh count={data['mesh_count']}; triangles={data['total_triangles']}; max/mesh={data['max_triangles_per_mesh']}")
    for w in warnings:
        print("WARNING:", w)


if __name__ == "__main__":
    main()

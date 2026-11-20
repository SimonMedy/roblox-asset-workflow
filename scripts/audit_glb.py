#!/usr/bin/env python3
"""Dependency-free read-only glTF 2.0 GLB preflight; not an actual Studio import test."""
from __future__ import annotations
import argparse
import json
import struct
from pathlib import Path

JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942
COMPONENTS = {5120: "b", 5121: "B", 5122: "h", 5123: "H", 5125: "I", 5126: "f"}
BYTES = {5120: 1, 5121: 1, 5122: 2, 5123: 2, 5125: 4, 5126: 4}
MAX_MESH_TRIANGLES = 20_000


def read_glb(path: Path) -> tuple[dict, bytes]:
    raw = path.read_bytes()
    if len(raw) < 20:
        raise ValueError("File too short for GLB")
    magic, version, length = struct.unpack_from("<4sII", raw)
    if magic != b"glTF" or version != 2 or length != len(raw):
        raise ValueError("Invalid GLB magic, version or declared length")
    offset, json_bytes, binary = 12, None, b""
    while offset < len(raw):
        if offset + 8 > len(raw):
            raise ValueError("Incomplete GLB chunk header")
        chunk_len, chunk_type = struct.unpack_from("<II", raw, offset)
        offset += 8
        if chunk_len % 4 or offset + chunk_len > len(raw):
            raise ValueError("Invalid GLB chunk length")
        chunk = raw[offset:offset + chunk_len]
        offset += chunk_len
        if chunk_type == JSON_CHUNK and json_bytes is None:
            json_bytes = chunk
        elif chunk_type == BIN_CHUNK and not binary:
            binary = chunk
    if json_bytes is None:
        raise ValueError("Missing JSON chunk")
    document = json.loads(json_bytes.decode("utf-8").rstrip(" \t\r\n\0"))
    if not isinstance(document, dict) or document.get("asset", {}).get("version") != "2.0":
        raise ValueError("Missing glTF 2.0 metadata")
    return document, binary


def uv_bounds(document: dict, binary: bytes, accessor_id: int) -> tuple[float, float] | None:
    """Decode non-sparse UV0 accessor, including stride and normalized integer components."""
    accessor = document["accessors"][accessor_id]
    if accessor.get("type") != "VEC2" or "sparse" in accessor or "bufferView" not in accessor:
        return None
    component = accessor.get("componentType")
    if component not in COMPONENTS:
        return None
    view = document["bufferViews"][accessor["bufferView"]]
    if view.get("buffer", 0) != 0 or document.get("buffers", [{}])[0].get("uri"):
        return None
    count = accessor["count"]
    width = 2 * BYTES[component]
    stride = view.get("byteStride", width)
    start = view.get("byteOffset", 0) + accessor.get("byteOffset", 0)
    view_end = view.get("byteOffset", 0) + view["byteLength"]
    if stride < width or (count and start + (count - 1) * stride + width > view_end):
        return None
    if count and start + (count - 1) * stride + width > len(binary):
        return None
    fmt = "<" + 2 * COMPONENTS[component]
    values = []
    for i in range(count):
        a, b = struct.unpack_from(fmt, binary, start + i * stride)
        if accessor.get("normalized") and component != 5126:
            maximum = float((1 << (BYTES[component] * 8 - (component in (5120, 5122)))) - 1)
            if component in (5120, 5122):
                a, b = max(a / maximum, -1.0), max(b / maximum, -1.0)
            else:
                a, b = a / maximum, b / maximum
        values.extend((a, b))
    return (min(values), max(values)) if values else None


def audit(document: dict, binary: bytes) -> dict:
    warnings: list[str] = []
    meshes = []
    uv_checked = 0
    for index, mesh in enumerate(document.get("meshes", [])):
        name = mesh.get("name") or f"mesh_{index}"
        triangles = 0
        materials: set[int] = set()
        primitives = mesh.get("primitives", [])
        for p, primitive in enumerate(primitives):
            mode = primitive.get("mode", 4)
            indices = primitive.get("indices")
            attributes = primitive.get("attributes", {})
            source = indices if indices is not None else attributes.get("POSITION")
            count = document["accessors"][source]["count"] if source is not None else 0
            if mode == 4:
                triangles += count // 3
                if count % 3:
                    warnings.append(f"{name}: primitive {p} has incomplete triangle indices")
            elif mode in (5, 6):
                triangles += max(0, count - 2)
            else:
                warnings.append(f"{name}: primitive {p} uses non-triangle mode {mode}")
            if "material" in primitive:
                materials.add(primitive["material"])
            if "TEXCOORD_0" not in attributes:
                warnings.append(f"{name}: primitive {p} missing TEXCOORD_0 (check paint/skins)")
            else:
                try:
                    bounds = uv_bounds(document, binary, attributes["TEXCOORD_0"])
                except (IndexError, KeyError, TypeError, ValueError, struct.error):
                    bounds = None
                if bounds is None:
                    warnings.append(f"{name}: primitive {p} UV0 could not be decoded; verify manually")
                else:
                    uv_checked += 1
                    if bounds[0] < -1e-5 or bounds[1] > 1 + 1e-5:
                        warnings.append(f"{name}: primitive {p} UV0 outside [0,1]: {bounds}")
        if len(primitives) > 1:
            warnings.append(f"{name}: {len(primitives)} glTF primitives; verify Studio part splitting/names")
        if len(materials) > 1:
            warnings.append(f"{name}: {len(materials)} materials; split customizable parts intentionally or atlas")
        if triangles > MAX_MESH_TRIANGLES:
            warnings.append(f"{name}: {triangles} triangles exceeds {MAX_MESH_TRIANGLES} per glTF mesh")
        meshes.append({"name": name, "triangles": triangles, "primitives": len(primitives),
                       "material_count": len(materials)})
    images = document.get("images", [])
    embedded = 0
    for i, item in enumerate(images):
        if "bufferView" in item or item.get("uri", "").startswith("data:"):
            embedded += 1
        else:
            warnings.append(f"image {i}: external or missing URI; texture not packed into GLB")
    extensions = document.get("extensionsUsed", [])
    for ext in extensions:
        warnings.append(f"Extension {ext}: verify import/appearance in Roblox Studio (support varies)")
    return {"mesh_count": len(meshes), "mesh_triangles_total": sum(m["triangles"] for m in meshes),
            "max_triangles_per_mesh": max((m["triangles"] for m in meshes), default=0),
            "uv_primitives_checked": uv_checked, "images_embedded": embedded,
            "images_total": len(images), "extensions_used": extensions, "meshes": meshes,
            "warnings": warnings,
            "limitations": "Preflight only: Roblox importer splitting, actual topology, transformations and rendering untested"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect exported binary glTF for Roblox handoff")
    parser.add_argument("file", type=Path, help="Exported .glb")
    parser.add_argument("--output", type=Path, help="Optional JSON output")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero if warnings exist")
    args = parser.parse_args()
    try:
        report = audit(*read_glb(args.file))
    except (OSError, ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Invalid or unreadable GLB: {exc}\n")
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    if args.strict and report["warnings"]:
        parser.exit(1)


if __name__ == "__main__":
    main()

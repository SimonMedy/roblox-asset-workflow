"""Synthetic GLB preflight tests; no Blender installation required."""
import json
import struct
import tempfile
import unittest
from pathlib import Path
from scripts.audit_glb import audit, read_glb, uv_bounds


def fixture(uv=(0.0, 0.0, 1.0, 1.0, 0.2, 0.8), *, second_material=False,
            external_image=False, extension=False):
    uv_data = struct.pack("<6f", *uv)
    indices = struct.pack("<3H", 0, 1, 2)
    binary = uv_data + indices
    primitive = {"attributes": {"POSITION": 0, "TEXCOORD_0": 1}, "indices": 2, "material": 0}
    primitives = [primitive]
    if second_material:
        primitives.append({**primitive, "material": 1})
    doc = {"asset": {"version": "2.0"}, "buffers": [{"byteLength": len(binary)}],
           "bufferViews": [{"buffer": 0, "byteOffset": 0, "byteLength": len(uv_data)},
                           {"buffer": 0, "byteOffset": len(uv_data), "byteLength": len(indices)}],
           "accessors": [{"count": 3, "type": "VEC3", "componentType": 5126},
                         {"count": 3, "type": "VEC2", "componentType": 5126, "bufferView": 0},
                         {"count": 3, "type": "SCALAR", "componentType": 5123, "bufferView": 1}],
           "meshes": [{"name": "Body", "primitives": primitives}],
           "images": [{"uri": "paint.png"}] if external_image else [{"bufferView": 0, "mimeType": "image/png"}]}
    if extension:
        doc["extensionsUsed"] = ["KHR_materials_emissive_strength"]
    return doc, binary


def encode_glb(doc, binary):
    payload = json.dumps(doc, separators=(",", ":")).encode("utf-8")
    payload += b" " * (-len(payload) % 4)
    binary += b"\0" * (-len(binary) % 4)
    length = 12 + 8 + len(payload) + 8 + len(binary)
    return (struct.pack("<4sII", b"glTF", 2, length)
            + struct.pack("<II", len(payload), 0x4E4F534A) + payload
            + struct.pack("<II", len(binary), 0x004E4942) + binary)


class AuditGlbTests(unittest.TestCase):
    def test_bounds_and_triangles(self):
        doc, data = fixture()
        report = audit(doc, data)
        self.assertEqual(report["mesh_triangles_total"], 1)
        self.assertEqual(report["uv_primitives_checked"], 1)
        self.assertEqual(report["warnings"], [])
        self.assertEqual(uv_bounds(doc, data, 1), (0.0, 1.0))

    def test_uv_material_and_texture_warnings(self):
        doc, data = fixture(uv=(-0.5, 0, 2, 0, 0.2, 0.8), second_material=True,
                            external_image=True, extension=True)
        warnings = " ".join(audit(doc, data)["warnings"])
        for expected in ("outside [0,1]", "2 materials", "not packed", "Extension"):
            self.assertIn(expected, warnings)

    def test_unreadable_uv(self):
        doc, data = fixture()
        del doc["accessors"][1]["bufferView"]
        self.assertIsNone(uv_bounds(doc, data, 1))
        self.assertIn("could not be decoded", " ".join(audit(doc, data)["warnings"]))

    def test_roundtrip_and_corrupt_file(self):
        doc, data = fixture()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.glb"
            path.write_bytes(encode_glb(doc, data))
            self.assertEqual(read_glb(path)[0]["meshes"][0]["name"], "Body")
            path.write_bytes(b"invalid")
            with self.assertRaises(ValueError):
                read_glb(path)

    def test_over_budget(self):
        doc, data = fixture()
        doc["accessors"][2]["count"] = 60_003
        self.assertIn("20000", " ".join(audit(doc, data)["warnings"]))


if __name__ == "__main__":
    unittest.main()

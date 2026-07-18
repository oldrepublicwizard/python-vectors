from __future__ import annotations

import math
import unittest

from unittest import TestCase

from vector_primitives.geometry import Polygon2, Vector2, Vector3, Vector4

class TestVector2(TestCase):
    def test_unpacking(self):
        source = Vector2(1.2, 2.3)
        x, y = source
        self.assertAlmostEqual(x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(y, 2.3, places=_VPLACES)

    def test_from_vector2(self):
        source = Vector2(1.2, 2.3)
        vec2 = Vector2.from_vector2(source)
        self.assertAlmostEqual(vec2.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec2.y, 2.3, places=_VPLACES)

    def test_from_vector3(self):
        source = Vector3(1.2, 2.3, 3.4)
        vec2 = Vector2.from_vector3(source)
        self.assertAlmostEqual(vec2.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec2.y, 2.3, places=_VPLACES)

    def test_from_vector4(self):
        source = Vector4(1.2, 2.3, 3.4, 5.6)
        vec2 = Vector2.from_vector4(source)
        self.assertAlmostEqual(vec2.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec2.y, 2.3, places=_VPLACES)


class TestVector3(TestCase):
    def test_unpacking(self):
        source = Vector3(1.2, 2.3, 3.4)
        x, y, z = source
        self.assertAlmostEqual(x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(z, 3.4, places=_VPLACES)

    def test_from_vector2(self):
        source = Vector2(1.2, 2.3)
        vec3 = Vector3.from_vector2(source)
        self.assertAlmostEqual(vec3.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec3.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec3.z, 0.0, places=_VPLACES)

    def test_from_vector3(self):
        source = Vector3(1.2, 2.3, 3.4)
        vec3 = Vector3.from_vector3(source)
        self.assertAlmostEqual(vec3.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec3.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec3.z, 3.4, places=_VPLACES)

    def test_from_vector4(self):
        source = Vector4(1.2, 2.3, 3.4, 5.6)
        vec3 = Vector3.from_vector4(source)
        self.assertAlmostEqual(vec3.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec3.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec3.z, 3.4, places=_VPLACES)


class TestVector4(TestCase):
    def test_unpacking(self):
        source = Vector4(1.2, 2.3, 3.4, 4.5)
        x, y, z, w = source
        self.assertAlmostEqual(x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(z, 3.4, places=_VPLACES)
        self.assertAlmostEqual(w, 4.5, places=_VPLACES)

    def test_from_vector2(self):
        source = Vector2(1.2, 2.3)
        vec4 = Vector4.from_vector2(source)
        self.assertAlmostEqual(vec4.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec4.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec4.z, 0.0, places=_VPLACES)
        self.assertAlmostEqual(vec4.w, 0.0, places=_VPLACES)

    def test_from_vector3(self):
        source = Vector3(1.2, 2.3, 3.4)
        vec4 = Vector4.from_vector3(source)
        self.assertAlmostEqual(vec4.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec4.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec4.z, 3.4, places=_VPLACES)
        self.assertAlmostEqual(vec4.w, 0.0, places=_VPLACES)

    def test_from_vector4(self):
        source = Vector4(1.2, 2.3, 3.4, 5.6)
        vec4 = Vector4.from_vector4(source)
        self.assertAlmostEqual(vec4.x, 1.2, places=_VPLACES)
        self.assertAlmostEqual(vec4.y, 2.3, places=_VPLACES)
        self.assertAlmostEqual(vec4.z, 3.4, places=_VPLACES)
        self.assertAlmostEqual(vec4.w, 5.6, places=_VPLACES)

    def test_from_euler(self):
        # Converting degrees to radians
        rad_90 = math.radians(90)

        q1 = Vector4.from_euler(0, 0, 0)
        q2 = Vector4.from_euler(rad_90, 0, 0)
        q3 = Vector4.from_euler(0, rad_90, 0)
        q4 = Vector4.from_euler(0, 0, rad_90)

        self.assertAlmostEqual(0.0, q1.x, 1)
        self.assertAlmostEqual(0.0, q1.y, 1)
        self.assertAlmostEqual(0.0, q1.z, 1)
        self.assertAlmostEqual(1.0, q1.w, 1)

        self.assertAlmostEqual(0.7, q2.x, 1)
        self.assertAlmostEqual(0.0, q2.y, 1)
        self.assertAlmostEqual(0.0, q2.z, 1)
        self.assertAlmostEqual(0.7, q2.w, 1)

        self.assertAlmostEqual(0.0, q3.x, 1)
        self.assertAlmostEqual(0.7, q3.y, 1)
        self.assertAlmostEqual(0.0, q3.z, 1)
        self.assertAlmostEqual(0.7, q3.w, 1)

        self.assertAlmostEqual(0.0, q4.x, 1)
        self.assertAlmostEqual(0.0, q4.y, 1)
        self.assertAlmostEqual(0.7, q4.z, 1)
        self.assertAlmostEqual(0.7, q4.w, 1)


class TestPolygon2(TestCase):
    def test_inside(self):
        poly = Polygon2(
            [
                Vector2(0.0, 0.0),
                Vector2(0, 6),
                Vector2(6, 6),
                Vector2(6, 0),
                Vector2(3, 3),
            ]
        )

        # Inside
        assert poly.inside(Vector2(2.0, 4.0))
        assert poly.inside(Vector2(5.0, 6.0))

        # On the edge
        assert poly.inside(Vector2(0.0, 3.0))
        assert not poly.inside(Vector2(0.0, 3.0), False)

        # Outside
        assert not poly.inside(Vector2(3.0, 0.0))
        assert not poly.inside(Vector2(3.0, 7.0))

    def test_area(self):
        poly = Polygon2(
            [
                Vector2(0.0, 0.0),
                Vector2(0, 6),
                Vector2(6, 6),
                Vector2(6, 0),
                Vector2(3, 3),
            ]
        )

        assert poly.area() == 27.0


if __name__ == "__main__":
    try:
        import pytest
    except ImportError:  # pragma: no cover
        unittest.main()
    else:
        pytest.main(["-v", __file__])

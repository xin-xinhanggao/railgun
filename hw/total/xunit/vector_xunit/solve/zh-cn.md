### test_get_vertical.py:

```python
import unittest
from get_vertical import vertical
from vector import Vector


class verticalTestCase(unittest.TestCase):

    def test_z_z(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(0, 0, 0)
        v3 = Vector(1, 0, 0)
        self.assertEqual(vertical(v1, v2), v3)

    def test_z_n(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(1, 0, 0)
        v3 = Vector(1, 0, 0)
        self.assertEqual(vertical(v1, v2), v3)

    def test_p_p(self):
        v1 = Vector(2, 0, 0)
        v2 = Vector(1, 0, 0)
        v3 = Vector(1, 0, 0)
        self.assertEqual(vertical(v1, v2), v3)

    def test_n_n(self):
        v1 = Vector(0, 1, 0)
        v2 = Vector(1, 0, 0)
        v3 = Vector(0, 0, 1)
        self.assertEqual(vertical(v1, v2), v3)

```

### test_operation.py:

```python
import unittest
from operation import dot, cross
from vector import Vector


class crossTestCase(unittest.TestCase):

    def test_zero_cross_zero(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(0, 0, 0)
        v3 = Vector(0, 0, 0)
        self.assertEqual(cross(v1, v2), v3)

    def test_zero_cross_normal(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(0, 1, 0)
        v3 = Vector(0, 0, 0)
        self.assertEqual(cross(v1, v2), v3)

    def test_p1_cross_p2(self):
        v1 = Vector(1, 1, 1)
        v2 = Vector(2, 2, 2)
        v3 = Vector(0, 0, 0)
        self.assertEqual(cross(v1, v2), v3)

    def test_n1_cross_n2(self):
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        v3 = Vector(0, 0, 1)
        self.assertEqual(cross(v1, v2), v3)


class dotTestCase(unittest.TestCase):

    def test_zero_dot_zero(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(0, 0, 0)
        self.assertEqual(dot(v1, v2), 0)

    def test_zero_dot_n1(self):
        v1 = Vector(0, 0, 0)
        v2 = Vector(1, 0, 0)
        self.assertEqual(dot(v1, v2), 0)

    def test_v1_dot_v2(self):
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        self.assertEqual(dot(v1, v2), 0)

    def test_n1_dot_n2(self):
        v1 = Vector(1, 1, 0)
        v2 = Vector(1, 0, 1)
        self.assertEqual(dot(v1, v2), 1)

```

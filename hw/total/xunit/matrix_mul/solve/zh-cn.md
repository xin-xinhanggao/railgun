### test_operation.py:

```python
import unittest
from operation import checkMatrix, multiply


class CheckTestCase(unittest.TestCase):

    def test_empty(self):
        list = [[]]
        self.assertEqual(checkMatrix(list), False)

    def test_column_different(self):
        list = [[1, 2], [3]]
        self.assertEqual(checkMatrix(list), False)

    def test_item_type(self):
        list = [['c']]
        self.assertEqual(checkMatrix(list), False)

    def test_legal(self):
        list = [[1, 0], [0, 1]]
        self.assertEqual(checkMatrix(list), True)


class MulTestCase(unittest.TestCase):

    def test_legal_mul_illegal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0]]
        self.assertEqual(multiply(m1, m2), False)

    def test_illegal_mul_legal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0]]
        self.assertEqual(multiply(m2, m1), False)

    def test_illegal_mul_illegal(self):
        m1 = [[1, 0], [0]]
        m2 = [[1, 0], [0]]
        self.assertEqual(multiply(m2, m1), False)

    def test_scale_error(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0]]
        self.assertEqual(multiply(m1, m2), False)

    def test_legal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0, 1]]
        m3 = [[1, 0], [0, 1]]
        self.assertEqual(multiply(m1, m2), m3)



```

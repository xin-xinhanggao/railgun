### test_operation.py:

```python
import unittest
from operation import checkMatrix, add


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


class AddTestCase(unittest.TestCase):

    def test_legal_add_illegal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0]]
        self.assertEqual(add(m1, m2), False)

    def test_illegal_add_legal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0]]
        self.assertEqual(add(m2, m1), False)

    def test_illegal_add_illegal(self):
        m1 = [[1, 0], [0]]
        m2 = [[1, 0], [0]]
        self.assertEqual(add(m2, m1), False)

    def test_different_row(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0]]
        self.assertEqual(add(m1, m2), False)

    def test_different_column(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1], [0]]
        self.assertEqual(add(m1, m2), False)

    def test_legal(self):
        m1 = [[1, 0], [0, 1]]
        m2 = [[1, 0], [0, 1]]
        self.assertEqual(add(m1, m2), False)


```

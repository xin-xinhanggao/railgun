    import unittest
    from pred import pred
    from BinNode import BinNode

    x = BinNode()
    y = BinNode(x)
    x1 = BinNode()
    y_r = BinNode(x1)
    x1.set_lc(y_r)
    x.set_lc(y)
    rc_y = BinNode(y)
    y.set_rc(rc_y)


    class SampleTestCase(unittest.TestCase):
        def test_1(self):
            self.assertEqual(None, pred(x))

        def test_2(self):
            self.assertEqual(None, pred(y))

        def test_2(self):
            self.assertEqual(None, pred(y_r))

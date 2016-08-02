    import unittest
    from succ import succ
    from BinNode import BinNode

    x = BinNode()
    y = BinNode(x)
    x1 = BinNode()
    y_l = BinNode(x1)
    x1.set_rc(y_l)
    x.set_rc(y)
    lc_y = BinNode(y)
    y.set_lc(lc_y)


    class SampleTestCase(unittest.TestCase):
        def test_1(self):
            self.assertEqual(y, succ(x))

        def test_2(self):
            self.assertEqual(None, succ(y))

        def test_3(self):
            self.assertEqual(None, succ(y_l))

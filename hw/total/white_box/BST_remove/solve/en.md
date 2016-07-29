    import unittest
    from remove import remove
    from BinNode import BinNode

    x = BinNode()
    y = BinNode(x)
    x.set_lc(y)
    x1 = x
    z = BinNode(x1)
    x1.set_rc(z)
    x2 = x1
    p = BinNode()
    x2.set_p(p)
    p.set_rc(x2)
    x3 = x2
    p1 = BinNode()
    p2 = BinNode(p1)
    p1.set_lc(p2)
    p1.set_p(x3)
    x3.set_rc(p1)

    class SampleTestCase(unittest.TestCase):
        def test_1(self):
            self.assertEqual("rChild", remove(y))

        def test_2(self):
            self.assertEqual("lChild", remove(x))

        def test_3(self):
            self.assertEqual("x->rChild", remove(x1))

        def test_4(self):
            self.assertEqual("u->rChild", remove(x2))

        def test_5(self):
            self.assertEqual("u->lChild", remove(x3))

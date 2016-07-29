    import unittest
    from splay import splay
    from BinNode import BinNode

    v1 = None
    x = BinNode()
    gg = BinNode()
    g = BinNode(gg) 
    lc = BinNode(x)
    rc = BinNode(x)
    x.set_lc(lc)
    x.set_rc(rc)
    c_x = x
    c_x.set_p(g)
    g.set_lc(c_x)


    class SampleTestCase(unittest.TestCase):
        def test_1(self):
            self.assertEqual("None", splay(v1))

        def test_2(self):
            self.assertEqual("zig-zag", splay(lc))

        def test_3(self):
            self.assertEqual("zag-zag", splay(rc))

        def test_4(self):
            self.assertEqual("zag-zig", splay(x))

        def test_5(self):
            self.assertEqual("zig-zig", splay(g))

        def test_6(self):
            self.assertEqual("root", splay(gg))

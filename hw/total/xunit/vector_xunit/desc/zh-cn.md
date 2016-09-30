(Python)观察附件中 operation.py 和 get_vertical.py，按照以下要求书写单元测试：

*   operation.py 的单元测试代码应当位于 test_operation.py 中，而 get_vertical.py 的单元测试代码应当位于 test_get_vertical.py 中。
*   operation.py 中有两个函数，分别为dot和cross。dot用来求两向量数量积，cross用来求两向量的向量积。
*  get_vertical.py 中包含方法vertical，用于求与两输入向量垂直的向量。
*   每一个函数应当由一个对应的 <code>unittest.TestCase</code> 测试，具体要求为：
    -   <code>operation.cross</code> 函数由 <code>test_operation.crossTestCase</code> 测试。
    -   <code>operation.dot</code> 函数由 <code>test_operation.dotTestCase</code> 测试。
    -   <code>get_vertical.get_vertical</code> 函数由 <code>test_get_vertical.verticalTestCase</code> 测试。
*   <code>test_operation.crossTestCase</code> 要求：
    -   成员函数 <code>test_zero_cross_zero</code> 测试两个零向量叉积结果。
    -   成员函数 <code>test_zero_cross_normal</code> 测试零向量与非零向量叉积结果。
    -   成员函数 <code>test_p1_cross_p2</code> 测试两个非零平行向量叉积的结果。
    -   成员函数 <code>test_n1_cross_n2</code> 测试两个非零且不平行向量叉积的结果。
*   <code>test_operation.dotTestCase</code> 要求：
    -   成员函数 <code>test_zero_dot_zero</code> 测试两个零向量点积的结果。
    -   成员函数 <code>test_zero_dot_n1</code> 测试零向量与非零向量点积的结果。
    -   成员函数 <code>test_v1_dot_v2</code> 测试两非零垂直向量点积的结果。
    -   成员函数 <code>test_n1_dot_n2</code> 测试两非零且不垂直向量点积的结果。
*   <code>test_get_vertical.verticalTestCase</code> 要求：
    -   成员函数 <code>test_z_z</code>，测试输入两个零向量的情况。
    -   成员函数 <code>test_z_n</code>，测试输入零向量与非零向量的情况。
    -   成员函数 <code>test_p_p</code>，测试输入两平行非零向量的情况。
    -   成员函数 <code>test_n_n</code>，测试输入两非零不平行向量的情况。

上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。
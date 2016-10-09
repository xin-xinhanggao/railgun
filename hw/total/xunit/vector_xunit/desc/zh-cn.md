(Python)观察附件中 operation.py 和 get_vertical.py，按照以下要求书写单元测试：

*   operation.py 的单元测试代码应当位于 test_operation.py 中，而 get_vertical.py 的单元测试代码应当位于 test_get_vertical.py 中。
*   每一个函数应当由一个对应的 <code>unittest.TestCase</code> 测试，具体要求为：
    -   <code>operation.cross</code> 函数由 <code>test_operation.crossTestCase</code> 测试。
    -   <code>operation.dot</code> 函数由 <code>test_operation.dotTestCase</code> 测试。
    -   <code>get_vertical.get_vertical</code> 函数由 <code>test_get_vertical.verticalTestCase</code> 测试。
*   <code>test_operation.crossTestCase</code> 要求：
    -   成员函数 <code>test_zero_cross_zero</code> 测试两个零向量叉积结果。
    -   成员函数 <code>test_zero_cross_normal</code> 测试零向量与非零向量叉积结果。
    -   成员函数 <code>test_p1_cross_p2</code> 测试两个平行向量叉积的结果。
    -   成员函数 <code>test_n1_cross_n2</code> 测试两个非零且不平行向量叉积的结果。
*   <code>test_operation.dotTestCase</code> 要求：
    -   成员函数 <code>test_zero_dot_zero</code> 测试两个零向量点积的结果。
    -   成员函数 <code>test_zero_dot_n1</code> 测试零向量与非零向量点积的结果。
    -   成员函数 <code>test_v1_dot_v2</code> 测试两垂直向量点积的结果。
    -   成员函数 <code>test_n1_dot_n2</code> 测试两非零且不垂直向量点积的结果。
*   <code>test_get_vertical.verticalTestCase</code> 要求：
    -   成员函数 <code>test_z_z</code>，测试两个零向量的情况。
    -   成员函数 <code>test_z_n</code>，测试零向量与非零向量的情况。
    -   成员函数 <code>test_p_p</code>，测试两平行非零向量的情况。
    -   成员函数 <code>test_n_n</code>，测试两非零非平行向量的情况。

(Java)观察附件中 Operation.java 和 GetVertical.java，按照以下要求书写单元测试：

*   Operation.java 的单元测试代码应当位于 OperationTest.java 中，而 GetVertical.java 的单元测试代码应当位于 GetVerticalTest.java 中。
*   每一个函数应当由一个对应的 <code>org.junit.Test</code> 测试，具体要求为：
    -   <code>Operation.cross</code> 函数由 <code>OperationTest</code> 测试。
    -   <code>Operation.dot</code> 函数由 <code>OperationTest</code> 测试。
    -   <code>GetVertical.getVertical</code> 函数由 <code>GetVerticalTest</code> 测试。
*   <code>OperationTest</code> 要求：
    -   成员函数 <code>test_zero_cross_zero</code> 测试两个零向量叉积结果。
    -   成员函数 <code>test_zero_cross_normal</code> 测试零向量与非零向量叉积结果。
    -   成员函数 <code>test_p1_cross_p2</code> 测试两个平行向量叉积的结果。
    -   成员函数 <code>test_n1_cross_n2</code> 测试两个非零且不平行向量叉积的结果。
*   <code>OperationTest</code> 要求：
    -   成员函数 <code>test_zero_dot_zero</code> 测试两个零向量点积的结果。
    -   成员函数 <code>test_zero_dot_n1</code> 测试零向量与非零向量点积的结果。
    -   成员函数 <code>test_v1_dot_v2</code> 测试两垂直向量点积的结果。
    -   成员函数 <code>test_n1_dot_n2</code> 测试两非零且不垂直向量点积的结果。
*   <code>GetVerticalTest</code> 要求：
    -   成员函数 <code>test_z_z</code>，测试两个零向量的情况。
    -   成员函数 <code>test_z_n</code>，测试零向量与非零向量的情况。
    -   成员函数 <code>test_p_p</code>，测试两平行非零向量的情况。
    -   成员函数 <code>test_n_n</code>，测试两非零非平行向量的情况。

上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。

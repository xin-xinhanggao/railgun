(Python)观察附件中 operation.py，按照以下要求书写单元测试：

*   本题中用二维列表表示矩阵，例：[ [1,0] , [0,1] ] 表示二维单位矩阵。
*   本题中认为空矩阵不是合法矩阵，且合法矩阵中只能包含整数和浮点数，不能包含其他数据类型。
*   operation.py 中<code>checkMatrix(list)</code>方法用来判断传入的list是否是合法矩阵。
* operation.py 中<code>multiply(matrix1,matrix2)</code>方法用来进行矩阵的乘法。
*   operation.py 的单元测试代码应当位于 test_operation.py 中。
*   每一个函数应当由一个对应的 <code>unittest.TestCase</code> 测试，具体要求为：
    -   <code>operation.checkMatrix</code> 函数由 <code>test_operation.CheckTestCase</code> 测试。
 -   <code>operation.multiply</code> 函数由 <code>test_operation.MulTestCase</code> 测试。
*   <code>test_operation.CheckTestCase</code> 要求：
    -   成员函数 <code>test_empty</code> 测试空矩阵的结果。
    -   成员函数 <code>test_column_different</code> 测试矩阵列的数目不相同的结果。
    -   成员函数 <code>test_item_type</code> 测试矩阵中元素类型不是整数或浮点数的结果。
    -   成员函数 <code>test_legal</code> 测试传入合法矩阵后的结果。

*   <code>test_operation.MulTestCase</code> 要求：
    -   成员函数 <code>test_legal_mul_illegal</code> 测试合法矩阵与非法矩阵相乘的结果。
    -   成员函数 <code>test_illegal_mul_legal</code> 测试非法矩阵与合法矩阵相乘的结果。
    -   成员函数 <code>test_illegal_mul_illegal</code> 测试非法矩阵与非法矩阵相乘的结果。
    -   成员函数 <code>test_scale_error</code> 测试两合法但规模不匹配矩阵相乘的结果。
    -   成员函数 <code>test_legal</code> 测试两合法且规模匹配矩阵相乘的结果。

上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。
(Python)Observe operation.py and get_vertical.py，and compose unit test cases as following：

*   The unit test code for operation.py should be placed in test_operation.py , while the code for get_vertical.py should be placed in test_get_vertical.py.
*   Each function should be tested by an individual <code>unittest.TestCase</code>:
    -   <code>operation.cross</code> should be tested by <code>test_operation.crossTestCase</code> 。
    -   <code>operation.dot</code> should be tested by <code>test_operation.dotTestCase</code> 。
    -   <code>get_vertical.get_vertical</code> should be tested by <code>test_get_vertical.verticalTestCase</code> 。
*   <code>test_operation.crossTestCase</code> ：
    -    <code>test_zero_cross_zero</code> test the product of two zero vectors。
    -    <code>test_zero_cross_normal</code>  test the product of a zero vector and a normal one。
    -    <code>test_p1_cross_p2</code> test the product of two vectors which are parallel。
    -    <code>test_n1_cross_n2</code> test the product of two vectors which are not parallel。
*   <code>test_operation.dotTestCase</code> ：
    -   <code>test_zero_dot_zero</code> test the dot of two zero vectors。
    -   <code>test_zero_dot_n1</code> test the product of a zero vector and a normal one。
    -  <code>test_v1_dot_v2</code> test the product of two vectors which are parallel。
    -   <code>test_n1_dot_n2</code> test the product of two vectors which are not parallel。
*   <code>test_get_vertical.verticalTestCase</code> ：
    -   <code>test_z_z</code>，test two zero vectors case。
    -   <code>test_z_n</code>，test zero one and nonzero one case。
    -   <code>test_p_p</code>,  test two parallel vectors case。
    -   <code>test_n_n</code>，test two unparallel vectors case。

You must make sure that your programs follow the code styles. Please upload your submission before deadlines. Otherwise there will be discounts on your scores.

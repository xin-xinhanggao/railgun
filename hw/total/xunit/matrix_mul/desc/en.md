(Python)Observe operation.py，and compose unit test cases as following:

*   We use two-dimensional list represents matrix，eg：[ [1,0] , [0,1] ] represents unit matrix.
*   We regard empty matrix as illegal matrix.
*   We appoint that the type of element in legal matrix only can be double,float or int.
*   <code>operation.checkMatrix(list)</code> is used to check whether list is a legal matrix.
* <code>mul(matrix1,matrix2)</code> is used to get product of two given matrixes.
*   The unit test code for observe.py should be placed in test_observe.py.

*   Each function should be tested by an individual <code>unittest.TestCase</code>:
    -   <code>operation.checkMatrix</code> should be tested by <code>test_operation.CheckTestCase</code>.
 -   <code>operation.add</code> should be tested by <code>test_operation.MulTestCase</code>.
*   <code>test_operation.CheckTestCase</code>：
    -   Method <code>test_empty</code> to test empty matrix.
    -   Method <code>test_column_different</code> to test matrix which the number of column is not consistent.
    -   Method <code>test_item_type</code> to test the type of element i n matrix is not int, float and double.
    -   Method <code>test_legal</code> to test legal matrix.

*   <code>test_operation.MulTestCase</code> :
    -   Method <code>test_legal_mul_illegal</code> to test the product of legal one and illegal one.
    -   Method <code>test_illegal_mul_legal</code>  to test the product of illegal one and legal one.
    -   Method <code>test_illegal_mul_illegal</code>  to test the product of illegal one and illegal one.
    -   Method <code>test_scale_error</code>  to test the product of two legal matrixes whose scale is not match with each other.
    -   Method <code>test_legal</code> to test the product of two legal matrixes which have the match scale.
You must make sure that your programs follow the code styles. Please upload your submission before deadlines. Otherwise there will be discounts on your scores.
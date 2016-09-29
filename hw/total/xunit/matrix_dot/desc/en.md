(Python)Observe operation.py，and compose unit test cases as following:

*   We use two-dimensional list represents matrix，eg：[ [1,0] , [0,1] ] represents unit matrix.
*   We regard empty matrix as illegal matrix.
*   We appoint that the type of element in legal matrix only can be double,float or int.
*   <code>operation.checkMatrix(list)</code> is used to check whether list is a legal matrix.
* <code>dot(matrix)</code> is used to get det of given matrix.
*   The unit test code for observe.py should be placed in test_observe.py.

*   Each function should be tested by an individual <code>unittest.TestCase</code>:
    -   <code>operation.checkMatrix</code> should be tested by <code>test_operation.CheckTestCase</code>.
 -   <code>operation.add</code> should be tested by <code>test_operation.DotTestCase</code>.
*   <code>test_operation.CheckTestCase</code>：
    -   Method <code>test_empty</code> to test empty matrix.
    -   Method <code>test_column_different</code> to test matrix which the number of column is not consistent.
    -   Method <code>test_item_type</code> to test the type of element i n matrix is not int, float and double.
    -   Method <code>test_legal</code> to test legal matrix.

*   <code>test_operation.DotTestCase</code>:
    -   Method <code>test_illegal</code></code> to test the det of illegal one.
    -   Method <code>test_rec</code> to test the det of rectangular one.
    -   Method <code>test_one</code> to test the det of one-demension matrix.
    -   Method <code>test_high</code> to test the det of high-demension matrix.
You must make sure that your programs follow the code styles. Please upload your submission before deadlines. Otherwise there will be discounts on your scores.
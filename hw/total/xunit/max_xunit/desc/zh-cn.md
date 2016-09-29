(Python)观察附件中 arith.py 和 minmax.py，按照以下要求书写单元测试：

*   arith.py 的单元测试代码应当位于 test_arith.py 中，而 minmax.py 的单元测试代码应当位于 test_minmax.py 中。
*   每一个函数应当由一个对应的 <code>unittest.TestCase</code> 测试，具体要求为：
    -   <code>arith.decrease</code> 函数由 <code>test_arith.decreaseTestCase</code> 测试。
    -   <code>arith.pow</code> 函数由 <code>test_arith.PowTestCase</code> 测试。
    -   <code>minmax.get_max</code> 函数由 <code>test_minmax.GetMinTestCase</code> 测试。
*   <code>test_arith.decreaseTestCase</code> 要求：
    -   成员函数 <code>test_positive_decrease_positive</code> 测试两个正数相减的结果。
    -   成员函数 <code>test_positive_decrease_negative</code> 测试正负数相减的结果。
    -   成员函数 <code>test_negative_decrease_negative</code> 测试两个负数相减的结果。
*   <code>test_arith.PowTestCase</code> 要求：
    -   成员函数 <code>test_positive_pow_positive</code> 测试两个正数乘方的结果。
    -   成员函数 <code>test_positive_pow_negative</code> 测试正数的负数次方的结果。
    -   成员函数 <code>test_negative_pow_positive_success</code> 测试负数的正数次方，且不引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_positive_failure</code> 测试负数的正数次方，且引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_negative_success</code> 测试负数的负数次方，且不引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_negative_failure</code> 测试负数的负数次方，且引发 <code>ValueError</code> 的结果。
*   <code>test_minmax.GetMaxTestCase</code> 要求：
    -   成员函数 <code>test_abc</code>，测试 a < b < c 的情况。
    -   成员函数 <code>test_acb</code>，测试 a < c < b 的情况。
    -   成员函数 <code>test_bac</code>，测试 b < a < c 的情况。
    -   成员函数 <code>test_bca</code>，测试 b < c < a 的情况。
    -   成员函数 <code>test_cab</code>，测试 c < a < b 的情况。
    -   成员函数 <code>test_cba</code>，测试 c < b < a 的情况。

(Java)观察附件中 arith.java 和 minmax.java，按照以下要求书写单元测试：

*   arith.java 的单元测试代码应当位于 arithTest.java 中，而 minmax.java 的单元测试代码应当位于 minmaxTest.java 中。
*   每一个函数应当由一个对应的 <code>org.junit.Test</code> 测试，具体要求为：
    -   <code>arith.decrease</code> 函数由 <code>arithTest</code> 测试。
    -   <code>arith.pow</code> 函数由 <code>arithTest</code> 测试。
    -   <code>minmax.get_max</code> 函数由 <code>minmaxTest</code> 测试。
*   <code>arithTest</code> 要求：
    -   成员函数 <code>test_positive_decrease_positive</code> 测试两个正数相减的结果。
    -   成员函数 <code>test_positive_decrease_negative</code> 测试正负数相减的结果。
    -   成员函数 <code>test_negative_decrease_negative</code> 测试两个负数相减的结果。
*   <code>arithTest</code> 要求：
    -   成员函数 <code>test_positive_pow_positive</code> 测试两个正数乘方的结果。
    -   成员函数 <code>test_positive_pow_negative</code> 测试正数的负数次方的结果。
    -   成员函数 <code>test_negative_pow_positive_success</code> 测试负数的正数次方，且不引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_positive_failure</code> 测试负数的正数次方，且引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_negative_success</code> 测试负数的负数次方，且不引发 <code>ValueError</code> 的结果。
    -   成员函数 <code>test_negative_pow_negative_failure</code> 测试负数的负数次方，且引发 <code>ValueError</code> 的结果。
*   <code>minmaxTest</code> 要求：
    -   成员函数 <code>test_abc</code>，测试 a < b < c 的情况。
    -   成员函数 <code>test_acb</code>，测试 a < c < b 的情况。
    -   成员函数 <code>test_bac</code>，测试 b < a < c 的情况。
    -   成员函数 <code>test_bca</code>，测试 b < c < a 的情况。
    -   成员函数 <code>test_cab</code>，测试 c < a < b 的情况。
    -   成员函数 <code>test_cba</code>，测试 c < b < a 的情况。


上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。

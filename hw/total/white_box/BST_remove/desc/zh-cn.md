二叉搜索树的删除算法一直是一个让人关注的焦点。在本题中，我们测试最基本的删除算法。

该算法针对结点的单分支，双分支情况分别进行处理，整体上比较复杂。为了简化难度，我们没有采用真正的remove函数，而是选择了其简化版本。

(Python)观察附件中 remove.py 中的函数 <code>remove</code>，写白盒单元测试，以达到尽可能高的覆盖率。

注意在 Python 中单元测试的类型必须继承自 <code>unittest.TestCase</code>，并且以保存在 test_*.py 的文件中。

(Java)观察附件中 remove.java 中的函数 <code>remove</code>，写白盒单元测试，以达到尽可能高的覆盖率。

每一个函数应当由一个对应的 <code>org.junit.Test</code> 测试，并且以保存在 removeTest.java 的文件中。

上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。

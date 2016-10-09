<code>Splay Tree</code>是一种重要的平衡二叉搜索树，而且操作高效，实现简洁。

为了能够提高<code>Splay Tree</code>的分摊效率，我们将采用双层伸展的方法。请你设计白盒测试用例，来测试<code>Splay Tree</code>的伸展调整算法。为了简化难度，我们没有采用真正的splay函数，而是选择了其简化版本。

我们已经将该伸展调整算法（即splay函数）的简化版本与二叉树节点类**BinNode**加到附件中，请于附件中下载。

(python)观察附件中splay.py 中的函数 <code>splay</code>，写白盒单元测试，以达到尽可能高的覆盖率。

注意在 Python 中单元测试的类型必须继承自 <code>unittest.TestCase</code>，并且以保存在 test_*.py 的文件中。

(java)观察附件中Splay.java 中的函数 <code>splay</code>，写白盒单元测试，以达到尽可能高的覆盖率。

注意在 Java 中使用 <code>org.junit.Test</code>进行对每个函数的单元测试，并且以保存在 SplayTest.py 的文件中。

上交的代码必须符合相应语言的代码规范。请务必在截止日期前上交作业，否则有相应的评分折扣。

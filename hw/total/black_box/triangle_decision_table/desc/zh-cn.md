为检测不同类型的的函数 <code>triangle_type</code>编写黑盒测试用例，该函数对不同的输入参数<kbd>a</kbd>, <kbd>b</kbd>, <kbd>c</kbd> 将会输出以下值：

*   非三角形
*   普通三角形（既不是等边三角形，也不是等腰三角形）
*   等腰三角形
*   等边三角形

请将以上4种情况当作**Action Stub** , 以下6种情况作为**Condition Stub**，列出判定表，并且将可以合并的规则合并。针对合并后判断表的每个符合数学逻辑的规则设计本题的黑盒测例，忽略违反数学逻辑的规则。

*  c1: a < b + c
*  c2: b < a + c
*  c3: c < a + b
*  c4: a == b
*  c5  a == c
*  c6  b == c

请在提交表单的文本框中输入你的测试用例。测试用例的格式为 CSV，且必须包含 <code>a,b,c</code> 的表头，例如：

    csv
    a,b,c
    4,1,2
请务必在截止日期前上交作业，否则不予计分。
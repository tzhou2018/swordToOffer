# -*- coding:utf-8 -*-
# 方法1
# 思路：使用python内置求和函数sum
class Solution:
    def Sum_Solution(self, n):
        # write code here
        listNum = list(range(1, n + 1))
        return sum(listNum)


# 方法2
# 思路：
# 1) 需利用逻辑与的短路特性实现递归终止;
# 2) 当n==0时，n>0 and self.Sum_Solution(n)只执行前面的判断，返回False；
# 3）当n>0时，执行self.Sum_Solution(n),实现递归计算。
class Solution:
    def __init__(self):
        self.res = 0

    def _sum(self, n):
        self.res += n
        n -= 1
        return n > 0 and self.Sum_Solution(n)

    def Sum_Solution(self, n):
        # write code here
        self._sum(n)
        return self.res


# 方法3
# 利用等差公式来计算，只用加法，乘方和位运算；

class Solution:
    def getSum(self, n):
        return (n ** 2 + n) >> 1

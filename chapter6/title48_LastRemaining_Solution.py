# -*- coding:utf-8 -*-
# 思路：
# 1）将输入的n个数编排成有序序列；
# 2）将out作为选择孩子的标号，从out开始往前走m-1个位置(out + (m-1)) % len(listNum),
# 直至当前圆圈长度等于1；
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <=0:
            return -1
        listNum = list(range(n))
        out = 0
        while len(listNum) > 1:
            out = (out + (m-1)) % len(listNum)
            del listNum[out]
        return listNum[0]
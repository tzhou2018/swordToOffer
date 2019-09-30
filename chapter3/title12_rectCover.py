# 解题思路：
# 还是斐波那契数列
# number <= 2 时，直接返回结果
# number > 2 时，f(n) = f(n-1) + f(n-2)
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        else:
            item1, item2, ans = 1, 2, 0
            for i in range(2, number):
                ans = item1 + item2
                item1, item2 = item2, ans
            return ans
# 丑数
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return 0
        ans = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(index - 1):
            num2, num3, num5 = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            tmp = min(num2, num3, num5)
            if tmp == num2:
                i2 += 1
            if tmp == num3:
                i3 += 1
            if tmp == num5:
                i5 += 1
            ans.append(tmp)
        return ans[-1]

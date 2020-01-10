# 整数中1出现的次数（从1到n整数中1出现的次数）
# -*- coding:utf-8 -*-

# 方法1
# 常规解法，遍历从1——n个数，依次求出每个数字中1的个数；
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            while i > 0:
                mod = i % 10
                i = i // 10
                if mod == 1:
                    count += 1
        return count
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ans, factor = 0, 1
        while n /factor != 0:
            low_num = n % factor
            cur_num = (n // factor) % 10
            high_num = n // (factor * 10)
            # 当前位数字为 0，则高位数字乘以当前位数；
            # 出现1的次数由更高位决定
            if cur_num == 0:
                ans += high_num * factor
            # 当前位数字为 1，1的次数不仅受更高位影响还受低位影响；
            # 则高位数字乘以当前位数在加上低位数字加 1
            elif cur_num == 1:
                ans += high_num *factor + low_num + 1
            # 出现1的情况仅由更高位决定
            else:
                ans += (high_num + 1) * factor
            factor *= 10
        return ans

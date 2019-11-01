# -*- coding:utf-8 -*-
# 思路：
# 1）判断所给字符串是否合法，判断该数正负
# 2）循环遍历s，使用python内置函数ord计算字符的ascii码值，并与ord('0')作差；
# 求出实际表示的值；
# 注：改程序在本地测试成功，但是提交到牛客网上并不能完全通过；
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        s = s.strip()
        if s[0] == '-':
            return -1 * self.convertInt(s[1:])
            # return 0
        elif s[0] == '+':
            return 1 * self.convertInt(s[1:])
        else:
            return self.convertInt(s)

    def convertInt(self, s):
        if not s:
            return 0
        ans = 0
        for item in s:
            if item >= '0' and item <= '9':
                ans = ans * 10 + ord(item) - ord('0')
            else:
                return 0
        return ans

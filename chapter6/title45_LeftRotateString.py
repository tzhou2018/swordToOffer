# -*- coding:utf-8 -*-
# 方法 1
# 思路：将所给字符串s当做列表进行处理，很容易就能得到左移、右移效果，
# 将转换后的字符串存储到列表result中，之后对result中的元素进行拼接。
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        lenS = len(s)
        result = []
        if lenS < n:
            return ''
        else:
            result.append(s[n:])
            result.append(s[:n])
        return ''.join(result)


# 方法 2
# 将所给字符串分为三部分进行逆转排序。首先将前n个逆转，之后将[n:]逆转，
# 最后将列表中的所有元素逆转并拼接
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        len_s = len(s)
        if n <= 0 or len_s == 0:
            return s
        n = n % len_s
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
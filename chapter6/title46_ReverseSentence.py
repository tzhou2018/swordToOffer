# -*- coding:utf-8 -*-
# 方法 1
# 思路：首先将所给字符串转化为列表，对此列表进行逆序排序，之后再将列表中的元素进行拼接
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        s = s.split(' ')
        s = s[::-1]
        return ' '.join(s)

# 方法 2
# -*- coding:utf-8 -*-
# 思路： 类似于title45 方法2
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        start, end = 0, 0
        while start < len(s):
            if s[start] == ' ':
                start += 1
                end += 1
            elif end == len(s) or s[end] == ' ':
                self.reverse(s, start, end - 1)
                end += 1
                start = end
            else:
                end += 1
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
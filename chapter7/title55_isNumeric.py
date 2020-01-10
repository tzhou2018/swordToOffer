# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/10/29 19:49
desc:
'''


# 思路：
# 遍历所给字符串s，依次判断每一个字符.注意:不要漏掉某些情况；

# 倘若，我们用 1e1+3e-1 来表示10.3，这种情况是不能通过的，
# 可能原题目也没有考虑这种情况吧！

class Solution:
    def isNumeric(self, s):
        is_dot, is_e = True, True
        for i in range(len(s)):
            if s[i] in '+-' and \
                    (i == 0 or s[i - 1] in 'eE'):
                continue
            elif is_dot and s[i] == '.':
                is_dot = False
                # 小数点可以在最后一位
                # if i == len(s) - 1:
                #     return False
            elif is_e and s[i] in 'eE':
                is_e = False
                is_dot = False
                if i == len(s) - 1:
                    return False
            elif s[i] not in "0123456789":
                return False
        return True


if __name__ == '__main__':
    print(Solution().isNumeric("1.5e+2"))

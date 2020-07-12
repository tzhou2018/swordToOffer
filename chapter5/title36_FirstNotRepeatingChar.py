# 第一个只出现一次的字符
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) > 10000 or not s:
            return -1
        res = list(s)
        dic = {}
        for key in res:
            dic[key] = dic.get(key, 0) + 1
        # 在python2.7中，dic.items() 返回的是无序状态的字典内容
        # 因此，我们按源字符串顺序遍历
        # for key, val in dic.items():
        #     if val == 1:
        #         return res.index(key)
        for i in range(len(s) - 1):
            if dic[s[i]] == 1:
                return i
        return -1


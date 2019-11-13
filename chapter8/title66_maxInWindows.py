# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/7 22:43
desc:
'''
# 思路：
# 通过两侧循环找出符合要求的最大数；
# 1）外层循环从第一个数字，依次遍历；
# 2）内层循环依次许多size个数，即range(i, i+size)，将最大的数字取出来追加到result中。

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return []
        result = []
        # 滑动窗口大于数组长度时返回空列表可以通过调试。
        if size > len(num):
            # result.append(max(num))
            return []
        if size < 1:
            return []
        for i in range(len(num)):
            if i + size <= len(num):
                temp = []
                for i in range(i, i+size):
                    temp.append(num[i])
                # print(temp)
                result.append(max(temp))
        return result

# 同样的思路可以这样解决，代码更简洁
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0:
            return []
        res = []
        for i in range(0, len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res

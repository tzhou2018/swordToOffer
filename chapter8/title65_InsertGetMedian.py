# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/5 21:36
desc:
'''

class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)
        self.nums.sort()

    def GetMedian(self):
        # write code here
        _len = len(self.nums)
        if _len % 2 == 0:
            return (self.nums[_len // 2] + self.nums[(_len - 1) // 2]) / 2.0
        else:
            return self.nums[_len // 2]

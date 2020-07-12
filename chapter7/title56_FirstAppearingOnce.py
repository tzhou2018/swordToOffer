# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/10/29 20:53
desc:
'''


# 思路：
# Insert 方法将字符流依次保存到s中，并且用字典存储每个字符出现的次数；
# FirstAppearingOnce 方法返回结果
class Solution:
    def __init__(self):
        self.s = ''
        self._dict = {}

    def FirstAppearingOnce(self):
        for item in self.s:
            if self._dict[item] == 1:
                return item
        return '#'

    def Insert(self, char):
        self.s = self.s + char
        if char not in self._dict:
            self._dict[char] = 1
        else:
            self._dict[char] = self._dict[char] + 1

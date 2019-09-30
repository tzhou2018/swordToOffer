# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        index = -1
        for i in range(len(array)):
            if array[i] & 1 != 0:
                index += 1
                array.insert(index, array.pop(i))
        return array
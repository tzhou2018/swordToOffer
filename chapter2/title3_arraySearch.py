# 有序数组；
# 思路：从左下角或者右上角开始比较
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows, cols = len(array)-1, len(array[0])
        row, col = rows, 0
        while row >= 0 and col <= cols-1:
            if (array[row][col] == target):
                return True
            elif (array[row][col] > target):
                row -= 1
            else:
                col += 1
        return False
# import numpy as np
#
# array1 = np.arange(12).reshape(3, 4)
# rows, cols = array1.shape
# print(rows, cols)



# -*- coding:utf-8 -*-
# 方法1
# 遍历给定的数组，求出最小值
# class Solution:
#   def minNumberInRotateArray(self, rotateArray):
#        # write code here
#        arrLong = len(rotateArray)
#        rever = rotateArray[0]
#        for i in range(arrLong):
#            if rotateArray[i] < rever:
#                rever = rotateArray[i]
#
#        return rever
# 方法2
# 折半查找
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        p = 0
        q = len(rotateArray) - 1
        mid = p
        while rotateArray[p] >= rotateArray[q]:
            if q - p == 1:
                mid = q
                break
            mid = int(q + p) / 2
            if rotateArray[p] <= rotateArray[mid]:
                p = mid
            elif rotateArray[q] >= rotateArray[mid]:
                q = mid
        return rotateArray[mid]

# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/10 14:45
desc:
'''


# 思路： 使用“”“”“"二分法"解决问题
class Solution(object):
    def getNumberSameAsIndex(self, nums):
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < mid:
                low = mid + 1
            else:
                assert nums[mid] >= mid
                high = mid
            return low if nums[low] == low else -1


if __name__ == '__main__':
    print(Solution().getNumberSameAsIndex([-3, -1, 1, 3, 5]))

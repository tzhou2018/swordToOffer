# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/10 14:46
desc:
'''


# 思路： 使用“”“”“"二分法"解决问题
class Solution(object):
    def getMissingNumber(self, nums):
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > mid:
                high = mid - 1
            else:

                low = mid + 1
        return low


if __name__ == '__main__':
    print(Solution().getMissingNumber([0, 1, 2, 4]))

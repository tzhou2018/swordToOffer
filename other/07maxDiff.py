# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/15 13:13
desc:
'''
class Solution:
    def maxdiff(self, nums):
        if not nums:
            return None

        min_value = nums[0]
        max_value = 0
        for i in range(1, len(nums)):
            min_value = min(min_value, nums[i])
            max_value = max(max_value, nums[i] - min_value)
        return max_value


if __name__ == '__main__':
    print(Solution().maxdiff([9, 11, 8, 5, 7, 12, 16, 15]))

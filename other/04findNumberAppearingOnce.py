# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/9 17:21
desc:
'''


# 思路：限制在 O(1) 空间复杂度，那就只有通过二进制，一位一位去看了。
class Solution:
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
                    # print("count:", count)
            # count 能取余3，说明数组中唯一存在的那个数在该位上不为零
            if count % 3:
                res += 1 << i
        return res


if __name__ == '__main__':
    print(Solution().findNumberAppearingOnce([1, 1, 1, 3]))

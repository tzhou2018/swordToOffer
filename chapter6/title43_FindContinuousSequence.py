# -*- coding:utf-8 -*-
# 解题思路：给出和为tsum，首先所要求的的是一个连续序列，因为将1~tsum作为一个序列，计算长度_len.
# 将i,j分别作为指向前后滑动窗口的左右指针，如果此时窗口内的序列和大于tsum，则i向右滑动一个位置；
# 否则，j向右滑动一个位置
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if not tsum:
            return []
        i, j = 1, 2
        _len = (tsum + 1)//2
        _sum = i + j
        result = []
        # 由于至少包括两个数， 因为这里循环条件设为 i<_len
        while i < _len:
            if _sum == tsum:
                result.append(range(i, j + 1))
            while _sum > tsum and i < _len:
                _sum -= i
                i += 1
                if _sum ==tsum:
                    result.append(range(i, j+1))
            j += 1
            _sum += j
        return result
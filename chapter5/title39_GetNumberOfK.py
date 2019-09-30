# 方法 1：遍历所给数组，直接比较
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        # high = len(data) -1
        # low = 0
        # mid = (low + high) // 2
        # while low < high:
        #     if data[mid] >= k:
        count = 0
        for i in range(len(data)):
            if data[i] == k:
                count += 1
        return count
# 方法 2：由于是有序数组，那么相同的数字一定是排列在一起，
# 因此，我们只需找到k的前后索引便可以得出结果
def GetNumberOfK(data, k):
    if not data:
        return 0
    left = 0
    right = len(data) - 1
    left_k = get_left(data, k, left, right)
    right_k = get_right(data, k, left, right)
    return right_k - left_k + 1
def get_left(data, k, left, right):
    while left <= right:
        mid = (left + right) // 2
        if data[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    print("left",left)
    return left
def get_right(data, k, left, right):
    while left <= right:
        mid = (left + right) //2
        if data[mid] <= k:
            left = mid + 1
        else:
            right = mid - 1
    print("right:",right)
    return right
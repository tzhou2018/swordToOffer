# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/5 21:36
desc:
'''


# 方法1
class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)
        self.nums.sort()

    def GetMedian(self):
        # write code here
        _len = len(self.nums)
        if _len % 2 == 0:
            return (self.nums[_len // 2] + self.nums[(_len - 1) // 2]) / 2.0
        else:
            return self.nums[_len // 2]


# 方法2
# 建立两个堆来实现
# 一个大根堆，一个是小根堆。大根堆中含有接收到的所有数中较小的一半，
# 这个堆顶就是较小一半的数中最大的那个。
# 小根堆中含有所有书中较大的一半，并且按小根堆的方式组织起来，那么这个堆的堆顶就是较大一半的数。
# 当两堆中元素的个数差超过大于1时进行调整。
# 整个过程可以在O(logn)中完成，获取中位数O(1)

import heapq


class Solution1:
    def __index__(self):
        self.minHeap = heapq.heapify([])
        self.maxHeap = heapq.heapify([])

    def insert(self, e):
        if self.maxHeap[0] >= e:
            heapq.heappush(self.maxHeap, -e)
        else:
            heapq.heappush(self.minHeap, e)
        diffSize = len(self.minHeap) - len(self.maxHeap)
        if diffSize > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif diffSize < -1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def getMidian(self):
        diffSize = len(self.minHeap) - len(self.maxHeap)
        minPop = self.minHeap[0]
        maxPop = -self.maxHeap[0]
        if diffSize == 0:
            return (minPop + maxPop) / 2
        elif diffSize > 0:
            return minPop
        else:
            return maxPop

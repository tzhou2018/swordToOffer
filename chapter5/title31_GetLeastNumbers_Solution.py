# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
# 则最小的4个数字是1,2,3,4,。

# 方法 1
# 使用python内置的排序方法
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        else:
            tinput.sort()
            return tinput[:k]

# 方法 2
# 使用堆队列算法
import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        ans = []
        if tinput is None or k < 1 or k > len(tinput):
            return ans
        for item in tinput:
            heapq.heappush(ans, item)
        return [heapq.heappop(ans) for _ in range(k)]
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


class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        ans = []
        if tinput is None or k < 1 or k > len(tinput):
            return ans
        for item in tinput:
            heapq.heappush(ans, item)
        return [heapq.heappop(ans) for _ in range(k)]


# 方法3
# 使用冒泡排序
class Solution3:
    def bublleSort(self, tinput, k):
        if not tinput or k < 1 or k > len(tinput):
            return []
        for i in range(k):
            for j in range(len(tinput) - 1, i, -1):
                if tinput[j] < tinput[j - 1]:
                    tinput[j], tinput[j - 1] = tinput[j - 1], tinput[j]
        return tinput[:k]


if __name__ == '__main__':
    arr = [8, 2, 4, 3, 1, 5, 1]
    print(Solution1().GetLeastNumbers_Solution(arr, 5))
    print(arr)
    print(Solution3().bublleSort(arr, 5))

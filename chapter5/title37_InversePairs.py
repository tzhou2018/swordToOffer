# 数组中的逆序对
# 解题思路：实质是考察归并排序
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        low = 0
        high = len(data) - 1
        # mid = (low+high) // 2
        temp = data[:]
        return self.Merge(data, temp, low, high) % 1000000007
    # temp 作为辅助数组，每次将temp中基本有序的元素赋值给 data，data赋值给temp继续归并
    def Merge(self, data, temp, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        left = self.Merge(temp, data, low, mid)
        right = self.Merge(temp, data, mid + 1, high)

        count = 0
        i = low
        j = mid + 1
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                count += mid - i + 1
                j += 1
            index += 1
        # 若第一个表未检测完， 复制
        if i <= mid:
            temp[index:index + (mid - i + 1)] = data[i:mid + 1]
        # 若第二个表未检测完， 复制
        if j <= high:
            temp[index:index + (high - j + 1)] = data[j:high + 1]
        return count + left + right
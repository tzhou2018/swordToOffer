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
        return self.merSort(data, low, high) % 1000000007

    def merSort(self, arr, low, high):
        if low >= high:
            return 0
        mid = low + (high - low) // 2
        return self.merSort(arr, low, mid) + \
               self.merSort(arr, mid + 1, high) + \
               self.Merge(arr, low, mid, high)

    # temp 作为辅助数组，每次将temp中基本有序的元素赋值给 data，
    # data赋值给temp继续归并
    def Merge(self, data, low, mid, high):

        temp = []
        count = 0
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp.append(data[i])
                i += 1
            else:
                temp.append(data[j])
                count += mid - i + 1
                j += 1
            # index += 1
        # 若第一个表未检测完， 复制
        while i <= mid:
            temp.append(data[i])
            i += 1
        # 若第二个表未检测完， 复制
        while j <= high:
            temp.append(data[j])
            j += 1
        data[low:high + 1] = temp
        return count


if __name__ == '__main__':
    print(Solution().InversePairs([7, 5, 6, 4]))

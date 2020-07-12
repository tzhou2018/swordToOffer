# -*- coding:utf-8 -*-
# 方法1
# 遍历给定的数组，求出最小值
# class Solution:
#   def minNumberInRotateArray(self, rotateArray):
#        # write code here
#        arrLong = len(rotateArray)
#        rever = rotateArray[0]
#        for i in range(arrLong):
#            if rotateArray[i] < rever:
#                rever = rotateArray[i]
#
#        return rever
# 方法2
# 折半查找
# 注意：当第一个指针p，第二个指针q以及min所指向的三个元素都相等时，
# 只能使用顺序查找；(不考虑此种情况，在牛客网提交的代码依然可以通过，
# 为了严谨考虑，在这里加上这种情况。)
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        p = 0
        q = len(rotateArray) - 1
        mid = p
        while rotateArray[p] >= rotateArray[q]:
            if q - p == 1:
                mid = q
                break
            mid = (q + p) // 2
            # 这种情况只能顺序查找
            if rotateArray[p] == rotateArray[q] and \
                    rotateArray[q] == rotateArray[mid]:
                return self.minInOrder(rotateArray, p, q)
            if rotateArray[p] <= rotateArray[mid]:
                p = mid
            elif rotateArray[q] >= rotateArray[mid]:
                q = mid
        return rotateArray[mid]

    def minInOrder(self, rotateArray, p, q):
        result = rotateArray[p]
        for i in range(p + 1, q + 1):
            if rotateArray[i] < result:
                result = rotateArray[i]
        return result


if __name__ == '__main__':
    # print(Solution().minNumberInRotateArray([1, 0, 1, 1, 1]))
    print(Solution().minNumberInRotateArray([3,4,5,1,2]))

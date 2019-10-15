# -*- coding:utf-8 -*-
# 方法 1
# 思路：遍历所给数组，将符合条件的数字对以列表形式存储在res中，
# 之后再根据所给条件进行判断，输出成绩最小的数字对
# 注意： 在判断之前需要先判断res是否为空。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        res = []
        for i in array:
            if (tsum - i) in array:
               res.append([i, tsum - i])
        multi = 999999
        minNum = []
        if res:
            for item in res:
                if item[0] * item[1] < multi:
                    multi = item[0] * item[1]
                    minNum = item
        return minNum


# 方法 2
# -*- coding:utf-8 -*-
# 思路：递增的序列，选择序列的首尾元素为起始元素进行判断，
# 按所给的元素调整首尾元素位置，满足条件的第一对元素即是所求序列。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        i, j = 0, len(array) - 1
        while i < j:
            _sum = array[i] + array[j]
            # 如果和大于tsum，选择较大数字前面的数字
            if _sum > tsum:
                j -= 1
            # 如果和小于tsum，选择较小数字后面的数字
            elif _sum < tsum:
                i += 1
            else:
                return [array[i], array[j]]
        return []
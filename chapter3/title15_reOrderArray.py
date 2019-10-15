# -*- coding:utf-8 -*-
# 思路：
# 借助List insert(),挨个判断所给数组array中的元素，
# 索引index记录要插入数据的位置（从第一个位置开始），
# 当奇数元素放置好后，偶数元素对应地也会放置好。
class Solution:
    def reOrderArray(self, array):
        # write code here
        index = -1
        for i in range(len(array)):
            if array[i] & 1 != 0:
                index += 1
                array.insert(index, array.pop(i))
        return array
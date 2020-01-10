# -*- coding:utf-8 -*-
# 方法 1
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


# 方法 2
# 参考牛客网上给的解法：
# 在首尾各放一个指针，当首指针指向的当前匀速为偶数时暂停；
# 当尾指针指向的当前元素为奇数时暂停；
# 交换首尾执行的元素；
# 以此循环，直至首尾指针指向的元素重合或者首指针的索引大于尾指针的索引；

# 注意：此种解法满足条件，但是未能在牛客网上通过。
class Solution:
    def reOrderArray(self, array):
        begin, end = 0, len(array) - 1

        while end > begin:
            while end > begin and array[begin] & 1 != 0:
                begin = begin + 1
            while end > begin and array[end] & 1 == 0:
                end -= 1
            if end > begin:
                array[begin], array[end] = array[end], array[begin]

        return array

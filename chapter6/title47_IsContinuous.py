# -*- coding:utf-8 -*-
# 方法 1
# 思路：1）对所给序列进行排序； 2）统计有序序列中元素0的个数；
# 3）统计非零元素序列间可以排成顺子的所需间隙；4）若所需间隙小于0元素的数目，则满足要求
class Solution:
    def IsContinuous(self, numbers):

        if not numbers:
            return False
        numbers.sort()
        zero_nums = numbers.count(0)
        i = zero_nums
        gaps = 0
        for j in range(i, len(numbers) - 1):
            if numbers[j] == numbers[j + 1]:
                return False
            else:
                gaps += numbers[j + 1] - numbers[j] - 1

        if gaps <= zero_nums:
            return True
        else:
            return False


# 方法 2
# 思路：前两步同方法1；3）max， min分别记录最大值 最小值；
# 4）需满足条件：max-min<=4,除零外没有重复元素。
class Solution1:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False

        new_list = [i for i in numbers if i > 0]
        new_list.sort()
        min, max = new_list[0], new_list[-1]
        for j in range(len(new_list) - 1):
            if (new_list[j + 1] - new_list[j]) == 0:
                return False
        if (max - min) <= 4:
            return True
        else:
            return False

    # 对上述方法 IsContinuous 进行修改，不适用额外空间
    def test(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        # 找到第一个部位零的位置
        i = numbers.count(0)
        # 找出除零之后的最大值、最小值
        _min = numbers[i]
        _max = numbers[-1]
        for j in range(j, len(numbers) - 1):
            if numbers[j + 1] - numbers[j] == 0:
                return False
        if (_max - _min) <= 4:
            return True

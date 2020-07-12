# 方法1
# 首先对所给的元素进行去重处理，之后统计这些元素各自出现多少次，符合条件的元素返回
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbersSet = list(set(numbers))

        for i in numbersSet:
            count = 0
            for j in numbers:
                if i == j:
                    count += 1
            if count > len(numbers) / 2:
                return i
        return 0


# 方法 2
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        ans, times = 0, 0
        for item in numbers:
            # 如果times为0，则把下一个元素赋值给ans，并将次数设为1
            if times == 0:
                ans = item
                times = 1
            # 如果ans与下一个元素的值相等，则将items的次数加1
            elif ans == item:
                times += 1
            # 如果ans与下一个元素的值不相等，则将times的次数减1
            else:
                times -= 1
        return ans if numbers.count(ans) * 2 > len(numbers) else 0

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) <= 1:
            return False
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] == numbers[j]:
                    # duplication.append(numbers[i])
                    duplication[0] = numbers[i]
                    return True
        return False
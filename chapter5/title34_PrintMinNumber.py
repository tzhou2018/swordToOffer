# 把数组排成最小的数
# 方法 1
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, number):
        # write code here
        import itertools
        if not number:
            return []
        num = map(str, number)
        k = itertools.permutations(num)
        result = []
        for i in k:
            result.append(int(''.join(i)))
        result = list(set(result))
        result.sort()
        return result[0]


# 方法2
class Solution1:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        len_num = len(numbers)
        # 每次循环确定一个元素
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len_num):
                tmp = int(numbers[i] + numbers[j]) - int(numbers[j] + numbers[i])
                if tmp > 0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)



if __name__ == '__main__':
    print(Solution().PrintMinNumber([3, 21, 321]))

# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/12 22:00
desc:
'''
# 方法1：动态规划
# 一般可以使用动态规划求解的问题有如下四个特点：
# 1）求一个问题的最优解（可以是最大值或者时最小值）
# 2）整体entity的最优解是依赖于各个子问题的最优解
# 3）这些小问题还有相互重叠的更小的问题；
# 4）从上往下分析，从下往上求解；即：
#   由于子问题在分解大问题的过程中重复出现，为了避免重复求解子问题，
#   我们可以用从下往上的顺序先求解子问题的最优解，并存储下来，再以此为基础求去
#   最大问题的最优解。
class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        products = [0, 1, 2, 3]
        for i in range(4, number + 1):
            max_1 = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                max_1 = max(max_1, product)
            products.append(max_1)
        return products.pop()


if __name__ == '__main__':
    maxRes = Solution().cutRope(6)
    print(maxRes)


# 方法2: 贪婪算法
def cutRope(number):
    if number < 2:
        return 0
    if number == 2:
        return 1
    if number == 3:
        return 2
    # 尽可能多地减去长度为3的绳子段

    timesOf3 = number // 3
    # 当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段。
    # 此时更好的方法是把绳子剪成长度为2的两段，因为2 * 2 > 3 * 1。
    if number - timesOf3 * 3 == 1:
        timesOf3 -= 1
    timesOf2 = (number - timesOf3 * 3) // 2
    return int(pow(3, timesOf3) * pow(2, timesOf2))

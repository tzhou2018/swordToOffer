# 连续子数组最大和
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # ans 为最终的返回值，即保存最大连续子序列和；
        # tmp表示加上当前number之后的子数组最大和
        ans, tmp = -999999, 0
        for number in array:
            if tmp > 0:
                tmp += number
            else:
                tmp = number
            if tmp > ans:
                ans = tmp
        return ans


# 方法 2
# 动态规划问题

def fun(array):
    # res 记录当前所有子数组和的最大值
    # 包含array[i]的连续数组的最大值
    res = array[0]
    temp = array[0]
    for i in range(1, len(array)):
        temp = max(temp + array[i], array[i])
        res = max(temp, res)
    return res

# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/10/28 18:59
desc:
'''


# 方法1
# 思路：
# 观察题目，若是可以使用除法，那么我们可以这样来构建B数组：
# B[i]=A[0]*A[1]*...*A[i-1]*A[i]*A[i+1]*...*A[n-1]/A[i].
# 考虑到不能使用除法，我们用两层循环构建乘积数组 B;
# 1)在外层循环中将A中的元素依次取出来；
# 2）内层计算A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]；
class Solution:
    def multiply(self, A):
        if not A:
            return None
        lenA = len(A)
        B = [0] * lenA
        for i in range(lenA):
            temp = 1
            for j in range(lenA):
                if i != j:
                    temp *= A[j]
            B[i] = temp
        return B


# 方法 2
# 思路：
# B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]；
# 可以将目标数组B分为两部分计算：
# C[i] = C[i-1] * A[i-1]= A[0]*A[1]*...*A[i-1]
# D[i] = D[i+1] * A[i+1]= A[i+1]*...*A[n-1]
# 如果将B当做二维数组，那么C[i]表示的为下三角，D[i]为上三角，
# 对角线元素值用 1 表示。
class Solution:
    def multiply(self, A):
        if not A:
            return None
        lenA = len(A)
        B = [0] * lenA
        B[0] = 1
        for i in range(1, lenA):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        for j in range(lenA - 2, -1, -1):
            temp *= A[j + 1]
            B[j] *= temp
        return B

    def test(self,A):
        if not A:
            return None
        lenA = len(A)
        B = [0] * lenA
        B[0] = 1
        for i in range(1,lenA):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for j in range(lenA -2,-1,-1):
            temp *= A[j+1]
            B[j] *= temp
        pass

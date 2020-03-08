# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/10 21:58
desc:
'''
# 思路
# 同上一道题，采用回溯算法；
# 从坐标(0, 0)开始行动。当它准备进入坐标为(i,j)的格子时，
# 通过检查坐标的数位和来判断机器人是否能够进入。
# 如果机器人能够进入坐标为(i,j)的格子，则再判断它能否进入4个相邻的格子。
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        print(matrix)
        return self.findGrid(threshold, rows, cols, matrix, 0, 0)

    def findGrid(self, threshold, rows, cols, matrix, i, j):
        count = 0
        if 0 <= i < rows and 0 <= j < cols and \
                sum(map(int, str(i) + str(j))) <= threshold and \
                matrix[i][j] == 0:
            matrix[i][j] = 1
            count = 1 + self.findGrid(threshold, rows, cols, matrix, i, j + 1) \
                    + self.findGrid(threshold, rows, cols, matrix, i, j - 1) \
                    + self.findGrid(threshold, rows, cols, matrix, i + 1, j) \
                    + self.findGrid(threshold, rows, cols, matrix, i - 1, j)
            # print(count)
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(4,3,4))
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/12/26 22:17
desc:
'''


# 思路:
# 礼物要么来自下边一格，要么来自右边一格，两者各取最大。
# 需要判断边界情况，利用一维初始化数组完成动态规划；
# 记f(x,y)为到达该坐标时拿到礼物的最大值，
# f(x,y) = max(f(x-1,y),f(x,y-1)) + gift[i,j]
class Solution(object):
    def getMaxValue(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return 0
        initList = [0 for _ in range(cols)]
        initList[0] = grid[0][0]
        for i in range(1, cols):
            initList[i] = grid[0][i] + initList[i - 1]
        # print(initList)
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    initList[j] += grid[i][0]
                else:
                    initList[j] = max(initList[j], initList[i - 1]) + grid[i][j]
        # print(initList)
        # return initList[cols - 1]
        return initList


if __name__ == '__main__':
    testList = [[2, 3, 20], [1, 7, 1], [4, 6, 1]]
    print(Solution().getMaxValue(testList))

# 题目描述
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

# 方法 1
# 思路：
#
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return ans

    # 利用 * 号操作符，可以将二维数组中每一列的元素取出，类似于拍扁。
    def turn(self, matrix):
        return list(map(list, zip(*matrix)))[::-1]


# 方法 2
# 思路：
# 采用最原始的方法，循环打印；打印一圈分为四步：
# 1)从左至右；2）从上至下；3）从右至左；4）从下至上；

class Solution2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        start = 0
        while (cols > start * 2 and rows > start * 2):
            ans = []
            result.extend(self.printMatrixCircle(ans, matrix, cols, rows, start))
            start += 1
        return result

    def printMatrixCircle(self, ans, matrix, cols, rows, start):
        endX = cols - 1 - start
        # print(endX)
        endY = rows - 1 - start
        for i in range(start, endX + 1):
            ans.append(matrix[start][i])
        if start < endY:
            for i in range(start + 1, endY + 1):
                ans.append(matrix[i][endX])
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                ans.append(matrix[endY][i])
        if start < endX and start < endY:
            for i in range(endY - 1, start, -1):
                ans.append(matrix[i][start])
        return ans


# 方法3
# 同方法2，参考程序员面试指南，更容易理解。
# 设计一种逻辑容易理解，代码易于实现转圈的遍历方式。
# 知道矩阵的左上顶点与右下顶点即可确定一个矩阵，
# 然后这两个点收缩，直至左上顶点坐标大于右下顶点坐标。
class Solution3:
    def printMatrix(self, matrix):
        # 左上顶点坐标
        tr, tc = 0, 0
        dr, dc = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while tr <= dr and tc <= dc:
            self.printEdge(matrix, res, tr, tc, dr, dc)
            tr += 1
            tc += 1
            dr -= 1
            dc -= 1
        return res

    def printEdge(self, matrix, res, tr, tc, dr, dc):
        # 只有一行
        if tr == dr:
            for i in range(tc, dc + 1):
                res.append(matrix[tr][i])
        # 只有一列
        elif tc == dc:
            for i in range(tr, dr + 1):
                res.append(matrix[i][tc])
        # 正常
        else:
            curC = tc
            curR = tr
            while curC != dc:
                res.append(matrix[tr][curC])
                curC += 1
            while curR != dr:
                res.append(matrix[curR][dc])
                curR += 1
            while curC != tc:
                res.append(matrix[dr][curC])
                curC -= 1
            while curR != tr:
                res.append(matrix[curR][tc])
                curR -= 1


if __name__ == '__main__':
    solution = Solution3()
    import numpy as np

    arr1 = np.arange(1, 17).reshape(4, 4)
    list1 = arr1.tolist()
    print(list1)
    print(solution.printMatrix(list1))

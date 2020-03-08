# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/10 10:39
desc:
'''
# 思路：
# 1) hasPath 方法挨个遍历matrix中的元素，找出第一个符合要求的元素；
# 2) find 判断当前元素 matrix[index] 是否满足path。如果满足，
# 就将当前的tem[index]置位False，
#   下次判断时，不用考虑这个元素；之后使用递归依次判断当前元素的上下左右元素是否满足条件。
#
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        tmp = [True] * rows * cols
        for i in range(rows):
            for j in range(cols):
                if self.find(matrix, rows, cols, i, j, path, tmp):
                    print("符合要求")
                    print(tmp)
                    return True
        print(tmp)
        return False

    def find(self, matrix, rows, cols, i, j, path, tmp):
        if not path:
            return True
        index = i * cols + j
        if i < 0 or i >= rows or j < 0 or j >= cols \
                or matrix[index] != path[0] or not tmp[index]:
            return False
        tmp[index] = False
        if self.find(matrix, rows, cols, i + 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i - 1, j, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j - 1, path[1:], tmp) \
                or self.find(matrix, rows, cols, i, j + 1, path[1:], tmp):
            return True
        tmp[index] = True
        return False

if __name__ == '__main__':
    solution = Solution()
    matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e' ]
    solution.hasPath(matrix, 3, 4,"bcced")
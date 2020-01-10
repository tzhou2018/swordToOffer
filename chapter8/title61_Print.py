# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/4 19:32
desc:
'''


# 思路：
# 采用广度优先遍历。
# 1)从根节点开始，将每层的结点存储在curLayerNodes中；
# 2)偶数层进行reverse操作。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        ans = []
        shift = False
        if not pRoot:
            return []
        curLayerNodes = [pRoot]
        while curLayerNodes:
            curLayerValues = []
            nextLayerNodes = []
            while curLayerNodes:
                node = curLayerNodes.pop(0)
                curLayerValues.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            if shift:
                ans.append(curLayerValues[::-1])
            else:
                ans.append(curLayerValues)
            shift = not shift
        return ans



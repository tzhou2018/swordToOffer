# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：从平衡二叉树的概念入手，递归判断
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeeDepth(pRoot.left) - self.TreeeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeeDepth(self, pRoot):
        if pRoot == None:
            return 0
        nLeft = self.TreeeDepth(pRoot.left)
        nRight = self.TreeeDepth(pRoot.right)
        return max(nLeft, nRight) + 1


# 另一种思路
# 通过结点返回信息：1）是否平衡 2）高度
# 便可确定这棵树是否是平衡的
class ReturnType:
    def __init__(self, isB, h):
        self.isB = isB
        self.h = h


def isBBT(root, h):
    if not root:
        return ReturnType(True, h)
    left = isBBT(root.left, h + 1)
    if not left.isB:
        return ReturnType(False, h)
    right = isBBT(root.right, h + 1)
    if not right.isB:
        return ReturnType(False, h)
    if abs(left.h - right.h) > 1:
        return ReturnType(False, max(left.h, right.h))
    return ReturnType(True, max(left.h, right.h))

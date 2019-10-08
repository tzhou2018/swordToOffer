# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
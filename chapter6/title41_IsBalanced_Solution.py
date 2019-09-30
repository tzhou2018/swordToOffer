# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
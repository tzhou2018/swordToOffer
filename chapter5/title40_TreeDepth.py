# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        leftN = self.TreeDepth(pRoot.left)
        rightN = self.TreeDepth(pRoot.right)
        return (leftN if leftN > rightN else rightN) + 1
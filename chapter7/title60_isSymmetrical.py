# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/1 20:19
desc:
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路：
# 1）首先判断根节点以及根结点的左子树，右子树；
# 2）左子树的左子树与右子树的右子树相同；
# 3）左子树的右子树与右子树的左子树相同。
# 也就是针对前序遍历算法的对称遍历算法

class Solution:
    def isSymmetrical(self, pRoot):

        return self.isSymBT(pRoot, pRoot)
    def isSymBT(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.isSymBT(tree1.left, tree2.right) and \
            self.isSymBT(tree1.right, tree2.left)
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/5 21:03
desc:
'''


# 思路:
# 二叉搜索树按中序遍历后刚好就是所要求的序列，此时找到第k个结点就行。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k <= 0:
            return None
        ans = []
        self.minOrder(pRoot, ans)
        if len(ans) < k:
            return None
        return ans[k - 1]

    # 中序遍历
    def minOrder(self, root, ans):
        if not root:
            return None
        if root.left:
            self.minOrder(root.left, ans)
        ans.append(root)
        if root.right:
            self.minOrder(root.right, ans)

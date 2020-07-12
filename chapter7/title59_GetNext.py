# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/1 19:38
desc:
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# 参考牛客网：https://www.nowcoder.com/profile/777988/codeBookDetail?submissionId=12620199
# 思路：
# 分为两大类：
# 1）有右子树，那么下一个结点就是右子树最左边的点；
# 2）没有右子树，也可以分为两类:
#       a)如果是父节点的左孩子，那么父节点就是下一个结点；
#       b)如果是父节点的右孩子，那么找他父节点的父节点的父节点...直至当前节点为父节点的左孩子。
# 到最后都没有，则返回空.
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            parent = pNode.next
            while parent and parent.left != pNode:
                pNode = parent
                parent = parent.next
            return parent
            # 另一种写法
            # while pNode.next:
            #     if pNode == pNode.next.left:
            #         return pNode.next
            #     pNode = pNode.next

        # return None

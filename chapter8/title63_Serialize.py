# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/5 19:43
desc:
'''
# 思路
# 1)对于序列化：使用先序遍历，递归将二叉树的值转化为字符，
# 并且将每个字符用逗号隔开。对于空节点用“‘#’代替。
# 2)对于反序列化：同样使用前序顺序。先将当前的结点设为None，
# 若是当前节点的值为‘#’，则返回空值，否则递归。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + \
               self.Serialize(root.left) + ','\
               +self.Serialize(root.right)
    def Deserialize(self, s):
        _list = s.split(',')
        return self.derserializeTree(_list)
    def derserializeTree(self, _list):
        if not _list:
            return None
        val = _list.pop(0)
        node = None
        # 先序遍历
        if val != '#':
            node = TreeNode(int(val))
            node.left = self.derserializeTree(_list)
            node.right = self.derserializeTree(_list)
        return node
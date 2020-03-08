# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/8 21:05
desc:
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 一般方法，有重复计算
    def isBalanced(self, root):
        if not root:
            return True
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        diff = left - right
        print("diff:", diff)
        if diff < -1 or diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return left + 1 if left > right else right + 1

    # plus 检测，采用后序遍历，省去重复计算
    flag = 1

    def plusIsBalanced(self, root):
        if not root:
            return True
        self._dfs(root)
        return self.flag

    def _dfs(self, node):
        if not node:
            return 0
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        if abs(left - right) > 1:
            self.flag = 0
        return max(left, right) + 1


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


# 先序遍历二叉树
def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


# 中序遍历二叉树
def midOrdBT(root):
    if not root:
        return "#"
    midOrdBT(root.left)
    print(root.val, end="\t")
    midOrdBT(root.right)


if __name__ == '__main__':
    # llist = ['1', '2', '3', '#', '4', '5', '6']
    llist = [8, '#', 10, '#', '#', 9, 11]
    root = listCreatTree(None, llist, 0)
    p = root
    print(".............................")
    preOrderBT(root)
    print()
    midOrdBT(p)
    print(Solution().isBalanced(root))
    print(Solution().plusIsBalanced(root))

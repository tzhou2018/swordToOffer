# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        # 查找根节点在中序遍历结果中的位置
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1 + pos], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    print(Solution().reConstructBinaryTree(pre, tin).val)
    print(Solution().reConstructBinaryTree(pre, tin).right)
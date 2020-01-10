# 解题思路
# BST 的后序序列和合法序列是，对于一个序列S，最后一个元素是X（也就是根元素），
# 如果去除最后一个元素的序列为T，那么T满足：T可以分为两段，前一段（左子树）小于X，
# 后一段（右子树）大于X，并且这两段（子树）都是合法的后序序列。
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        # 在序列前面找到第一个比根节点大的位置i
        # i之后为右子树
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        # 从位置i到len(sequence)-1 的所有元素都比根节点的值大
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        left, right = True, True
        if len(sequence[0:i]) > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        # 注意：序列中最后一位是根节点，不可以取到
        if len(sequence[i:-1]) > 0:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

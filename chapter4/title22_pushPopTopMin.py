# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
# 解题思路
# 使用两个列表来模拟栈，每次入栈之前使得每一个栈中最小的元素存储在 minStack 顶部
class Solution:
    def __init__(self):
        self.data = []
        self.minStack = []

    def push(self, node):
        if not self.minStack:
            self.minStack.append(node)
        if self.minStack[-1] > node:
            self.minStack.append(node)

        self.data.append(node)

    def pop(self):
        if self.minStack[-1] == self.data[-1]:
            self.minStack.pop()
        self.data.pop()

    def top(self):
        return self.data[-1]

    def min(self):
        return self.minStack[-1]

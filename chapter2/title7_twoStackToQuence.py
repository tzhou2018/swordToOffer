# -*- coding:utf-8 -*-
# 思路：注意栈和队列的性质。
# 栈是先进后出且只能从栈顶出；队列则为先进先出，一般都是从队头出
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        # stack1,stack2调用pop()为python内置函数
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
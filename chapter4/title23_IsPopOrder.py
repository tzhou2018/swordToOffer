
# 解题思路
# 借用一个辅助栈，遍历压栈顺序，先将第一个元素放入到辅助栈中，然后判断辅助栈栈顶元素是否与出栈序列第一个元素相等；
# 若相等，将辅助栈栈顶与出栈序列第一个元素弹出；循环依次比较；
# 若是遍历入栈序列结束后，辅助栈还不为空，说明弹出序列不是该栈的弹出序列。
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not popV or len(pushV) != len(popV):
            return False
        stack = []
        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack:
            return False
        else:
            return True

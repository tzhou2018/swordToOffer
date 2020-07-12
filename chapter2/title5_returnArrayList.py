# 这个示例完整的创建一个链表，并且去遍历从尾到头打印出来
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 在牛客网上线上编程，我们只需书写这一段就行
class Solution:
    # 返回从尾部到头部的列表值序列
    def printListFromTailToHead(self, listNode):
        _stack = []
        while listNode:
            _stack.insert(0, listNode.val)
            listNode = listNode.next
        return _stack


if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(2, 11):
        node = ListNode(i)
        p.next = node
        p = node
    print(Solution().printListFromTailToHead(pHead))

# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/10/29 21:21
desc:
'''
# 思路：
# 遍历链表，环的存在就是遍历遇见第一个重复的即为入口结点.
# 下面给出一个完整的示例，创建十个结点组成的环形链表。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p = pHead
        nodeList = []
        while p:
            if p in nodeList:
                return p
            else:
                nodeList.append(p)
            p = p.next
        return None
if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(10):
        node = ListNode(i)
        p.next = node
        p = node
    p.next = pHead
    # while pHead:
    #     print(pHead.val)
    #     pHead = pHead.next
    print(Solution().EntryNodeOfLoop(pHead))


# 方法2
# 参考剑指offer上给的解法
# 1.判断环
# 2.计算环内结点；
# 3.头指针p1先移动k-1
# 4.头指针p1，p2同时移动，相遇的结点即为入口结点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        count = self.countNode(pHead)
        print(count)
        if count:
            return self.FindKthToTail(pHead, count)

    # 判断是否有环，并计算环内结点数目
    def countNode(self, pHead):
        if not pHead:
            return None
        p = pHead
        q = pHead
        while p.next and q.next.next:

            p = p.next
            q = q.next.next
            if p.val == q.val:
                count = 0
                val = p.val
                while p:
                    p = p.next
                    count += 1
                    if p.val == val:
                        return count
        return None

    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        p1 = head
        for i in range(k):
            if p1:
                p1 = p1.next
            else:
                return None
        p2 = head
        while p1:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
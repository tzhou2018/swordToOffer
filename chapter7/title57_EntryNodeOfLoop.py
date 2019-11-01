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
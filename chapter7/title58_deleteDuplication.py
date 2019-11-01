# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/10/30 20:14
desc:
'''


# 思路：
# 为了便于操作，我们这里加上头结点 first=ListNode(-1);
# 指针 cur 始终执向当前节点；
# 为了便于操作，引入 last 指针，last 始终置于cur之前；

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)
        first.next = pHead
        cur = pHead
        last = first
        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                last.next = cur
            else:
                cur = cur.next
                last = last.next
        return first.next


def create_linked_list(arr=None):
    """
    根据输入的数组建立一个链表
    :param arr: 输入的数组
    :return: 链表的头指针
    """
    pHead = ListNode(arr[0])
    p = pHead
    for i in arr[1:]:
        node = ListNode(i)
        p.next = node
        p = node
    return pHead


def print_linked_list(pHead):
    """
    打印链表
    :param pHead: 链表的头结点
    :return: None
    """
    p = pHead
    while p:
        print(p.val, end='\t')
        p = p.next
    print()


if __name__ == '__main__':
    pHead = create_linked_list(arr=[1, 1, 3, 4, 5, 5, 6])
    print_linked_list(pHead)
    new_pHead = Solution().deleteDuplication(pHead)
    print_linked_list(new_pHead)

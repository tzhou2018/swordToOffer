# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        p1 = head
        for i in range(k - 1):
            if p1.next:
                p1 = p1.next
            else:
                return None
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2

    # 另一种方式，先让 p1 走  k 步
    def FindKthToTail1(self, head, k):
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
            p1 = p1.next
            p2 = p2.next
        return p2


if __name__ == '__main__':
    phead = ListNode(10)
    p = phead
    for i in range(9, 0, -1):
        node = ListNode(i)
        p.next = node
        p = node
    print(Solution().FindKthToTail1(phead, 3).val)

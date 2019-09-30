class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 采用头插法
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        # 不带头结点
        # p_reverse = None
        # while pHead:
        #     p_next = pHead.next
        #     pHead.next = p_reverse
        #     p_reverse = pHead
        #     pHead = p_next
        # return p_reverse
        # 带头结点
        p_reverse = ListNode(0)
        p_reverse.next = None
        while pHead:
            p = pHead.next
            pHead.next = p_reverse.next
            p_reverse.next = pHead
            pHead = p
        return p_reverse.next

if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(2, 11):
        node = ListNode(i)
        p.next = node
        p = node
    p = pHead
    while p is not None:
        print(p.val, end='\t')
        p = p.next
    print('\n')
    p = Solution().ReverseList(pHead)
    while p is not None:
        print(p.val, end='\t')
        p = p.next
# 方法 1
# 创建一个空链表p，将pHead1，pHead2 的头结点比较，值小的加入到p中
# 若某个链表为空，则另一链表的所有值都大于此前的链表，此时只需将剩下的部分追加到p的尾部
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        # 创建头结点，便于处理
        p_merge = ListNode(0)
        p = p_merge
        while pHead1  and pHead2 :
            if pHead1.val < pHead2.val:
                p_merge.next = pHead1
                p_merge = pHead1
                pHead1 = pHead1.next
            else:
                p_merge.next = pHead2
                p_merge = pHead2
                pHead2 = pHead2.next

        if pHead1 is not None:
            p_merge.next = pHead1
        if pHead2 is not None:
            p_merge.next = pHead2
        return p.next


if __name__ == '__main__':
    p1 = ListNode(1)
    p = p1
    for i in range(3, 11, 2):
        node = ListNode(i)
        p.next = node
        p = node

    p2 = ListNode(2)
    p = p2
    for i in range(4, 11, 2):
        node = ListNode(i)
        p.next = node
        p = node

    p_merge = Solution().Merge(p1, p2)
    p = p_merge
    while p:
        print(p.val, end='\t')
        p = p.next

# 方法 2
# 使用递归
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        p_merge = None
        if pHead1.val < pHead2.val:
            p_merge = pHead1
            p_merge.next = self.Merge(pHead1.next, pHead2)
        else:
            p_merge = pHead2
            p_merge.next = self.Merge(pHead1, pHead2.next)
        return p_merge
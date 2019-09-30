# 解题思路
# 1. 把复制的结点链接在原始链表的每一对应结点后面
# 2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
# 3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，
# 注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，next指针要重新赋值None(判定程序会认定你没有完成复制）
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        # 复制节点在原节点之后
        pCur = pHead
        while pCur is not None:
            node = RandomListNode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        # 复制random 指针
        pCur = pHead
        while pCur is not None:
            if pCur.random is not None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        # 将新旧链表分离
        head = pHead.next
        cur = head
        pCur = pHead
        while pCur:
            pCur.next = pCur.next.next
            if cur.next:
                cur.next = cur.next.next
            pCur = pCur.next
            cur = cur.next
        return head
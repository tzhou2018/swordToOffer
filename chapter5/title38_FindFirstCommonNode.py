# 输出两个链表的第一个公共结点
# 思路：链接：https://www.nowcoder.com/questionTerminal/6ab1d9a29e88450685099d45c9e31e46?answerType=1&f=discussion
# 来源：牛客网
#
# 思路：首先我们要知道什么是公共节点，
# 两个链表从某一节点开始，他们的next都指向同一个节点。
# 但由于是单向链表的节点，每个节点只有一个next，因此从第一个公共节点开始，
# 之后他们的所有节点都是重合的，不可能再出现分叉。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1： 从表头开始遍历，短的先遍历完，然后指向长的表头；
# 等到长的遍历完之后指向短的表头，此时两指针所指向的剩余链表长度相当.
# 这种方法只考虑两个无环链表相交
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        curl1, curl2 = pHead1, pHead2
        # print(pHead1.val, pHead2.val)
        while curl1 != curl2:
            # print(curl1.val, curl2.val)
            curl1 = curl1.next if curl1 is not None else pHead2
            # print(curl1.val)
            curl2 = curl2.next if curl2 is not None else pHead1
            # print("curl2:", curl2.val)
        # 此时curl1, curl2 都指向空
        if curl1 == curl2:
            # print(curl1.val)
            # print("curl1,curl2")
            return curl1
        else:
            return None


def create_linked_list(arr=None):
    pHead = ListNode(arr[0])
    p = pHead
    for i in arr[1:]:
        node = ListNode(i)
        p.next = node
        p = node
    return pHead


if __name__ == '__main__':
    # 有问题.测试没有通过
    p1 = create_linked_list(arr=[2, 1, 0, 1])
    p2 = create_linked_list(arr=[4, 3, 1, 0, 1])
    print(Solution().FindFirstCommonNode(p1, p2))
    # p = p1
# 方法 2： 通过比较结点上的值来判断；感觉这种方法不严谨。
# 若仅仅是结点上的值相等，结点的指针域不等，这种方法也是可以通过。
# class Solution:
#     def FindFirstCommonNode(self, head1, head2):
#         # write code here
#         list1 = []
#         list2 = []
#         node1 = head1
#         node2 = head2
#         while node1:
#             list1.append(node1.val)
#             node1 = node1.next
#         while node2:
#             if node2.val in list1:
#                 return node2
#             else:
#                 node2 = node2.next

# 方法3
# 解题思路：先让长的链表往前走n步（n为两链表长度差），之后两链表依次往后遍历并比较
class Solution:
    def FindFirstCommonNode(self, head1, head2):
        # write code here
        if not head1 or not head2:
            return None
        lhead1 = []
        lhead2 = []
        cur1, cur2 = head1, head2
        while head1:
            lhead1.append(head1.val)
            head1 = head1.next
        while head2:
            lhead2.append(head2.val)
            head2 = head2.next
        if len(lhead1) > len(lhead2):
            for _ in range(len(lhead1) - len(lhead2)):
                cur1 = cur1.next
        else:
            for _ in range(len(lhead2) - len(lhead1)):
                cur2 = cur2.next
        while cur2 != cur1:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

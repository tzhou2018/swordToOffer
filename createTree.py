# -*- coding:utf-8 -*-

'二叉树结点类'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# '列表创建二叉树'


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


# 先序遍历二叉树
def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


# 中序遍历二叉树
def midOrdBT(root):
    if not root:
        return None
    midOrdBT(root.left)
    print(root.val, end="\t")
    midOrdBT(root.right)


# 后序遍历二叉树
def postOrdBT(root):
    if not root:
        return "#"
    midOrdBT(root.left)
    midOrdBT(root.right)
    print(root.val, end="\t")


# 层次遍历
# 试题 61 按之字形顺序打印二叉树


if __name__ == '__main__':
    llist = [1, 2, 3, '#', 4, 5, 6]
    root = listCreatTree(None, llist, 0)
    p = root
    post = root
    print(".............................")
    print("先序   中序  后序")
    preOrderBT(root)
    print()
    midOrdBT(p)
    print()
    postOrdBT(post)
    # print(root.val)
    # while root

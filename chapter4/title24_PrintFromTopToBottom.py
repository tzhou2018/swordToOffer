# 解题思路
# 使用列表 ans 存储每个节点的值，使用 queue 存储节点信息，首先存储根节点。
# 在循环中，若 queue 不为空，我们存储queue当前节点的值，并将当前节点 pop 出来；
# 接着判断左右节点是否为空

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        ans = []
        if not root:
            return ans
        _queue = [root]
        while _queue:
            item = _queue.pop(0)
            ans.append(item.val)
            if item.left is not None:
                _queue.append(item.left)
            if item.right is not None:
                _queue.append(item.right)

        return ans

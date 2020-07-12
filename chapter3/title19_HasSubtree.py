# 解题思路：
# 对于两棵二叉树来说，要判断B是不是A的子结构，首先第一步在树A中查找与B根节点的值一样的节点。
# 通常对于查找树中某一个节点，我们都是采用递归的方法来遍历整棵树。
# 第二步就是判断树A中以R为根节点的子树是不是和树B具有相同的结构。
# 这里同样利用到了递归的方法，如果节点R的值和树的根节点不相同，则以R为根节点的子树和树B肯定不具有相同的节点；
# 如果它们值是相同的，则递归的判断各自的左右节点的值是不是相同。
# 递归的终止条件是我们达到了树A或者树B的叶节点。

# 有地方要重点注意，is_subTree()函数中的两个 if 判断语句 不能颠倒顺序 。
# 因为如果颠倒了顺序，会先判断pRoot1 是否为None, 其实这个时候，pRoot1 的节点已经遍历完成确认相等了，
# 但是这个时候会返回 False，判断错误。
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.is_subTree(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def is_subTree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.is_subTree(pRoot1.left, pRoot2.left) and \
               self.is_subTree(pRoot1.right, pRoot2.right)



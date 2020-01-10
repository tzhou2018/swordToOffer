## [other](/other)

> 试题 47： 礼物的最大值

> 在一个 m×n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

**注意：**
```angular2html
m,n>0
样例：

输入： [ [2,3,1], [1,7,1], [4,6,1] ]

输出：19

解释：沿着路径 2→3→7→6→1 可以得到拿到最大价值礼物。
```
```python
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/12/26 22:17
desc:
'''


# 思路:
# 礼物要么来自左边一格，要么来自右边一格，两者各取最大。
# 需要判断边界情况，利用一维初始化数组完成动态规划；
# 记f(x,y)为到达该坐标时拿到礼物的最大值，f(x,y) = max(f(x-1,y),f(x,y-1)) + gift[i,j]
class Solution(object):
    def getMaxValue(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return 0
        initList = [0 for _ in range(cols)]
        initList[0] = grid[0][0]
        for i in range(1, cols):
            initList[i] = grid[0][i] + initList[i - 1]
        # print(initList)
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    initList[j] += grid[i][0]
                else:
                    initList[j] = max(initList[j], initList[i - 1]) + grid[i][j]
        # print(initList)
        return initList[cols - 1]


if __name__ == '__main__':
    testList = [[2, 3, 1], [1, 7, 1], [4, 6, 1]]
    print(Solution().getMaxValue(testList))

```

> 试题 48：最长不重复字符串的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

假设字符串中只包含从’a’到’z’的字符。

样例：

输入："abcabc"

输出：3

```python
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/9 17:21
desc:
'''


# 思路：限制在 O(1) 空间复杂度，那就只有通过二进制，一位一位去看了。
class Solution:
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
                    # print("count:", count)
            # count 能取余3，说明数组中唯一存在的那个数在该位上不为零
            if count % 3:
                res += 1 << i
        return res


if __name__ == '__main__':
    print(Solution().findNumberAppearingOnce([1, 1, 1, 3]))

```

> 试题55-2：平衡二叉树

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

假设字符串中只包含从’a’到’z’的字符。

样例：

输入："abcabc"

输出：3
```python
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/8 21:05
desc:
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 一般方法，有重复计算
    def isBalanced(self, root):
        if not root:
            return True
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        diff = left - right
        print("diff:", diff)
        if diff < -1 or diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return left + 1 if left > right else right + 1

    # plus 检测，采用后序遍历，省去重复计算
    flag = 1

    def plusIsBalanced(self, root):
        if not root:
            return True
        self._dfs(root)
        return self.flag

    def _dfs(self, node):
        if not node:
            return 0
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        if abs(left - right) > 1:
            self.flag = 0
        return max(left, right) + 1


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


if __name__ == '__main__':
    # llist = ['1', '2', '3', '#', '4', '5', '6']
    llist = [8, '#', 10, '#', '#', 9, 11]
    root = listCreatTree(None, llist, 0)
    p = root
    print(".............................")
    print(Solution().isBalanced(root))
    print(Solution().plusIsBalanced(root))

```

> 试题 56-2：数组中唯一只出现一次的数字 [?]

在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

你可以假设满足条件的数字一定存在。

思考题：

如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
样例：

输入：[1,1,1,2,2,2,3,4,4,4]

输出：3
```python
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/9 17:21
desc:
'''


# 思路：限制在 O(1) 空间复杂度，那就只有通过二进制，一位一位去看了。
class Solution:
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
                    # print("count:", count)
            # count 能取余3，说明数组中唯一存在的那个数在该位上不为零
            if count % 3:
                res += 1 << i
        return res


if __name__ == '__main__':
    print(Solution().findNumberAppearingOnce([1, 1, 1, 3]))

```

> 试题 53-2：0 到 n-1 中缺失的数字

一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 到 n-1 之内。
在范围 0 到 n-1 的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
样例

```angular2html
输入：[0,1,2,4]

输出：3
```

```python
# 思路： 使用“”“”“"二分法"解决问题
class Solution(object):
    def getMissingNumber(self, nums):
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > mid:
                high = mid - 1
            else:

                low = mid + 1
        return low


if __name__ == '__main__':
    print(Solution().getMissingNumber([0, 1, 2, 4]))

```

> 试题 53-3：数组中数值和下标相等的元素

假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
例如，在数组 [−3,−1,1,3,5] 中，数字 3 和它的下标相等。

样例：

输入：[−3,−1,1,3,5]
输出：3
注意：如果不存在，则返回 −1。
```python
# 思路： 使用“”“”“"二分法"解决问题
class Solution(object):
    def getNumberSameAsIndex(self, nums):
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < mid:
                low = mid + 1
            else:
                assert nums[mid] >= mid
                high = mid
            return low if nums[low] == low else -1


if __name__ == '__main__':
    print(Solution().getNumberSameAsIndex([-3, -1, 1, 3, 5]))
```




## [other](/other)

> 01.试题 47： 礼物的最大值

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

> 02.试题 48：最长不重复字符串的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

假设字符串中只包含从’a’到’z’的字符。

样例：
```text
输入："abcabc"

输出：3

```

> 03.试题55-2：平衡二叉树



> 04.试题 56-2：数组中唯一只出现一次的数字 [?]

在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

你可以假设满足条件的数字一定存在。

思考题：

如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
```text
样例：

输入：[1,1,1,2,2,2,3,4,4,4]

输出：3
```


> 05.试题 53-2：0 到 n-1 中缺失的数字

一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 到 n-1 之内。
在范围 0 到 n-1 的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
样例

```angular2html
输入：[0,1,2,4]

输出：3
```
> 06.试题 53-3：数组中数值和下标相等的元素

假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
例如，在数组 [−3,−1,1,3,5] 中，数字 3 和它的下标相等。

样例：
```text
输入：[−3,−1,1,3,5]
输出：3
注意：如果不存在，则返回 −1。
```


> 07.剑指offer 63： 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股票可能获得的利润是多少？

例如一只股票在某些时间节点的价格为 [9, 11, 8, 5, 7, 12, 16, 14]。

如果我们能在价格为 5 的时候买入并在价格为 16 时卖出，则能收获最大的利润 11。

样例：
```
输入：[9, 11, 8, 5, 7, 12, 16, 14]

输出：11
```


> 思路：在过往的股价中找到最低价，“当前股价 - 最低价”为获利。遍历过程中，找到这个获利的最大值即可。由于只允许做一次股票买卖交易，枚举每一天作为卖出的日子，买入日子一定在卖出日子之前，为了获利最多，希望买入的日子的股票价格尽可能低。用 minnum 记录第 
0 到 第 i 天的最低价格，则在第 i 天卖出的最大获利为 nums[i] - minnum，枚举 i 找到最大获利。

```python
class Solution:
    def maxdiff(self, nums):
        if not nums:
            return None

        min_value = nums[0]
        max_value = 0
        for i in range(1, len(nums)):
            min_value = min(min_value, nums[i])
            max_value = max(max_value, nums[i] - min_value)
        return max_value


if __name__ == '__main__':
    print(Solution().maxdiff([9, 11, 8, 5, 7, 12, 16, 15]))
```
> 08.小和问题

小和问题

在一个数组中， 每一个数左边比当前数小的数累加起来， 叫做这个数组的小和。 求一个数组
的小和。
```text
例子：
[1,3,4,2,5]
1左边比1小的数， 没有；
3左边比3小的数， 1；
4左边比4小的数， 1、 3；
2左边比2小的数， 1；
5左边比5小的数， 1、 3、 4、 2；
所以小和为1+1+3+1+1+3+4+2=16
```
上面的做法是比较当前数值前面有哪些数比自己小，则相加。

换种思路，当前数值后面有哪些数字比自己大，则当前值 * 个数（比自己大）




# 方法 1
# 比较倾向于找规律的解法，f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5，
# 可以总结出f(n) = f(n-1) + f(n-2)的规律，但是为什么会出现这样的规律呢？
# 假设现在6个台阶，我们可以从第5跳一步到6，这样的话有多少种方案跳到5就有多少种方案跳到6，
# 另外我们也可以从4跳两步跳到6，跳到4有多少种方案的话，就有多少种方案跳到6，其他的不能从3跳到6什么的啦，
# 所以最后就是f(6) = f(5) + f(4)；
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        item1, item2, ans = 1, 2, 0
        for _ in range(2, number):
            ans = item1 + item2
            item1, item2 = item2, ans
        return ans
# 方法 2
# 使用递归
# def jumpFloor(number):
#     if number == 1:
#         return 1
#     elif number ==2:
#         return 2
#     else:
#         return jumpFloor(number-1) + jumpFloor(number-2)
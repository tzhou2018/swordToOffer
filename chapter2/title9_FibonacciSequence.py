# -*- coding:utf-8 -*-
# from time import time
# start = time()
class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n
        item1, item2 = 0, 1
        for _ in range(2, n+1):
            ans = item1 + item2
            item1, item2 = item2, ans
        return ans
# 方法 2
# 使用递归; 当我们试图跟踪执行的程序，即使是很小的参数n，都感觉头都要炸了。
# 在这里，我们坚持信念，假定两个递归调用都可以正常工作，那么很明显，把他们加到一起必然可以得到正确结果

# 使用递归很耗时间，对时间要求严格的程序无法通过
# from time import time
# start = time()
# class Solution:
#
#     def Fibonacci(self, n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.Fibonacci(n-1) + self.Fibonacci(n-2)
# print(Solution().Fibonacci(39))
# end = time()
# print(end-start)

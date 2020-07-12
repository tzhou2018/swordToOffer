# -*- coding:utf-8 -*-
# 方法 1
# 思路：
# 首先看十进制是如何做的： 5+7=12，三步走
# 第一步：相加各位的值，不算进位，得到2。
# 第二步：计算进位值，得到10. 如果这一步的进位值为0，那么第一步得到的值就是最终结果。
# 第三步：重复上述两步，只是相加的值变成上述两步的得到的结果2和10，得到12。

# 同样我们可以用三步走的方式计算二进制值相加： 5（101），7(111)
# 第一步：相加各位的值，不算进位，得到010，二进制每位相加就相当于各位做异或操作，101^111。
# 第二步：计算进位值，得到1010，相当于各位做与操作得到101，再向左移一位得到1010，(101&111)<<1。
# 第三步重复上述两步， 各位相加 010^1010=1000，进位值为100=(010&1010)<<1。
# 继续重复上述两步：1000^100 = 1100，进位值为0(1000 & 100)，跳出循环，1100为最终结果。

# 注意：在牛客网上如下程序报错超时，但是同样的java程序却可以通过运算，
# 我也是[一脸尼克杨问号]
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 is not 0:
            temp = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = temp
            num2 = carry
        return num1


class Solution1:
    def add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = temp & 0xfff
            num2 = carry
        return num1


# 修改后，如下程序可以通过牛客网调试
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            _sum = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = _sum & 0xffffffff
            num2 = carray
        return num1 if num1 >> 31 == 0 else num1 - 2 ** 32


# 方法 2：
# 思路：
# 偷个懒，使用python内置的sum函数可以实现
class Solution:
    def Add(self, num1, num2):
        # write code here
        s = []
        s.append(num1)
        s.append(num2)
        return sum(s)

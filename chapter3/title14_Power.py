# 方法 1
def Power(base, exponent):
    return pow(base,exponent)

# 方法 2
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        result = 1
        if exponent == 0:
            return 1
        elif exponent > 0:
            for i in range(exponent):
                result *= base
            return result
        else:
            for i in range((-1)*exponent):
                result *= base
            return 1.0/result

# 方法3
# 一种高效的方法：
# 参考剑指offer给的解法，进行优化；
def Power2(base, exponent):
    abx_exponent = abs(exponent)
    if abx_exponent == 0:
        return 1
    if abx_exponent == 1:
        return base
    result = Power2(base, abx_exponent >> 1)
    result *= result
    if abx_exponent & 0x1 == 1:
        result *= base
    if exponent < 0:
        result = 1 / result
    return result

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
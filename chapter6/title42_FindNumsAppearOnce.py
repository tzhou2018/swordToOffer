# -*- coding:utf-8 -*-
# 方法 1
# 思路：遍历所给数组，将重复出现的数字放在 dubNumber,将所有出现过的数字放在 result 中，
# 之后对两个数组求差集。
# 当某一数字多次出现时，该方法任然有效。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # result = []
        dubNumber = []
        for i in range(len(array)):
            count = 0
            for j in range(i, len(array)):
                if j + 1 < len(array):
                    if array[i] == array[j + 1]:
                        count += 1
                        dubNumber.append(array[j + 1])
                        # array.pop(j)
            # if count == 0:
            #     result.append(array[i])
        # print(result)
        # print(dubNumber)
        return list(set(array).difference(set(dubNumber)))


# 方法 2
# 思路：从位运算符中异或运算考虑：两个相同的数字异或为0，一个数与0异或依然是他本身。
# 当所给数组中只有一个数出现一次时，我们把所给数组中的所有数依次进行异或运算，
# 最后剩下的就是落单的数，因为成对的数都抵消了；

# 依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，
# 这个结果的二进制中的1，表现的是A和B的不同的位。我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，
# 分组标准是第3位是否为1。如此，相同的数肯定在一个组，因为相同数字所有位都相同，而不同的数，肯定不在一组。
# 然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。
# 如： 输入数组 [2,4,3,6,3,2,5,5]
# 异或计算后： 0010
# 倒数第二位是1，按这个进行分组；
# 第一组是 [2,3,6,3,2]; 第二组是 [4,5,5]


def FindNumsAppearOnce(self, array):
    key = 0
    for item in array:
        key ^= item
    num1, num2 = 0, 0
    mark = 1
    while key & mark == 0:
        mark <<= 1
    for item in array:
        if item & mark == 0:
            num1 ^= item
        else:
            num2 ^= item
    return num1, num2
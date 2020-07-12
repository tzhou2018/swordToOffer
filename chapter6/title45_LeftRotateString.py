# -*- coding:utf-8 -*-
# 方法 1
# 思路：将所给字符串s当做列表进行处理，很容易就能得到左移、右移效果，
# 将转换后的字符串存储到列表result中，之后对result中的元素进行拼接。
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        lenS = len(s)
        result = []
        if lenS < n:
            return ''
        else:
            result.append(s[n:])
            result.append(s[:n])
        return ''.join(result)


# 方法 2
# 不借助额外空间
# 将所给字符串分为三部分进行逆转排序。首先将前n个逆转，之后将[n:]逆转，
# 最后将列表中的所有元素逆转并拼接
class Solution1:
    def LeftRotateString(self, s, n):
        # write code here
        len_s = len(s)
        if n <= 0 or len_s == 0:
            return s
        n = n % len_s
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


# 方法3
# 参考程序员面试指南，第五章翻转字符串 p269
class Solution2:
    def rotate2(self, arr, size):
        if not arr or size > len(arr):
            return
        start = 0
        end = len(arr) - 1
        lpart = size
        rpart = len(arr) - size
        s = min(lpart, rpart)
        d = lpart - rpart
        while True:
            self.exchange(arr, start, end, s)
            if d == 0:
                break
            elif d > 0:
                start += s
                lpart = d
            else:
                end -= s
                rpart = -d
            s = min(lpart, rpart)
            d = lpart - rpart
        return arr

    def exchange(self, arr, start, end, size):
        i = end - size + 1
        while size != 0:
            arr[start], arr[i] = arr[i], arr[start]
            start += 1
            i += 1
            size -= 1

if __name__ == '__main__':
    arr = list('1234567abcd')
    size = 7
    print(Solution2().rotate2(arr,size))
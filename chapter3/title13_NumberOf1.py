# 方法 1
# 借助逻辑运算符
def NumberOf1(n):
        # write code here
        count = 0
        flag = 1
        for _ in range(32):
            if flag & n != 0:
                count += 1
            flag <<= 1
        return count
# 方法2
def numberOf(n):
    return sum([(n>>i & 1) for i in range(32)])
# 方法 3
# 能给面试官代来惊喜的解法；
# 思路：把一个整数减去1，再和原整数作与运算，会把该整数最右边的1变为0；
# 注意：这种解法没有在牛客网上通过

class Solution:
    def NumberOf1(self, n):
        # write code here
        # write code here
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count

if __name__ == '__main__':
    print(Solution().NumberOf1(1023))

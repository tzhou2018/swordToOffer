# 方法 1
# 借助逻辑运算符
def NumberOf2(n):
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
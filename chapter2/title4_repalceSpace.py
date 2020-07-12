# solutions 1
# 使用python内置函数
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')


# solution 2
# 正则表达式
import re


class Solution1:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # ret = re.compile(' ')
        # return ret.sub('%20', s)
        return re.sub(r'\s', lambda m: '%20', s)


# 方法3
# 遍历所给列表，当遇到空格时，使用"20%"替换
class Solution3:
    @staticmethod
    def replaceSpace(arrStr):
        arrStr = list(arrStr)
        for i in range(len(arrStr)):
            if arrStr[i] == " ":
                arrStr[i] = "%20"
        return "".join(arrStr)


if __name__ == '__main__':
    arrStr = "We Are Happy"
    print(Solution3.replaceSpace(arrStr))

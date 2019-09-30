# solutions 1
# 使用python内置函数
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')
# solution 2
# 是哟正则表达式
import re


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # ret = re.compile(' ')
        # return ret.sub('%20', s)

        return re.sub(r'\s', lambda m: '%20', s)
# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/12/27 20:33
desc:
'''


class Solution:
    # 常规方法：遍历字符串
    def lengthOfLongestSubstring(self, s):
        """
        :param s:
        :return:
        """
        if len(s) < 1:
            return 0
        ret = []
        lenS = 0
        for i in s:
            if i not in ret:
                ret.append(i)
            else:
                # print(ret)
                ret.clear()
                ret.append(i)
                continue
            if len(ret) > lenS:
                lenS = len(ret)
        print(ret)
        return lenS

    # 方法 2
    # 动态规划
    # 找到递推公式： f(i)= f(i-1) +1
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特判
        l = len(s)
        if l < 2:
            return l
        # dp[i] 表示以 s[i] 结尾的最长不重复子串的长度
        # 因为自己肯定是不重复子串，所以初始值设置为 1
        dp = [1 for _ in range(l)]
        # 用字典来存储字符串s，其中k-v表示 ‘字符’-下标
        map = dict()
        map[s[0]] = 0
        for i in range(1, l):
            if s[i] in map:
                if i - map[s[i]] > dp[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = i - map[s[i]]
            else:
                dp[i] = dp[i - 1] + 1
            # 设置字符与索引键值对
            map[s[i]] = i
        # 最后拉通看一遍最大值
        print(dp)
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring1('abcaab'))

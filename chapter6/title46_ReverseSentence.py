# -*- coding:utf-8 -*-
# 方法 1
# 思路：首先将所给字符串转化为列表，对此列表进行逆序排序，之后再将列表中的元素进行拼接
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        s = s.split(' ')
        s = s[::-1]
        return ' '.join(s)


# 方法 2
# -*- coding:utf-8 -*-
# 思路： 类似于title45 方法2
class Solution1(object):
    def ReverseSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        size = len(s)
        arr = list(s)

        self.__reverse(arr, 0, size - 1)

        begin = 0
        index = 0
        while index < size:
            if arr[index] == ' ':
                self.__reverse(arr, begin, index - 1)
                begin = index + 1
            index += 1
        # 最后还要反转一下

        self.__reverse(arr, begin, size - 1)
        return ''.join(arr)

    def __reverse(self, arr, left, right):
        if left >= right:
            return
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    print(Solution1().ReverseSentence("I'am a student."))

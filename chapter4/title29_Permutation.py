# 字符串排列
# 方法 1
import itertools


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return ss
        result = []
        # 通俗地讲，就是返回可迭代对象的所有数学全排列方式
        k = itertools.permutations(ss)
        for i in k:
            result.append(''.join(i))
        result = list(set(result))
        result.sort()
        return result


# 方法 2
class Solution2:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        ans = []
        for i in range(len(ss)):
            print('len(ss):', len(ss))
            for item in map(lambda x: ss[i] + x, self.Permutation(ss[:i] + ss[i + 1:])):
                print('item:', item)
                if item not in ans:
                    print(ans)
                    ans.append(item)
        return ans


# 方法3
# 使用递归
# 如果需要去重的话，将所得的元素加入到set中
class Solution3:
    def allPermutations(self, str):
        list1 = list(str)
        self.process1(list1, 0)

    def process1(self, chs, i):
        if i == len(chs):
            print(''.join(chs), end=' ')
        for j in range(i, len(chs)):
            self.swap(chs, i, j)
            self.process1(chs, i + 1)
            self.swap(chs, i, j)

    def swap(self, chs, i, j):
        chs[i], chs[j] = chs[j], chs[i]


if __name__ == '__main__':
    sol = Solution3()
    sol.allPermutations("abc")

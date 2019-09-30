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
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return ss
        ans = []
        for i in range(len(ss)):
            print('len(ss):',len(ss))
            for item in map(lambda x: ss[i] + x, self.Permutation(ss[:i] + ss[i + 1:])):
                print('item:', item)
                if item not in ans:
                    print(ans)
                    ans.append(item)
        return ans
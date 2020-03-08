# -*- coding:utf-8 -*-
# 方法 1
# 遍历所给数组中的每一个元素，时间复杂度O(n2)
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) <= 1:
            return False
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] == numbers[j]:
                    # duplication.append(numbers[i])
                    duplication[0] = numbers[i]
                    return True
        return False


# 方法 2
# 使用桶排序的思想来解决，思想就是把一个数放在它该放的位置上。
class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        size = len(nums)
        if size < 2:
            return -1
        # 先统一检查数字是不是越界了
        for i in range(size):
            if nums[i] < 0 or nums[i] > size - 1:
                return -1
        for i in range(size):
            # nums[i] 应该在 i 的位置上
            while i != nums[i]:
                # 发现要交换的那个数和自己一样，就可以返回了
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                self.__swap(nums, i, nums[i])
        return -1

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp


if __name__ == '__main__':
    nums = [2, 3, 5, 4, 3, 2, 6, 7]
    solution = Solution()
    result = solution.duplicateInArray(nums)
    print(result)

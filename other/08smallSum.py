'''
@Time    : 2020/2/10 14:51
@FileName: smallSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def smallSum(arr):
    # 当数组为空或者只有一个数，小和为0
    if not arr or len(arr) < 1:
        return 0
    return mergeSum(arr, 0, len(arr) - 1)


# 求和函数
def mergeSum(arr, l, r):
    '''
    :param arr:原数组
    :param l: 划分过后的数组的左指针
    :param r: 划分过后的数组的右指针
    :return: 返回全部小和之和
    '''
    # 如果划分的数组的左指针和右指针重合，则没有产生小和，返回0
    if l == r:
        return 0
    # mid是划分的中点，其数值表示在原数组arr的索引位置
    mid = (l + r) // 2
    return mergeSum(arr, l, mid) + mergeSum(arr, mid + 1, r) + \
           merge(arr, l, mid, r)
    # return merge(arr, l, mid, r)


# 合并时求小和
def merge(arr, l, m, r):
    '''
    :param arr:程序一开始传入的原数组
    :param l: 将要合并时的数组左指针
    :param mid: 合并时在数组中的中点索引位置
    :param r: 将要合并时的数组右指针
    :return: 返回合并时产生的小和，在合并时只会求解  两数组右边数组的数对左边数组的数产生的小和。
    '''
    ret = []
    # p1是左边数组的第一个索引位
    p1 = l
    # p2是右边数组的第一个索引位
    p2 = m + 1
    res = 0
    while p1 <= m and p2 <= r:
        # 求解右边数组中的数对左边数组中的数产生的小和
        # 如果p1索引上的数比p2上的索引数小，则p2后面的数都比p1的数大，都会贡献小和。产生小和：arr[p1]*(r-p2+1)
        res += (r - p2 + 1) * arr[p1] if arr[p1] < arr[p2] else 0
        if arr[p1] < arr[p2]:
            ret.append(arr[p1])
            p1 += 1
        else:
            ret.append(arr[p2])
            p2 += 1
    while p1 <= m:
        ret.append(arr[p1])
        p1 += 1
    while p2 <= r:
        ret.append(arr[p2])
        p2 += 1
    # 将局部排序好的ret 去 替换原数组arr
    arr[l:r + 1] = ret
    print(arr)
    return res


arr = [1, 3, 4, 2, 5]
print(smallSum(arr))

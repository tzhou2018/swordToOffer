# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2019/11/4 20:32
desc:
'''
# 思路：
# 同 title62_PrintInLayer.py
# 若是题设没有要求返回二维列表，我们可以用队列(先进先出)这种容器来存储数据。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        ans = []
        if not pRoot:
            return ans
        curLayerNodes = [pRoot]
        while curLayerNodes:
            curLayerValues = []
            nextLayerNodes = []
            while curLayerNodes:
                node = curLayerNodes.pop(0)
                curLayerValues.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            ans.append(curLayerValues)
        return ans

# class Solution:
#     # 返回二维列表[[1,2],[4,5]]
#     def Print(self, pRoot):
#         # write code here
#         ans = []
#         if not pRoot:
#             return ans
#         curQueueNodes = [pRoot]
#         while curQueueNodes:
#             # ans = []
#             # nextLayerNodes = []
#             # while curLayerNodes:
#             node = curQueueNodes.pop(0)
#             ans.append(node.val)
#             if node.left:
#                 curQueueNodes.append(node.left)
#             if node.right:
#                 curQueueNodes.append(node.right)
#             # curLayerNodes = nextLayerNodes
#         # ans.append(ans)
#         return ans
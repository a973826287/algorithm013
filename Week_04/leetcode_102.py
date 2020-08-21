#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        res = []

        while queue:
            children = []
            nodes = []
            for item in queue:
                children.append(item.val)
                if item.left:
                    nodes.append(item.left)
                if item.right:
                    nodes.append(item.right)
            res.append(children)
            queue = nodes
        return res

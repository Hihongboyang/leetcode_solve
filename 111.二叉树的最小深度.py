#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ 分两种，深度优先和广度优先"""
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 9999
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)

        return min_depth + 1

        
# @lc code=end


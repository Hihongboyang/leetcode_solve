#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def assist(root):
            if root is None:
                return 0

            left_h = assist(root.left)
            right_h = assist(root.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h)>1:
                return -1
            else:
                return max(left_h, right_h) + 1
            
        return assist(root) >= 0
# @lc code=end


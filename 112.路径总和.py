#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def check_sum(self, root, target, sum_val) -> int:
    #     sum_val += root.val
    #     if not root.left and not root.right and target == sum_val:
    #         return True
    #     if not root.left and not root.right and target != sum_val:
    #         return False

    #     if root.left:
    #         left_val = self.check_sum(root.left, target, sum_val)
    #     else:
    #         left_val = False

    #     if root.right:
    #         right_val = self.check_sum(root.right, target, sum_val)
    #     else:
    #         right_val = False

    #     return left_val or right_val


    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     if not root:
    #         return False

    #     return self.check_sum(root, targetSum, 0)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum-root.val)

# @lc code=end
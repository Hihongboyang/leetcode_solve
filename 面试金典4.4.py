# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root: TreeNode):
            if not root:
               return 0

            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight)>1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return helper(root) >= 0
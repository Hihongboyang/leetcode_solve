# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length < 1:
            return None
        TreeList = [TreeNode(x) for x in nums] # 将数据都转为节点
        root = TreeList[length / 2]  # 取最中间的节点为根节点
        root.left = self.helper(TreeList[:length / 2])
        root.right = self.helper(TreeList[(length / 2)+1:])


        return root

    def helper(self, nums):
        length = len(nums)

        if length == 1:
            return nums[0]
        elif length == 0:
            return None

        root = nums[length/2]
        root.left = self.helper(nums[:length/2])
        root.right = self.helper(nums[(length/2 + 1):])

        return root
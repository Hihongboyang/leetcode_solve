#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        from queue import LifoQueue
        ret_list = list()
        if not root:
            return ret_list
        leaf_que = LifoQueue(10)

        leaf_que.put(root)
        while(not leaf_que.empty()):
            leaf_root = leaf_que.get()
            ret_list.append(leaf_root.val)
            if leaf_root.left:
                leaf_que.put(leaf_root.left)
            if leaf_root.right:
                leaf_que.put(leaf_root.right)
                
        return ret_list[::-1]

# @lc code=end


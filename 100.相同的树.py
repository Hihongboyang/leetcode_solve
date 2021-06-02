#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [1,2,3,4,5]\n[1,2,3,4,null,5]
# [1]\n[1,null,2]
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def assist(node):
            stack = [node]
            while(stack):
                try:
                    stack.append(node.left)
                except AttributeError:
                    pass

                try:
                    stack.append(node.right)
                except AttributeError:
                    pass

                node =  stack.pop(0)
                yield node
        
        for i,j in zip(assist(p), assist(q)):
            if (i and j) and (i.val == j.val):
                continue
            elif i == j:
                continue
            else:
                return False
        return True
            

# @lc code=end


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        使用类似二分法查找的思想，来查找p的下一个节点。
        当向左查找的时候，保留根节点
        查找右子树时，查找比p值大的最小值
        """
        res = None
        cur = root
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur  # 只要是大于目标值，每次都记录节点，并向左移动，知道记录最小值为止
                cur = cur.left  
        return res


class Solution2:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = None
        # 查找到p节点的位置，同时记录下了p的根节点
        while root.val != p.val:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        
        if not root.right:
            # 如果没有右子树，直接返回根节点
            return res
        else:
            # 有右子树，取有子树的最左节点
            root = root.right
            while root.left:
                root = root.left
            return root

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        使用循环代替递归的使用，完成中序遍历。
        检查是不是二叉搜索树，使用中序遍历，数值总是依次递增的。
        """
        stack = list()
        MIN_VAL = float("-inf")

        while stack or root:
            while root:    # ======================root
                # 首先按照左子树路径全部压入栈中。
                stack.append(root)   # 所有的需要遍历的节点都放在栈中
                root = root.left

            cur_node = stack.pop(-1)
            if cur_node.val <= MIN_VAL:  # 使用等号，因为二叉搜索树不能有重复值
                return False
            
            MIN_VAL = cur_node.val
            root = cur_node.right  # ======================root

        return True

            
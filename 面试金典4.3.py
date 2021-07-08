# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ret_list = list()
        queue_list = list()
        if not tree:
            return []
        queue_list.append(tree)

        while queue_list:
            root = ListNode(-1)
            root_p = root
            for i in range(len(queue_list)):
                cur_node = queue_list.pop(0)
                temp = ListNode(cur_node.val)
                root_p.next = temp
                root_p = temp

                if cur_node.left:
                    queue_list.append(cur_node.left)

                if cur_node.right:
                    queue_list.append(cur_node.right)
            ret_list.append(root.next)
        return ret_list


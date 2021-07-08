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
            for i in queue_list:
                temp = ListNode(i.val)
                root_p.next = temp
                root_p = temp
            ret_list.append(root.next)
            queue_list.append(-1)

            while queue_list:
                temp = queue_list.pop(0)
                if temp == -1:
                    break

                if temp.left:
                    queue_list.append(temp.left)

                if temp.right:
                    queue_list.append(temp.right)
        return ret_list


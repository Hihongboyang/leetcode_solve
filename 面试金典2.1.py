# Definition for singly-linked list.
from functools import reduce
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        mapping = dict()
        p_head = head
        before = None
        while p_head != None:
            is_exists = mapping.get(p_head.val, None)
            if is_exists:
                before.next = p_head.next
                
            else:
                mapping[p_head.val] = True
                before = p_head
            p_head = p_head.next
        return head

def create_node(x:ListNode, y:ListNode):
    x.next = y
    return y

if __name__ == "__main__":
    data_list = [
        [1,2,3,4,1,6],
        [3,3,3,3],
    ]
    for item in data_list:
        data_node = [ListNode(i) for i in item]
        reduce(create_node, data_node)
        head = data_node[0]
        some = Solution()
        some.removeDuplicateNodes(head)
        while(head):
            print(head.val)
            head = head.next
        print("=============")




            
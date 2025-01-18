#
# @lc app=leetcode.cn id=430 lang=python3
# @lcpr version=30204
#
# [430] 扁平化多级双向链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            if not cur.child:
                cur = cur.next
            else:
                next_node = cur.next
                child_head = self.flatten(cur.child)
                # 需要把child设置为None不然会报The linked list is not a valid doubly linked list
                cur.child = None 
                cur.next = child_head
                child_head.prev = cur
                child_head.child = None
                while cur.next:
                    cur = cur.next
                cur.next = next_node
                if next_node:
                    next_node.prev = cur
                    next_node.child = None
                cur = next_node

        return head

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


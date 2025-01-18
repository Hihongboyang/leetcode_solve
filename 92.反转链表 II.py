#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        front_part = dummy
        index = 0
        while index < left-1:
            front_part = front_part.next
            index += 1

        current = front_part.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = front_part.next
            front_part.next = next_node
            index += 1
        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        
        while cur.next and cur.next.next:
            temp_cur = cur.next  # 保存节点, 防止丢失
            temp_next = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp_cur
            temp_cur.next = temp_next
            cur = cur.next.next
        return dummy.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


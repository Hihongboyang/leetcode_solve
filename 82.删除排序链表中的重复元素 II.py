#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5 -> 5 -> 6 -> 7
#  ↑    ↑    ↑
# h/c  c.n  c.n.n
# ---------------------------------------------------------
#  1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5 -> 5 -> 6 -> 7
#  ↑    ↑    ↑
#  c   c.n  c.n.n
#  cur.next != cur.next.next; cur = cur.next
# ---------------------------------------------------------
#  1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5 -> 5 -> 6 -> 7
#       ↑    ↑    ↑    ↑
#       c   c.n==c.n.n ↑
#            t == t.n  ↑
#                  t  t.n
#       c.n<- <- <- <- ↓
#  cur.next == cur.next.next;
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head # 先拿到一个头, 防止丢失

        cur = dummy_head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        return dummy_head.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#


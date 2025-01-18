#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = self.findmid(head)
        list1 = head
        list2 = mid.next
        mid.next = None
        list2 = self.reverse(list2)

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list1 = temp1

            list2.next = list1
            list2 = temp2

    def findmid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

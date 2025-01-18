#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 利用快慢指针, 先找到链表的中间位置, 然后将后面的链表反转,
# 将反转后的链表与之前链表比较看是不是回文
# 最后还原链表
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        front_half_end = self.front_half(head)
        behind_half_start = self.reverse_list(front_half_end.next)

        result = True
        first = head
        second = behind_half_start

        while result and second is not None:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next

        front_half_end.next = self.reverse_list(behind_half_start)
        return result
        

    def reverse_list(self, head):
        prev = None
        cur = head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


    def front_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow
    

        

        
# @lc code=end

#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,2,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,2,2,2,2,1]\n
# @lcpr case=end

#


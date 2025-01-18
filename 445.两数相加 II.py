#
# @lc app=leetcode.cn id=445 lang=python3
# @lcpr version=30204
#
# [445] 两数相加 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 先反转链表, 再相加, 再反转链表
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        ret = self.addTwo(l1, l2)
        return self.reverseList(ret)
        

    def addTwo(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry
            mod = sum % 10
            carry = sum // 10

            cur.next = ListNode(mod)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#


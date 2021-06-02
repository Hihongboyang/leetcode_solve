#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head
        flag = False
        while(p1 and p2):
            try:
                p1 = p1.next
                p2 = p2.next.next
            except AttributeError as e:
                flag = False
                break

            if p1 == p2:
                flag = True
                break
        return flag

# @lc code=end


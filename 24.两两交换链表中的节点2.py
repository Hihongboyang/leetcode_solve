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

# 迭代方式实现
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 反转的node是pre和cur
        pre = head
        cur = head.next
        next = head.next.next

        cur.next = pre  # 交换
        pre.next = self.swapPairs(next)

        return cur

        
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


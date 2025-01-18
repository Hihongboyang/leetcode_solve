#
# @lc app=leetcode.cn id=328 lang=python3
# @lcpr version=30204
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        #        odd  even
        #         ↓    ↓ 
        # head    1 -> 2 -> 3 -> 4
        #     ev_he  ↗
        odd = head
        even_head = head.next
        even = even_head

        while even and even.next:
            # odd
            # ↑ ->->->  ↓ 
            # 1    2 -> 3 -> 4
            #      ↑
            #     even
            odd.next = even.next
            #           odd
            # ↑ ->->->  ↓ 
            # 1    2 -> 3 -> 4
            #      ↑
            #     even
            odd = odd.next
            #           odd
            # ↑  ->->-> ↓ 
            # 1    2    3 -> 4
            #      ↓  ->->-> ↑
            #     even
            even.next = odd.next
            #           odd
            # ↑  ->->-> ↓ 
            # 1    2    3 -> 4 -> None
            #      ↓  ->->-> ↑
            #                even
            even = even.next
        
        odd.next = even_head
        return head
        


        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,5,6,4,7]\n
# @lcpr case=end

#


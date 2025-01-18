#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        size = len(lists)
        return self.merge_sort(lists, 0, size - 1)
    
    def merge_sort(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        if left == right:
            return lists[left]
        
        mid = left + (right - left) // 2
        left_node = self.merge_sort(lists, left, mid)
        right_node = self.merge_sort(lists, mid+1, right)
        return self.merge(left_node, right_node)

    def merge(self, left: List[ListNode], right: List[ListNode]):
        root = ListNode(-1)
        cur = root
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left

        if right:
            cur.next = right

        return root.next
        
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#


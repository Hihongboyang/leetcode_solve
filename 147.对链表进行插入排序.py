#
# @lc app=leetcode.cn id=147 lang=python3
# @lcpr version=30204
#
# [147] 对链表进行插入排序
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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(val=-1, next=head)
        cur = head.next  # 当前需要排序的节点
        tail = head  # 已经排序节点的尾部

        while cur:
            if tail.val <= cur.val:  # 注意相等也不需要再排序了
                # 当前节点比已经排序的节点都大, 不需要插入到前面
                tail = tail.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    # 找到比cur.val大的节点的前一个节点
                    prev = prev.next

                # 将节点插入到prev节点的后面
                tail.next = cur.next
                cur.next = prev.next
                prev.next = cur

            cur = tail.next

        return dummy.next




# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end


# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#


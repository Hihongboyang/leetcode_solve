#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # 创建头节点, 使操作一致

        pre = dummy  # 开始都指向头
        end = dummy

        while end.next is not None:
            for _ in range(0, k):  # 将end移动到要反转的序列的末尾
                end = end.next
                if not end:
                    return dummy.next

            start = pre.next  # 要反转位置的开始
            next = end.next   # 保存反转结束位置后面一位
            end.next = None
            pre.next = self.reverse(start) # 反转,然后与之前的pre拼接
            start.next = next  # 与后面的数据拼接
            pre = start  # 移动pre到完成反转的位置, 之前的数据不用动了
            end = pre  # 回到最开始的状态
        return dummy.next

    def reverse(self, head: Optional[ListNode]):
        pre = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n1\n
# @lcpr case=end

#

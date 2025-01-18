#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30204
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        
        count = 1
        cur = head
        # 先计算出链表的长度
        while cur.next:
            cur = cur.next
            count += 1

        # 计算需要移动几个数
        if (add := count - k % count) == count:
            head
        
        # 头尾相连
        cur.next = head
        # 移动到指定位置
        while add:
            cur = cur.next
            add -= 1

        # 断开连接
        ret = cur.next
        cur.next = None
        return ret
        

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#


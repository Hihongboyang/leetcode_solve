#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30204
#
# [142] 环形链表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 假设快慢指针为 slow fast, 最开始都在head
#              ┌───────┐
#  s f         |       |
#  ↓ ↓         |       |
# head ------->|       |
#              |       |
#              |       |
#              └───────┘
# --------------------------------------------
# 当slow到达环的入口时, fast会在环上某个位置. 
#              ┌───────┐
#              |       f
#              |       |
# head ------->s       |
#              |       |
#              |       |
#              └───────┘
# --------------------------------------------
# 假设head到环入口的位置的距离是z.
# s到f的上半劣弧是x. f到s的优弧是y.
# 那么 2z = z + k(x+y) + x  (k>=0,有可能走了多个园了,也可能没走过) 
# (s走过的距离=f走过的距离) z = k(x+y)+x
#              ┌───x─>─┐
#              |       f
#              |       |
# head ------->s       |
# |---> z <--- |       |
#              |       |
#              └─<─y───┘
# --------------------------------------------
#              ┌───x─>─┐
#              |       f
#              |       |
# head ------->s       |
# |->k(x+y)+x<-|       |
#              |       |
#              └─<─y───┘
# --------------------------------------------
# 当f再走y步, 到达环的入口处, 此时s走了y/2. 
# f再走y步, s正好走了y, 此时slow和fast相遇.
# 假设相遇的位置是在 C处
#              ┌───y─>─┐
#              |       |
#              |       |
# head ------->|       |
# |->k(x+y)+x<-|       C
#              |       |
#              └───────┘
# --------------------------------------------
# 由之前的计算可知, 上方的优弧距离是y, 则下方的劣弧距离是x.
# 此时再用一个指针p(与slow速度一样)从head出发, 经过 k(x+y)+x 会和slow指针在环口相遇.
# 因为 p经过 k(x+y)+x, slow也会走过k个环(x+y) + x的距离

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        return ptr


# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n-1\n
# @lcpr case=end

#

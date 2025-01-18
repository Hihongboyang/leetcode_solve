#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        # 先复制一份原来的节点
        while cur:
            node = Node(cur.val, next=cur.next)
            cur.next = node
            cur = node.next

        # 再将随机链接, 连接上
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 将两个链表分开
        new_head = Node(x=0)
        new_cur = new_head
        cur = head
        while cur:
            new_cur.next = cur.next
            new_cur = new_cur.next
            cur.next = new_cur.next
            cur = cur.next
            

        return new_head.next
# @lc code=end



#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#


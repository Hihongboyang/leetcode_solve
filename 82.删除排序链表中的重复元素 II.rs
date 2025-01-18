/*
 * @lc app=leetcode.cn id=82 lang=rust
 * @lcpr version=30204
 *
 * [82] 删除排序链表中的重复元素 II
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn delete_duplicates(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut ret = Some(Box::new(ListNode::new(0)));
        let mut r_p = ret.as_mut()?;
        let mut prev = 101;  // 保存之前的值, 方便后面比较

        while let Some(mut node) = head {
            head = node.next.take();  // 先获取到当前节点的下一个节点
            if head.is_some() && (head.as_ref()?.val == node.val) || node.val == prev {
                // 如果当前节点和下一个节点相同, 或者当前节点和之前节点相同, 则不保存.
                prev = node.val
            } else {
                // 当前节点和前一个节点, 后一个节点都不同就保存
                prev = node.val;
                r_p.next = Some(node);
                r_p = r_p.next.as_mut()?;
            }
        }
        return ret.as_mut()?.next.take();
    }
}
// @lc code=end

/*
// @lcpr case=start
// [1,2,3,3,4,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,2,3]\n
// @lcpr case=end

 */

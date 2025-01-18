/*
 * @lc app=leetcode.cn id=83 lang=rust
 * @lcpr version=30204
 *
 * [83] 删除排序链表中的重复元素
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
        if head.is_none() {
            return None;
        }

        let mut cur = head.as_mut()?;
        while let Some(nxt) = cur.next.take() {  // 这里把值取走了
            if nxt.val == cur.val {
                cur.next = nxt.next;
            } else {
                cur.next = Some(nxt);   // 要把值再填回去
                cur = cur.next.as_mut()?;
            }
        }
        return head;
    }
}
// @lc code=end

/*
// @lcpr case=start
// [1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,2,3,3]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=206 lang=rust
 * @lcpr version=30204
 *
 * [206] 反转链表
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

// 1. cur   next       prev -> None
//     ↓     ↓ 
//     ◫ -> ◫ -> ◫
// ------------------------------
// 2. cur   next
//     ↓     ↓ 
//     ◫    ◫ -> ◫
//     ↓
//    prev
//     ↓
//    None
// ------------------------------
// 3.        cur prev  next
//            ↓  ↙     ↓ 
//    None <- ◫        ◫ -> ◫
// ------------------------------
// 4.        prev cur next
//            ↓    ↓ ↙ 
//    None <- ◫   ◫ -> ◫
// ------------------------------
// 5.        prev  cur  next
//            ↓     ↓    ↓
//    None <- ◫ <- ◫    ◫
// ------------------------------
// 6.         prev cur  next
//               ↘ ↓    ↓
//    None <- ◫ <- ◫    ◫
// ------------------------------
// 7.              prev cur next
//                  ↓    ↓ ↙ 
//    None <- ◫ <- ◫    ◫
// ------------------------------
// 8.              prev cur   next
//                  ↓    ↓     ↓
//    None <- ◫ <- ◫    ◫ -> None
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut current: Option<Box<ListNode>> = head;
        let mut prev:  Option<Box<ListNode>> = None;

        while let Some(mut node) = current {
            let next = node.next;
            node.next = prev;
            prev = Some(node);
            current = next;
        }
        return prev;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */


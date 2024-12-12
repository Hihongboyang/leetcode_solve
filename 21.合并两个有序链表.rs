/*
 * @lc app=leetcode.cn id=21 lang=rust
 *
 * [21] 合并两个有序链表
 */

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
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut list3 = ListNode::new(0);
        let mut ptr3 = &mut list3;

        while let (Some(n1), Some(n2)) = (list1.as_ref(), list2.as_ref()) {
            if n1.val < n2.val {
                ptr3.next = list1;
                ptr3 = ptr3.next.as_mut().unwrap();
                list1 = ptr3.next.take();
            } else {
                ptr3.next = list2;
                ptr3 = ptr3.next.as_mut().unwrap();
                list2 = ptr3.next.take();
            }
        }
        ptr3.next = if list1.is_some() { list1 } else { list2 };
        list3.next
    }
}
// @lc code=end


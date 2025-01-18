/*
 * @lc app=leetcode.cn id=23 lang=rust
 * @lcpr version=30204
 *
 * [23] 合并 K 个升序链表
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
    pub fn merge_k_lists(mut lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.len() <= 1 {
            return lists.pop()?;
        } else if lists.len() == 2 {
            return Self::merge_two_lists(lists.pop().unwrap(), lists.pop().unwrap());
        }

        let right_arr = lists.split_off(lists.len() >> 1);
        let left = Self::merge_k_lists(lists);
        let right = Self::merge_k_lists(right_arr);

        return Self::merge_k_lists(vec![left, right]);
    }

    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut ptr = &mut dummy;

        while let (Some(n1), Some(n2)) = (list1.as_ref(), list2.as_ref()) {
            if n1.val < n2.val {
                ptr.next = list1;
                ptr = ptr.next.as_mut().unwrap();
                list1 = ptr.next.take();
            } else {
                ptr.next = list2;
                ptr = ptr.next.as_mut().unwrap();
                list2 = ptr.next.take();
            }
        }
        ptr.next = list1.or(list2);
        dummy.next
    }
}
// @lc code=end

/*
// @lcpr case=start
// [[1,4,5],[1,3,4],[2,6]]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

// @lcpr case=start
// [[]]\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=496 lang=rust
 * @lcpr version=30204
 *
 * [496] 下一个更大元素 I
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

// 单调栈
use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = vec![];
        let mut mapping: HashMap<i32, i32> = HashMap::new();

        nums2.iter().for_each(|&n| {
            while !stack.is_empty() && stack.last().unwrap() < &n {
                mapping.insert(stack.pop().unwrap(), n);
            }
            stack.push(n);
        });

        nums1.iter().map(|&n| *mapping.get(&n).unwrap_or(&-1)).collect()
    }
}
// @lc code=end

/*
// @lcpr case=start
// [4,1,2]\n[1,3,4,2].\n
// @lcpr case=end

// @lcpr case=start
// [2,4]\n[1,2,3,4].\n
// @lcpr case=end

 */

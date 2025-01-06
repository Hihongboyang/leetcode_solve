/*
 * @lc app=leetcode.cn id=1438 lang=rust
 * @lcpr version=30204
 *
 * [1438] 绝对差不超过限制的最长连续子数组
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::BTreeMap;
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let mut window: BTreeMap<i32, Vec<usize>> = BTreeMap::new();
        let mut left = 0;
        let mut max = 0;

        for (right, &num) in nums.iter().enumerate() {
            window.entry(num).or_insert_with(Vec::new).push(right);
            while (window.keys().next_back().unwrap() - window.keys().next().unwrap()) > limit {
                if let Some(values) = window.get_mut(&nums[left]) {
                    values.remove(0);
                    if values.len() == 0 {
                        window.remove(&nums[left]);
                    }
                    left += 1;
                }
            }
            max = max.max(right - left + 1)
        }
        return max as i32;
    }
}
// @lc code=end

/*
// @lcpr case=start
// [8,2,4,7]\n4\n
// @lcpr case=end

// @lcpr case=start
// [10,1,2,4,7,2]\n5\n
// @lcpr case=end

// @lcpr case=start
// [4,2,2,2,4,4,2,2]\n0\n
// @lcpr case=end

 */

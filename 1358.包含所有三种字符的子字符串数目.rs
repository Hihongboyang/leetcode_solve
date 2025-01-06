/*
 * @lc app=leetcode.cn id=1358 lang=rust
 * @lcpr version=30204
 *
 * [1358] 包含所有三种字符的子字符串数目
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let mut left: usize = 0;
        let mut count: usize = 0;
        let nums = s.as_bytes();
        let mut length: usize = nums.len() - 1;
        let mut mapping: HashMap<u8, i32> = HashMap::new();

        for (right, &num) in nums.iter().enumerate() {
            *mapping.entry(num).or_insert(0) += 1;  // 记录字符数量
            while mapping.len() > 2 {
                count += (length - right + 1);  // 只要包含了三个类型的字符了, 后面再加入字符都是符合的
                *mapping.entry(nums[left]).or_insert(0) -= 1;  // 窗口左侧向右移动
                if mapping[&nums[left]] == 0 {
                    mapping.remove(&nums[left]);
                }
                left += 1;
            }

        }
        return count as i32;
    }
}
// @lc code=end

/*
// @lcpr case=start
// "abcabc"\n
// @lcpr case=end

// @lcpr case=start
// "aabcabc"\n
// @lcpr case=end

// @lcpr case=start
// "aaacb"\n
// @lcpr case=end

// @lcpr case=start
// "abc"\n
// @lcpr case=end

 */

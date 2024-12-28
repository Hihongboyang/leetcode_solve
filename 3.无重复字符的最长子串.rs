/*
 * @lc app=leetcode.cn id=3 lang=rust
 * @lcpr version=30204
 *
 * [3] 无重复字符的最长子串
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut max = 0;
        let mut map = std::collections::HashMap::new();
        
        for (right, c) in s.chars().enumerate() {
            if let Some(&idx) = map.get(&c) {
                left = left.max(idx + 1);
            }
            map.insert(c, right);
            max = max.max(right - left + 1);
        }
        return max as i32;
    }
}
// @lc code=end



/*
// @lcpr case=start
// "abcabcbb"\n
// @lcpr case=end

// @lcpr case=start
// "bbbbb"\n
// @lcpr case=end

// @lcpr case=start
// "pwwkew"\n
// @lcpr case=end

// @lcpr case=start
// "dvdf"\n
// @lcpr case=end

// @lcpr case=start
// "abba"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n
// @lcpr case=end

// @lcpr case=start
// "au"\n
// @lcpr case=end

// @lcpr case=start
// "aab"\n
// @lcpr case=end


 */


/*
 * @lc app=leetcode.cn id=424 lang=rust
 * @lcpr version=30204
 *
 * [424] 替换后的最长重复字符
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    // 1. 需要记录窗口中每种字符的数量.
    // 2. 如果窗口的长度减去最大数量的字符数正好等于k, 那就说明找到了一个最长的字符串.
    // 3. 窗口向右增长后, 如果不满足2的条件会从左边向右增长缩小窗口,每次只缩小一格.
    //    然后邮编窗口继续向右增长. 在找到当时的最大窗口后, 窗口只会增大或者不变, 不会再缩小.
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut mapping = [0; 26];
        let nums = s.as_bytes();
        let k = k as usize;
        let (mut left, mut right) = (0, 0);
        let mut max = 0;

        for (index, &num) in nums.iter().enumerate() {
            mapping[(num - b'A') as usize] += 1;
            max = max.max(mapping[(num - b'A') as usize]);
            if (index - left + 1 - max) > k {
                mapping[(nums[left]-b'A') as usize] -= 1;
                left += 1;
            }
            right = index;
        }
        return (right - left + 1) as i32;
    }
}
// @lc code=end

/*
// @lcpr case=start
// "ABAB"\n2\n
// @lcpr case=end

// @lcpr case=start
// "AABABBA"\n1\n
// @lcpr case=end

// @lcpr case=start
// "AABACBA"\n1\n
// @lcpr case=end

// @lcpr case=start
// "BA"\n1\n
// @lcpr case=end

// @lcpr case=start
// "ABEBDCCC"\n2\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=467 lang=rust
 * @lcpr version=30204
 *
 * [467] 环绕字符串中唯一的子字符串
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_substring_in_wrapround_string(s: String) -> i32 {
        let mut left = 0;
        let mut count = 0;
        let nums = s.as_bytes();
        let mut last = nums[0];
        let mut mapping = vec![0; 32];

        for (right, &num) in nums.iter().enumerate() {
            if right > 0 && ((num - last) == 1 || (last - num) == 25)  {
                count += 1;
            } else {
                count = 1;
            }

            last = num;
            mapping[(nums[right] - 97) as usize] = count.max(mapping[(nums[right] - 97) as usize]);
        }
        return mapping.iter().sum::<i32>();
    }
}
// @lc code=end

/*
// @lcpr case=start
// "a"\n
// @lcpr case=end

// @lcpr case=start
// "cac"\n
// @lcpr case=end

// @lcpr case=start
// "zab"\n
// @lcpr case=end

 */

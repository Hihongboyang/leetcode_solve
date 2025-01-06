/*
 * @lc app=leetcode.cn id=674 lang=rust
 * @lcpr version=30204
 *
 * [674] 最长连续递增序列
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let mut count = 1;
        let mut max_count = 0;
        let length = nums.len();
        
        for i in 1..length {
            if nums[i] <= nums[i-1] {
                max_count = count.max(max_count);
                count = 1;
            }
            if nums[i] > nums[i-1] {
                count += 1;
            }
        }
        return count.max(max_count);

    }
}
// @lc code=end

/*
// @lcpr case=start
// [1,3,5,4,7]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,2,2]\n
// @lcpr case=end

 */

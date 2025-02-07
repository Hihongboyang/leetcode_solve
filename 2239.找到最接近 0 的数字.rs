/*
 * @lc app=leetcode.cn id=2239 lang=rust
 * @lcpr version=30204
 *
 * [2239] 找到最接近 0 的数字
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        *nums.iter().min_by_key(|&x| (x.abs(), -x)).unwrap()
    }
}
// @lc code=end



/*
// @lcpr case=start
// [-4,-2,1,4,8]\n
// @lcpr case=end

// @lcpr case=start
// [2,-1,1]\n
// @lcpr case=end

 */


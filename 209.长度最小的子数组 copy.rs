/*
 * @lc app=leetcode.cn id=209 lang=rust
 * @lcpr version=30204
 *
 * [209] 长度最小的子数组
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut left: usize = 0;
        let mut sum: i32 = 0;
        let mut min: usize = nums.len() + 1;

        nums.iter().enumerate().for_each(|(right, &num)| {
            sum += num;
            while sum >= target {
                min = min.min(right - left + 1);
                sum -= nums[left];
                left += 1;
            }
        });

        if min < nums.len() {
            return min as i32;
        } else {
            return 0;
        }
    }
}
// @lc code=end

/*
// @lcpr case=start
// 7\n[2,3,1,2,4,3]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[1,4,4]\n
// @lcpr case=end

// @lcpr case=start
// 11\n[1,1,1,1,1,1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// 11\n[1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// 11\n[1,1,1,1,1,1,1,1,1,1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// 15\n[5,1,3,5,10,7,4,9,2,8]\n
// @lcpr case=end



 */

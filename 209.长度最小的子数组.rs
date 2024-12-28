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
        let mut left = 0;
        let mut right = 0;
        let mut sum = 0;
        let mut min = std::i32::MAX;

        for (index, &num) in nums.iter().enumerate() {
            sum += num;
            right = index;
            if sum >= target {
                while sum - nums[left] >= target {
                    sum -= nums[left];
                    left += 1;
                }
                min = min.min((right - left + 1) as i32);
            }
        }
        if sum < target {
            return 0;
        }
        return min as i32;
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


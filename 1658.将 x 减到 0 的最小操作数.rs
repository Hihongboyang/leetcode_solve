/*
 * @lc app=leetcode.cn id=1658 lang=rust
 * @lcpr version=30204
 *
 * [1658] 将 x 减到 0 的最小操作数
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let target: i32 = nums.iter().sum::<i32>() - x;
        let (mut sum, mut left) = (0, 0);
        let mut max: i32 = -1;

        if target < 0 {
            return -1;
        }

        for (right, &num) in nums.iter().enumerate() {
            sum += num;
            while sum > target {
                sum -= nums[left];
                left += 1;
            }
            if sum == target {
                max = max.max((right - left + 1) as i32);
            }
        }

        if max < 0 {
            return -1;
        } else {
            return nums.len() as i32 - max;
        }
    }
}
// @lc code=end

/*
// @lcpr case=start
// [1,1,4,2,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [5,6,7,8,9]\n4\n
// @lcpr case=end

// @lcpr case=start
// [3,2,20,1,1,3]\n10\n
// @lcpr case=end

// @lcpr case=start
// [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]\n134365\n
// @lcpr case=end

 */

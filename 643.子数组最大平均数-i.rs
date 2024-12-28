/*
 * @lc app=leetcode.cn id=643 lang=rust
 * @lcpr version=30204
 *
 * [643] 子数组最大平均数 I
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut left = 0;
        let mut right = 0;
        let mut average: f64 = std::f64::MIN;

        for (index, &num) in nums.iter().enumerate() {
            right = index;
            if (right - left + 1) == (k as usize) {
                let sum = nums[left..=right].iter().sum::<i32>();
                let ave = sum as f64 / k as f64;
                left += 1;
                average = average.max(ave);
            }
        }

        return average;
        
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,12,-5,-6,50,3]\n4\n
// @lcpr case=end


// @lcpr case=start
// [5]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n6\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n7\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n8\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n9\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n10\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n1\n
// @lcpr case=end

 */


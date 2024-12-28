/*
 * @lc app=leetcode.cn id=713 lang=rust
 * @lcpr version=30204
 *
 * [713] 乘积小于 K 的子数组
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut sum = 1;
        let mut count = 0;

        for (index, &num) in nums.iter().enumerate() {
            sum *= num;
            right = index;
            while sum >= k && left <= right {
                sum /= nums[left];
                left += 1;
            }
            count += (right - left + 1) as i32;
        }
        return count;
        
    }
}
// @lc code=end



/*
// @lcpr case=start
// [10,5,2,6]\n100\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n0\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n4\n
// @lcpr case=end


 */


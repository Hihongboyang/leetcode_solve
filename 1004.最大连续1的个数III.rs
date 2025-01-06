/*
 * @lc app=leetcode.cn id=1004 lang=rust
 * @lcpr version=30204
 *
 * [1004] 最大连续1的个数 III
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut left: usize = 0;
        let mut count: usize = 0;
        let mut max: usize = 0;

        nums.iter().enumerate().for_each(|(right, &num)| {
            if num == 0 {
                count += 1
            }
            while count > k {
                if nums[left] == 0 {
                    count -= 1;
                }
                left += 1;
            }
            max = max.max(right - left + 1);
        });
        return max as i32;
    }
}
// @lc code=end

/*

// @lcpr case=start
// [1,1,1,0,0,0,1,1,1,1,0]\n0\n
// @lcpr case=end


// @lcpr case=start
// [1,1,1,0,0,0,1,1,1,1,0]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,0,0,0,1,1,1,1,0]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,0,0,0,1,1,1,1,0]\n1\n
// @lcpr case=end

// @lcpr case=start
// [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1, 0]\n1\n
// @lcpr case=end

// @lcpr case=start
// [0, 1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [0]\n1\n
// @lcpr case=end

// @lcpr case=start
// [0]\n0\n
// @lcpr case=end
 */

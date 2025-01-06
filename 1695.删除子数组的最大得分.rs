/*
 * @lc app=leetcode.cn id=1695 lang=rust
 * @lcpr version=30204
 *
 * [1695] 删除子数组的最大得分
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        let mut mapping: HashSet<i32> = HashSet::new();
        let mut left = 0;
        let mut max = 0;
        let mut sum = 0;

        for (right, &num) in nums.iter().enumerate() {
            if !mapping.contains(&num) {
                sum += num;
                mapping.insert(num);
                max = max.max(sum);
            } else {
                while nums[left] != num {
                    sum -= nums[left];
                    mapping.remove(&nums[left]);
                    left += 1;
                }
                left += 1;  
                // 如果nums[left]==num则sum之前已经加上num的值了, 
                // 就不用再加了, 只需要移动指针就行了
            }
        }
        return max;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [4,2,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [5,2,1,2,5,2,1,2,5]\n
// @lcpr case=end


// @lcpr case=start
// [1,1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,1,2,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [10000,1,10000,1,1,1,1,1,1]\n
// @lcpr case=end

 */


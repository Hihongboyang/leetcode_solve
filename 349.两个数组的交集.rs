/*
 * @lc app=leetcode.cn id=349 lang=rust
 * @lcpr version=30204
 *
 * [349] 两个数组的交集
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut ret: Vec<i32> = vec![];
        let mut nums1 = nums1.iter().collect::<HashSet<&i32>>();

        for n in nums2.iter() {
            if nums1.contains(n){
                ret.push(*n);
                nums1.remove(n);
            }
        }
        return ret;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,2,1]\n[2,2]\n
// @lcpr case=end

// @lcpr case=start
// [4,9,5]\n[9,4,9,8,4]\n
// @lcpr case=end

 */


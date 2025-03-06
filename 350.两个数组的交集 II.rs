/*
 * @lc app=leetcode.cn id=350 lang=rust
 * @lcpr version=30204
 *
 * [350] 两个数组的交集 II
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

use std::collections::HashMap;

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut counts: HashMap<i32, usize> = HashMap::new();
        let mut ret: Vec<i32> = vec![];

        nums1
            .iter()
            .for_each(|n| *counts.entry(*n).or_insert(0) += 1);

        nums2.iter().for_each(|n| {
            counts.entry(*n).and_modify(|v| {
                if *v > 0 {
                    *v -= 1;
                    ret.push(*n);
                }
            });
        });
        // for n in nums2.iter() {
        //     if let Some(v) = counts.get_mut(n) {
        //         if *v > 0 {
        //             *v -= 1;
        //             ret.push(*n);
        //         }
        //     }
        // }
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

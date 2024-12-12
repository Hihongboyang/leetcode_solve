/*
 * @lc app=leetcode.cn id=1 lang=rust
 *
 * [1] 两数之和
 */
/* version 1
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in i+1..nums.len() {
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }
        return vec![];
    }
}
*/

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut mapping: HashMap<i32, i32> = HashMap::new();

        for i in 0..nums.len() {
           if let Some(index) =  mapping.get(&nums[i]) {  // get返回的是数值的引用
               return vec![*index, i as i32];
           } else {
               mapping.insert(target-nums[i], i as i32);
           }
        }
        return vec![];
    }
}
// @lc code=end


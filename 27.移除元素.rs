/*
 * @lc app=leetcode.cn id=27 lang=rust
 *
 * [27] 移除元素
 */

// @lc code=start
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut point:usize = 0;
        
        for index in 0..nums.len() {
            if nums[index] != val {
                nums[point] = nums[index];
                point += 1;
            }
        }
        point as i32  //少了return  内存使用减少了0.3MB
    }
}
// @lc code=end


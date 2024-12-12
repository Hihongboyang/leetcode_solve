/*
 * @lc app=leetcode.cn id=26 lang=rust
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut count = 0;
        let length = nums.len();
        if length < 1 {
            return 0;
        }
        
        for index in 1..length {
            if nums[count] != nums[index] {
                count += 1;
                nums[count] = nums[index];
            }
        }
        count+=1;
        return count as i32

    }
}
// @lc code=end


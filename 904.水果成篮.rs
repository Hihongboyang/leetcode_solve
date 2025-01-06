/*
 * @lc app=leetcode.cn id=904 lang=rust
 * @lcpr version=30204
 *
 * [904] 水果成篮
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut max = 0;
        let mut count = 0;
        let mut count_map: HashMap<i32, i32> = HashMap::new();
        
        for (right, &num) in fruits.iter().enumerate() {
            *count_map.entry(num).or_insert(0) += 1;
            if *count_map.get(&num).unwrap() == 1 as i32 {
                count += 1;
            }

            while count > 2 {
                *count_map.entry(fruits[left]).or_insert(1) -= 1;
                if count_map[&fruits[left]] == 0 as i32{
                    count -= 1;
                }
                left += 1;
            }
            max = max.max(right - left + 1);
        }
        return max as i32;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,3,3,1,2,1,1,2,3,3,4]\n
// @lcpr case=end

 */


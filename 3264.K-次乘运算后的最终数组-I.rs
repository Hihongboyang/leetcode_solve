/*
 * @lc app=leetcode.cn id=3264 lang=rust
 * @lcpr version=30204
 *
 * [3264] K 次乘运算后的最终数组 I
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        let mut ans = vec![0; nums.len()];

        let mut map: Vec<(usize, i32)> = nums.into_iter().enumerate().collect::<Vec<_>>();
        for _ in 0..k {
            map.sort_by(|a, b| {
                if a.1 != b.1 {
                    a.1.cmp(&b.1)
                } else {
                    a.0.cmp(&b.0)
                }
            });  // 排序, 从小到大排序
            map[0] = (map[0].0, map[0].1 * multiplier);
        }

        map.into_iter().for_each(|(index, val)| ans[index] = val);
        return ans;
    }
}
// @lc code=end

/*
// @lcpr case=start
// [2,1,3,5,6]\n5\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n3\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,3,5]\n5\n3\n
// @lcpr case=end

 */

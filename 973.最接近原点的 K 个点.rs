/*
 * @lc app=leetcode.cn id=973 lang=rust
 * @lcpr version=30204
 *
 * [973] 最接近原点的 K 个点
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

// 排序
impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut points = points;
        points.sort_unstable_by_key(|item| item[0] * item[0] + item[1] * item[1]);
        points.truncate(k as usize);
        points
    }
}
// @lc code=end



/*
// @lcpr case=start
// [[1,3],[-2,2]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[3,3],[5,-1],[-2,4]]\n2\n
// @lcpr case=end

 */


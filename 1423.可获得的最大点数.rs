/*
 * @lc app=leetcode.cn id=1423 lang=rust
 * @lcpr version=30204
 *
 * [1423] 可获得的最大点数
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn max_score(card_points: Vec<i32>, k: i32) -> i32 {
        // 找到反向的窗口.
        // 在数组内部找到 n-k 大小窗口的最小值. 也就找到剩下数的最大值
        let window_size: usize = (card_points.len()) - k as usize;
        let mut min: i32 = card_points[..window_size].iter().sum::<i32>();
        let mut sum: i32 = min;
        println!("window_size: {}, min: {}, sum: {}", window_size, min, sum);

        for index in window_size..card_points.len() {
            sum += (card_points[index] - card_points[index-window_size]);
            min = min.min(sum);
        }        
        return card_points.iter().sum::<i32>() - min;
    }
}

// @lc code=end

/*
// @lcpr case=start
// [1,2,3,4,5,6,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2]\n2\n
// @lcpr case=end

// @lcpr case=start
// [9,7,7,9,7,7,9]\n7\n
// @lcpr case=end

// @lcpr case=start
// [9,7,7,9,7,7,9]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,1000,1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,79,80,1,1,1,200,1]\n3\n
// @lcpr case=end

 */

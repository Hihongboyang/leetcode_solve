/*
 * @lc app=leetcode.cn id=1052 lang=rust
 * @lcpr version=30204
 *
 * [1052] 爱生气的书店老板
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let mut left = minutes as usize;
        let mut sums = [0, 0]; // [不生气顾客的和, 生气时顾客的和]
        let mut max = 0;

        for (i, (&c, &g)) in customers.iter().zip(grumpy.iter()).enumerate() {
            sums[g as usize] += c; // 顾客数加到对应的位置
            if i < left - 1 {
                continue;
            }

            max = max.max(sums[1]); // 记录生气时的最大顾客数
            if grumpy[i - left + 1] == 1 {
                // 窗口左边的生气时顾客数要减去
                sums[1] -= customers[i - left + 1];
            }
        }
        return sums[0] + max;
    }
}
// @lc code=end

/*
// @lcpr case=start
// [1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n[0]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n[0,0,0,0,0,0,0,0,0,0]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n[1,1,1,1,1,1,1,1,1,1]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n[1,1,1,1,1,1,1,1,1,1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7,8,9,10]\n[1,0,1,0,1,0,1,0,1,0]\n3\n
// @lcpr case=end


 */

/*
 * @lc app=leetcode.cn id=239 lang=rust
 * @lcpr version=30204
 *
 * [239] 滑动窗口最大值
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k  = k as usize;
        let length = nums.len();
        let mut res = Vec::with_capacity(length - k + 1);  // 提前分配存储空间
        let mut deque = VecDeque::new();  // 存储数值从大到小值的下标
        
        for (i, &num) in nums.iter().enumerate() {
            while !deque.is_empty() && nums[*deque.back().unwrap()] < num {  // 只有123步, 没法说明deque中的元素是递减的
                deque.pop_back();
            }

            deque.push_back(i);  // 1. 入队

            if i - deque[0] >= k {  // 2. 如果队首元素已经不在窗口内，就出队
                deque.pop_front();
            }

            if i >= k - 1 {  // 3. 如果窗口形成了，就记录当前窗口的最大值
                res.push(nums[deque[0]]);
            }
        }
        return res;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,3,-1,-3,5,3,6,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */


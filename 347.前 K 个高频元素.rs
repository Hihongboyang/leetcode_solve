/*
 * @lc app=leetcode.cn id=347 lang=rust
 * @lcpr version=30204
 *
 * [347] 前 K 个高频元素
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

// 首先对数组中的数字进行统计
// 然后利用小顶堆, 将数量排在k个后的元素都弹出,
// 小顶堆中剩下的就是前k多的元素, 然后从后向前填充结果即可.
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap}; // rust中BinaryHeap是大顶堆

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut hash = HashMap::new();
        let mut heap = BinaryHeap::with_capacity(k as usize);
        nums.into_iter().for_each(|n| {
            *hash.entry(n).or_insert(0) += 1;
        });

        for (k, v) in hash {
            // 如果到达标定容量, 新的统计数没有堆顶小, 不用添加了
            if heap.len() == heap.capacity() {
                if *heap.peek().unwrap() < (Reverse(v), k) {
                    continue
                } else {
                    // 如果比堆顶小, 就pop腾出一个位置
                    heap.pop();
                }
            }

            heap.push((Reverse(v), k));
        }
        heap.into_iter().map(|(_, k)| k).collect()        
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,1,1,2,2,3]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */


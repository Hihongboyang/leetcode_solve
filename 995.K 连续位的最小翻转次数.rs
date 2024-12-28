/*
 * @lc app=leetcode.cn id=995 lang=rust
 * @lcpr version=30204
 *
 * [995] K 连续位的最小翻转次数
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    // 滑动窗口解题
    // 首先要知道:  
    // 1. 一个数是否被反转, 受他前面k-1个数的影响
    // 2. 一个数被反转偶数次会变回原来的数, 奇数次会变成相反的数 0->1, 1->0
    
    // 下来就是要记录, 某个位置前面的数据是否反转, 以及反转了多少次. 
    // ---->如何记录?<----
    // 使用一个[数组], 记录发生反转的窗口k的开始的位置, 有一个位置记录说明发生了一次反转
    // 如果当前位置i, 超过了[数组][0]+k的位置, 说明不再受到[数组][0]位置反转的影响, 可以将这个位置删除

    // ---->如何判断当前位置是否需要反转?<----
    // 当 i 为 0，并且len([数组])为偶数, 说明被之前反转了偶数次后还会是0, 所以需要反转
    // 当 i 为 1，并且len([数组])为奇数, 说明被之前反转了奇数次后是0, 所以需要反转
    // 总结一下就是: 如果 len([数组]) % 2 == nums[i], 那么nums[i]需要被反转.
    pub fn min_k_bit_flips(nums: Vec<i32>, k: i32) -> i32 {
        let mut ret = 0;
        let k = k as usize;
        let mut queue = vec![];
        let length = nums.len();

        for i in 0..nums.len() {
            if queue.len() > 0 && i >= (queue[0] + k) {
                queue.remove(0);
            }
            if nums[i] as usize == queue.len() % 2 {
                if i + k > length {
                    return -1;
                }
                queue.push(i);
                ret += 1;
            }
        }
        return ret;

    }
}
// @lc code=end

/*
// @lcpr case=start
// [0,1,0]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,1,0]\n2\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0,1,0,1,1,0]\n3\n
// @lcpr case=end

// @lcpr case=start
// [0,1,1,1,0,0]\n3\n
// @lcpr case=end


 */

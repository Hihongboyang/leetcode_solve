/*
 * @lc app=leetcode.cn id=567 lang=rust
 * @lcpr version=30204
 *
 * [567] 字符串的排列
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let n1 = s1.len();
        let n2 = s2.len();
        if n1 > n2 {
            return false;
        }

        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let mut cnt1 = vec![0; 26]; // 26个字母对应列表
        let mut cnt2 = vec![0; 26];

        for i in 0..n1 {
            cnt1[(s1[i] - b'a') as usize] += 1; // 先计算并比较最前面的n1个字符
            cnt2[(s2[i] - b'a') as usize] += 1;
        }
        if cnt1 == cnt2 {
            // 如果相等，直接返回true
            return true;
        }

        // 再计算剩下的字符
        for i in n1..n2 {
            cnt2[(s2[i] - b'a') as usize] += 1;  // 右边加入一个字符
            cnt2[(s2[i - n1] - b'a') as usize] -= 1;  // 左边减去一个字符
            if cnt1 == cnt2 {
                return true;
            }
        }
        false
    }
}
// @lc code=end

/*
// @lcpr case=start
// "eidbaooo"\n
// @lcpr case=end

// @lcpr case=start
// "eidboaoo"\n
// @lcpr case=end

 */

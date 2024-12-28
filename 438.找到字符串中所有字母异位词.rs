/*
 * @lc app=leetcode.cn id=438 lang=rust
 * @lcpr version=30204
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let s_len = s.len();
        let p_len = p.len();
        let mut res = vec![];
        if p_len > s_len {
            return res;
        }

        let s = s.as_bytes();
        let p = p.as_bytes();
        let mut cnts = vec![0; 26]; // 26个字母对应列表
        let mut cntp = vec![0; 26];

        for i in 0..p_len {
            cnts[(s[i] - b'a') as usize] += 1; // 先计算并比较最前面的p_len个字符
            cntp[(p[i] - b'a') as usize] += 1;
        }

        if cnts == cntp {
            res.push(0);
        }

        // 再计算剩下的字符
        for i in p_len..s_len {
            cnts[(s[i] - b'a') as usize] += 1; // 右边加入一个字符
            cnts[(s[i - p_len] - b'a') as usize] -= 1; // 左边减去一个字符
            if cnts == cntp {
                res.push((i - p_len + 1) as i32);
            }
        }
        return res;
    }
}
// @lc code=end

/*
// @lcpr case=start
// "cbaebabacd"\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// "abab"\n"ab"\n
// @lcpr case=end

 */

/*
 * @lc app=leetcode.cn id=20 lang=rust
 * @lcpr version=30204
 *
 * [20] 有效的括号
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 != 0 {
            return false;  // 长度是偶数
        }

        let map = [(b')', b'('), (b']', b'['), (b'}', b'{')]
            .iter()
            .cloned()
            .collect::<HashMap<_, _>>();

        let mut st = vec![];
        for c in s.bytes() {
            if !map.contains_key(&c) {
                st.push(c);  // 左括号, 入栈
            } else if st.is_empty() || st.pop().unwrap() != *map.get(&c).unwrap() {
                return false;  // 没有括号, 或者类型不匹配
            }
        }
        return st.is_empty();  // 所有括号必须都完成匹配
    }
}
// @lc code=end

/*
// @lcpr case=start
// "()"\n
// @lcpr case=end

// @lcpr case=start
// "()[]{}"\n
// @lcpr case=end

// @lcpr case=start
// "(]"\n
// @lcpr case=end

// @lcpr case=start
// "([])"\n
// @lcpr case=end

 */

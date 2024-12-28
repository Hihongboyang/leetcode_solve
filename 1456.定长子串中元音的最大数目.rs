/*
 * @lc app=leetcode.cn id=1456 lang=rust
 * @lcpr version=30204
 *
 * [1456] 定长子串中元音的最大数目
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        // 循环{
        // 如果是元音 count+=1
        // 判断是否到达窗口大小
        // 如果到达窗口大小, 与max比较, 更新max
        // 取出窗口最左边的字符, 如果是元音, count-=1
        // }
        let s = s.as_bytes();
        let mut count = 0;
        let mut max = 0;
        let k = k as usize;

        for (index, &c) in s.iter().enumerate() {
            // 进入窗口, 开始计数
            if c == b'a' || c == b'e' || c == b'i' || c == b'o' || c == b'u' {
                count += 1;
            }

            // 未到窗口大小
            if index < k - 1 {
                continue;
            }
            // 到达窗口大小, 更新max
            max = max.max(count);
            let s_out = s[index + 1 - k];
            if s_out == b'a' || s_out == b'e' || s_out == b'i' || s_out == b'o' || s_out == b'u' {
                count -= 1;
            }

        }
        return max;
    }
}

// @lc code=end

/*
// @lcpr case=start
// "abciiidef"\n3\n
// @lcpr case=end

// @lcpr case=start
// "aeiou"\n2\n
// @lcpr case=end

// @lcpr case=start
// "leetcode"\n3\n
// @lcpr case=end

// @lcpr case=start
// "rhythms"\n4\n
// @lcpr case=end

// @lcpr case=start
// "tryhard"\n4\n
// @lcpr case=end

 */

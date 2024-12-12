/*
 * @lc app=leetcode.cn id=13 lang=rust
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut res = 0;
        let mut last = 0;
    
        for b in s.bytes().rev() {  // 反序
            let n = match b {
                b'I' => 1,
                b'V' => 5,
                b'X' => 10,
                b'L' => 50,
                b'C' => 100,
                b'D' => 500,
                b'M' => 1000,
                _=> panic!(),
            };
    
            res += if n < last { -n } else { n };  // 前一个比后一个大, 则相减
            last = n;
        }
        return res;
    }
}
// @lc code=end


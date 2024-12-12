/*
 * @lc app=leetcode.cn id=9 lang=rust
 *
 * [9] 回文数
 */


/* version 1
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x!=0 && x%10 == 0) {
           return false;
        }

        let number_str = x.to_string();
        let str_len = number_str.len();
        
        for i in 0..str_len {
            let j = str_len - i - 1;
            if &number_str[i..i+1] == &number_str[j..j+1] {
                if j < i {
                    return true;
                }
            } else {
                return false;
            }
        }
        return true;

    }
}
*/
// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x!=0 && x%10 == 0) {
           return false;
        }
        let mut x:i32 = x;
        let mut revert_num:i32 = 0;
        while x > revert_num {
            revert_num = revert_num*10 + x%10;
            x /= 10;
        }

        return x == revert_num || x == revert_num/10

    }
}
// @lc code=end


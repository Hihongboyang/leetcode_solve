/*
 * @lc app=leetcode.cn id=14 lang=rust
 *
 * [14] 最长公共前缀
 */
/*  version 1
strs
.iter()
.max()
.unwrap()
.chars()
.zip(strs.iter().min().unwrap().chars())
.take_while(|x| x.0 == x.1)
.map(|x| x.0.to_string())
.collect::<Vec<_>>()
.join("")
*/

// @lc code=start
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() < 1 {
            println!("{}", "".to_string());
        }
    
        let first_ = &strs[0];
        let first_cahrs: Vec<char> = first_.chars().collect();
        let mut min_len = first_.len();
    
        for i in 1..strs.len() {
            let seconde_ = &strs[i];
            let seconde_cahrs: Vec<char> = seconde_.chars().collect();
            let seconde_len = seconde_.len();
    
            min_len = seconde_len.min(min_len);
    
            let mut rec_num = 0;
            for j in 0..min_len {
                if first_cahrs[j] == seconde_cahrs[j] {
                    rec_num += 1;
                } else {
                    break;
                }
            }
            min_len = min_len.min(rec_num);
        }
    
        if min_len > 0 {
            first_[0..min_len].to_string()
        } else {
            "".to_string()
        }
    }
}
// @lc code=end


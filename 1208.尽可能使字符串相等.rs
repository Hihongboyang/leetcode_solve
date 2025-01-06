/*
 * @lc app=leetcode.cn id=1208 lang=rust
 * @lcpr version=30204
 *
 * [1208] 尽可能使字符串相等
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let mut left = 0;
        let mut max = 0;
        let mut sum: i32 = 0;
        let s_nums = s.as_bytes();
        let t_nums = t.as_bytes();

        for (right, (&s, &t)) in s_nums.iter().zip(t_nums).enumerate() {
            sum += (t as i32 - s as i32).abs();
            if i32::from(sum) <= max_cost{
                max = max.max(right - left + 1);
            } else {
                while left <= right && i32::from(sum) > max_cost {
                    sum -= (t_nums[left] as i32 - s_nums[left] as i32).abs();
                    left += 1;
                }
            }
        }
        return max as i32;
    }
}
// @lc code=end

/*
// @lcpr case=start
// "abcd"\n"bcdf"\n3\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n"cdef"\n3\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n"acde"\n0\n
// @lcpr case=end

// @lcpr case=start
// "aaaaa"\n"bbbbb"\n3\n
// @lcpr case=end

// @lcpr case=start
// "aaaaa"\n"bbbbb"\n0\n
// @lcpr case=end

// @lcpr case=start
// "krrgw"\n"zjxss"\n19\n
// @lcpr case=end

// @lcpr case=start
// "ujteygggjwxnfl"\n"nstsenrzttikoy"\n43\n
// @lcpr case=end

// @lcpr case=start
// "krpgjbjjznpzdfy"\n"nxargkbydxmsgby"\n14\n
// @lcpr case=end

// @lcpr case=start
// "kkujxwtrlwvkkyccrimpiiinzyzcpuqnretofvouicbqwmuypaynwfjztmjugihipeyfasclggdzzofbcfbuazeppmxswdvuzlnwckkzzlqkphusagqmxfvjlpxgjwoprahezgrrlwtxbbhehvmvwcoyngwsgegcelpgehdzecxsrwozlvtogajxmbqhgljxerdgierc"\n"jynhwjttmbcelakawdfwqkfhgxxqzvpmsczlklzqnrxkpupmajzfcfgxhgzqzbbgvgmjtaiekkdbdnudnichmricfokewmxtlvdiqmuybpgsmcdhybwlxdqkhnfjfonilzohukpwztipmuroiknsnodvegbiugxsmcxqccccdcripyfrzqcmqtblowvkkbnagkgsftau"\n715\n
// @lcpr case=end

 */

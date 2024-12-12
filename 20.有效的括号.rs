/*
 * @lc app=leetcode.cn id=20 lang=rust
 *
 * [20] 有效的括号
 */

 /*  version 1
 impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 != 0 {  // 长度是奇数的不通过
            return false;
        }
    
        let mut stack: Vec<char> = Vec::new();  // 建立栈
        let mut mapping: HashMap<char, char> = HashMap::new();
        mapping.insert('}', '{');
        mapping.insert(']', '[');
        mapping.insert(')', '(');
    
        let mut val: Option<char> = None;
        for one in s.chars() {
            if mapping.contains_key(&one){ // 如果在mapping则 弹出栈
                val = stack.pop()
            } else {
                stack.push(one);  // 否则压入栈
                continue;
            }
            
            if let Some(val) = val {
                if val != *mapping.get(&one).unwrap() {  // 判断取出的值是否对应
                    return false;
                }
            }
            else {
                return false
            }
            
        }
        stack.is_empty()
    }
}
 */

// @lc code=start
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();

        for b_val in s.into_bytes().into_iter() {
            match b_val {
                b'{' | b'(' | b'[' => stack.push(b_val),
                b')' => {
                    if stack.is_empty() || b_val - stack.pop().unwrap() != 1 {
                        return false;
                    }
                }
                b'}' | b']' => {
                    if stack.is_empty() || b_val - stack.pop().unwrap() != 2 {
                        return false;
                    }
                }
                _ => (),

            }
        }
        stack.is_empty()
    }
}
// @lc code=end


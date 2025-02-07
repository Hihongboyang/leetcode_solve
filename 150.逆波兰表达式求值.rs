/*
 * @lc app=leetcode.cn id=150 lang=rust
 * @lcpr version=30204
 *
 * [150] 逆波兰表达式求值
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

// 栈
impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = vec![];

        for token in tokens.into_iter() {
            match token.as_str() {
                "+" => {
                    let a = stack.pop().unwrap();
                    *stack.last_mut().unwrap() += a;
                }

                "-" => {
                    let a = stack.pop().unwrap();
                    *stack.last_mut().unwrap() -= a;
                }

                "*" => {
                    let a = stack.pop().unwrap();
                    *stack.last_mut().unwrap() *= a;
                }

                "/" => {
                    let a = stack.pop().unwrap();
                    *stack.last_mut().unwrap() /= a;
                }

                _ => {
                    stack.push(token.parse::<i32>().unwrap());
                }
            }
        }
        stack.pop().unwrap()
    }
}
// @lc code=end



/*
// @lcpr case=start
// ["2","1","+","3","*"]\n
// @lcpr case=end

// @lcpr case=start
// ["4","13","5","/","+"]\n
// @lcpr case=end

// @lcpr case=start
// ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
// @lcpr case=end

 */


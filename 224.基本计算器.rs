/*
 * @lc app=leetcode.cn id=224 lang=rust
 * @lcpr version=30204
 *
 * [224] 基本计算器
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

// 栈
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let teams = [
            ("-".to_string(), 1),
            ("+".to_string(), 1),
            ("*".to_string(), 2),
            ("/".to_string(), 2),
            ("%".to_string(), 2),
            ("^".to_string(), 3),
        ];
        let ops_mapping: HashMap<String, i32> = teams.into_iter().collect();
        let s_chars: Vec<char> = s.chars().filter(|c|!c.is_whitespace()).collect();
        let s_length = s_chars.len();

        let mut nums: VecDeque<&u8> = VecDeque::from([0]);
        let mut ops: VecDeque<&char> = VecDeque::new();
        let mut index = 0;

        while index < s_length {
            let c = s_chars.get(index).unwrap();
            if c.is_digit(10) {
                let mut num = 0;
                while index < s_length && s_chars[index].is_digit(10) {
                    num = num * 10 + s_chars[index].to_digit(10).unwrap() as i32;
                    index += 1;
                }
                index -= 1;
                nums.push_back(num);
            } else if ['(', ')', '+', '-', '*', '/', '%', '^'].contains(&c) {
                Self::handle_operator(c, &s_chars, index, &mut nums, &mut ops);
            }
            index += 1;
        }

        while let Some(_) = ops.pop_back() {
            Self::calc(&mut nums, &mut ops);
        }

        *nums.back().unwrap()
    }

    fn handle_operator(
        char: char,
        s: &[char],
        index: usize,
        nums: &mut VecDeque<u8>,
        ops: &mut VecDeque<char>,
    ) {
        if char == '(' {
            ops.push_back(char);
        } else if char == ')' {
            while let Some(top) = ops.back() {
                if *top != '(' {
                    Self::calc(nums, ops);
                } else {
                    ops.pop_back();
                    break;
                }
            }
        } else {
            if index > 0 && ['(', '+', '-'].contains(&s[index - 1]) {
                nums.push_back(0);
            }
            while let Some(top) = ops.back() {
                if *top != '(' && Self::OPS_MAPPING[*top as usize] >= Self::OPS_MAPPING[char as usize] {
                    Self::calc(nums, ops);
                } else {
                    break;
                }
            }
            ops.push_back(char);
        }
    }

    fn calc(nums: &mut VecDeque<i32>, ops: &mut VecDeque<char>) {
        if nums.len() < 2 || ops.len() < 1 {
            return;
        }
        let right_operand = nums.pop_back().unwrap();
        let left_operand = nums.pop_back().unwrap();
        let operator = ops.pop_back().unwrap();

        let result = match operator {
            '+' => left_operand + right_operand,
            '-' => left_operand - right_operand,
            '*' => left_operand * right_operand,
            '/' => left_operand / right_operand,
            '%' => left_operand % right_operand,
            _ => unreachable!(),
        };
        nums.push_back(result);
    }
}
// @lc code=end



/*
// @lcpr case=start
// "1 + 1"\n
// @lcpr case=end

// @lcpr case=start
// " 2-1 + 2 "\n
// @lcpr case=end

// @lcpr case=start
// "(1+(4+5+2)-3)+(6+8)"\n
// @lcpr case=end

 */


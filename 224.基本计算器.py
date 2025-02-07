#
# @lc app=leetcode.cn id=224 lang=python3
# @lcpr version=30204
#
# [224] 基本计算器
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start

# 栈
from collections import deque

class Solution:
    ops_mapping = {
        "-": 1,
        "+": 1,
        "*": 2,
        "/": 2,
        "%": 2,
        "^": 3,
    }

    def calculate(self, s: str) -> int:
        # 移除输入字符串中的空格
        s_chars = list(s.replace(' ', ''))
        s_length = len(s_chars)
        
        # 初始化数字栈和运算符栈
        nums = deque([0])  # 先放一个0 方便计算
        ops = deque()

        index = 0
        while index < s_length:
            char = s_chars[index]
  
            if char.isdigit():
                # 处理连续的数字字符，将其转换为一个整数
                num = 0
                while index < s_length and s_chars[index].isdigit():
                    num = num * 10 + int(s_chars[index])
                    index += 1

                index -= 1
                nums.append(num)
            elif char in "()+-*/%^":
                # 处理运算符
                self.handle_operator(char, s_chars, index, nums, ops)
                
            # 由于 while 循环中 index 已经自增，这里需要回退一位
            index += 1

        # 处理运算符栈中剩余的运算符
        while ops:
            self.calc(nums, ops)

        return nums[-1]

    def handle_operator(self, char, s, index, nums, ops):
        if char == "(":
            # 遇到左括号，直接压入运算符栈
            ops.append(char)
        elif char == ")":
            # 遇到右括号，不断进行计算直到遇到左括号
            while ops and ops[-1] != "(":
                self.calc(nums, ops)
            if ops and ops[-1] == "(":
                ops.pop()
        else:
            # 处理负数或括号后的运算符，先压入 0
            if index > 0 and s[index - 1] in ("(", "+", "-"):
                nums.append(0)
            
            # 当运算符栈不为空且栈顶不是左括号，并且栈顶运算符优先级不低于当前运算符时，进行计算
            while ops and ops[-1] != '(' and self.ops_mapping.get(ops[-1], 0) >= self.ops_mapping.get(char, 0):
                self.calc(nums, ops)
            
            # 将当前运算符压入运算符栈
            ops.append(char)
            
    def calc(self, nums, ops):
        # 检查栈中元素数量是否足够进行计算
        if len(nums) < 2 or len(ops) < 1:
            return
        # 从数字栈中弹出两个操作数
        right_operand = nums.pop()
        left_operand = nums.pop()
        # 从运算符栈中弹出运算符
        operator = ops.pop()

        # 使用 match 语句进行运算符匹配和计算
        match operator:
            case '+':
                result = left_operand + right_operand
            case '-':
                result = left_operand - right_operand
            case '*':
                result = left_operand * right_operand
            case '/':
                result = left_operand // right_operand
            case '%':
                result = left_operand % right_operand
        # 将计算结果压入数字栈
        nums.append(result)

# @lc code=end


#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

# @lcpr case=start
# "1-(     -2)"\n
# @lcpr case=end

#

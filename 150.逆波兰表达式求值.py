#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30204
#
# [150] 逆波兰表达式求值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 栈
from operator import add, sub, mul


def div(x, y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))


class Solution:
    op_map = {"+": add, "-": sub, "*": mul, "/": div}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))
        return stack.pop()


# @lc code=end


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

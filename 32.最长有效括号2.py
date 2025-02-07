#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        start = -1  # 用于记录当前有效括号子串的起始位置

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)  # 遇到左括号，将其下标入栈
            else:
                if stack:
                    stack.pop()  # 弹出栈顶的左括号下标
                    if stack:
                        # 如果栈不为空，当前有效括号子串长度为当前位置减去栈顶元素的值
                        max_len = max(max_len, i - stack[-1])
                    else:
                        # 如果栈为空，当前有效括号子串长度为当前位置减去起始位置
                        max_len = max(max_len, i - start)
                else:
                    # 若栈为空且遇到右括号，更新起始位置
                    start = i

        return max_len

        
# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "(((((((((())))))))))"\n
# @lcpr case=end

# @lcpr case=start
# "((((((((((())))))))))"\n
# @lcpr case=end

# @lcpr case=start
# "((())))"\n
# @lcpr case=end

# @lcpr case=start
# "()(()"\n
# @lcpr case=end

# @lcpr case=start
# "())()"\n
# @lcpr case=end

# @lcpr case=start
# "()()()"\n
# @lcpr case=end
#


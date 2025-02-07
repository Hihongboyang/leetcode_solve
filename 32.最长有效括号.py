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
        stack = [-1]
        max_len = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        
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


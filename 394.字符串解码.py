#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 栈,    存储字符, 存储重复数
# stack, string, mul = [], "", 0
#
# 3 [ a ] 2 [ b c ]
# ---------------------------------------- 
# 3 [ a ] 2 [ b c ]
# ↑
# c
# stack, string, mul = [], "", 3
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#   ↑
#   c
# stack, string, mul = [(3, "")], "", 0
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#     ↑
#     c
# stack, string, mul = [(3, "")], "a", 0
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#       ↑
#       c
# stack, string, mul = [], "aaa", 0
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#         ↑
#         c
# stack, string, mul = [], "aaa", 2
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#           ↑
#           c
# stack, string, mul = [(2, "aaa")], "", 0
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#               ↑
#               c
# stack, string, mul = [(2, "aaa")], "bc", 0
# ----------------------------------------
# 3 [ a ] 2 [ b c ]
#                 ↑
#                 c
# stack, string, mul = [], "aaabcbc", 0
# ---------------------------------------- 
class Solution:
    def decodeString(self, s: str) -> str:
        stack, mul, string = [], 0, ""
        for c in s:
            if c == '[':
                stack.append((mul, string))
                mul = 0
                string = ""
            elif c == ']':
                (cur_mul, last_res) = stack.pop()
                string = last_res + string * cur_mul
            elif c.isdigit():
                mul = mul * 10 + int(c)
            else:
                string += c

        return string

        
# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

# @lcpr case=start
# "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=316 lang=python3
# @lcpr version=30204
#
# [316] 去除重复字母
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 单调栈
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_cor = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and stack[-1] > c and i < last_cor[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)
        
        
# @lc code=end



#
# @lcpr case=start
# "bcabc"\n
# @lcpr case=end

# @lcpr case=start
# "cbacdcbc"\n
# @lcpr case=end

#


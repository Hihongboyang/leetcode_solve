#
# @lc app=leetcode.cn id=1047 lang=python3
# @lcpr version=30204
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop(-1)
            else:
                stack.append(c)
        
        return "".join(stack)
    
# @lc code=end



#
# @lcpr case=start
# "abbaca"\n
# @lcpr case=end

#


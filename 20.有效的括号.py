#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {"}":"{", ")":"(", "]":"["}
        for item in s:
            if item not in paren_map:
                stack.append(item)
            elif not stack or paren_map.get(item, None) != stack.pop(-1):
                return False
        return not stack

# @lc code=end


#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "}])":
                if not stack:
                    return False
                else:
                    diff = ord(i) - ord(stack.pop())
                    if diff > 3 or diff <= 0:
                        return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False



# @lc code=end


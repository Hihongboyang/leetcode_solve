#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = mapping[s[0]]
        stack = s[0]
        for i in s[1:]:
            if mapping[stack] < mapping[i]:
                sum = sum - 2 * mapping[stack] + mapping[i]
                
            else:
                sum += mapping[i]
            stack = i
        
        return sum

# @lc code=end


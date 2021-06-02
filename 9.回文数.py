#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        if x<0 or (x!=0 and x % 10 == 0):
            return False
        
        while temp < x:
            temp = (x % 10) + temp * 10 
            x = x // 10
        
        return x == temp or x == temp//10

# @lc code=end


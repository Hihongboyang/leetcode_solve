#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s_len = len(s)
        star = 0
        end = s_len -1
        flag = True
        while(star<end):
            if not str.isalnum(s[star]):
                star += 1
                continue
            if not str.isalnum(s[end]):
                end -= 1
                continue

            print(s[star], s[end])
            if str.lower(s[star]) != str.lower(s[end]):
                flag = False
                break
            else:
                star += 1
                end -= 1

        return flag
                


# @lc code=end


#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        columnTitle  = columnTitle[::-1]
        for i in range(len(columnTitle)-1, 0, -1):
            item_val = ord(columnTitle[i]) - 64

            result = result + item_val * pow(26, i)

        result = ord(columnTitle[0]) - 64 + result

        return result

# @lc code=end


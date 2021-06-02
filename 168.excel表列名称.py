#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret_list = list()
        while(columnNumber > 0):
            columnNumber -= 1
            a, b = divmod(columnNumber, 26)
            ret_list.append(b)
            columnNumber = a

        return "".join([chr(65+i) for i in ret_list[::-1]])


# @lc code=end



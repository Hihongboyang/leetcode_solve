#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret_list = list()
        for n in range(numRows):
            row = list()
            for i in range(n + 1):
                if i == n or i == 0:
                    row.append(1)
                else:
                    row.append(ret_list[n-1][i]+ret_list[n-1][i-1])
            ret_list.append(row)
        return ret_list


# @lc code=end


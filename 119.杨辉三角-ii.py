#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def factorize(self, n):
        if n == 0:
            return 1
        print(n)
        return reduce(lambda x,y: x*y, range(1, n+1))

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        ret_list = list()
        for i in range(rowIndex + 1):
            ret_list.append(self.factorize(rowIndex) // (self.factorize(i) * self.factorize(rowIndex-i)))
        return ret_list


# @lc code=end


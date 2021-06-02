#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        gain = 0

        for i in range(len(prices)):
            if prices[i] - prices[buy] < 0:
                buy = i

            if prices[i] - prices[buy] > gain:
                gain = prices[i] - prices[buy]
        return gain
            


            


# @lc code=end


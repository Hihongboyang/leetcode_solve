#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        some = 0
        gain = 0

        for i in range(len(prices)):
            if prices[i] - prices[buy] <= 0:
                buy = i
                gain += some
                some = 0
            if prices[i] - prices[buy] > 0:
                if prices[i] - prices[buy] > some:
                    some = prices[i] - prices[buy]
                else:
                    gain += some
                    some = 0
                    buy = i
        else:
            gain += some                  
        return gain
        #[1,2,4,2,5,7,2,4,9,0]
# @lc code=end


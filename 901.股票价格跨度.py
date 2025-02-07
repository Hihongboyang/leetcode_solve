#
# @lc app=leetcode.cn id=901 lang=python3
# @lcpr version=30204
#
# [901] 股票价格跨度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
class StockSpanner:
    def __init__(self):
        self.cur_day = -1
        self.stack = [(-1, inf)]  # 这样无需判断栈为空的情况

    def next(self, price: int) -> int:

        while self.stack[-1][1] <= price:
            self.stack.pop()

        self.cur_day += 1
        self.stack.append((self.cur_day, price))

        return self.cur_day - self.stack[-2][0]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end


#
# @lcpr case=start
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"][[], [100], [80], [60], [70], [60], [75], [85]]\n
# @lcpr case=end

#

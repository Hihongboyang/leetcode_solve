#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()  # 保存之前产生过的数
        while n != 1 and n not in seen:  # n没有出现过, 就进行计算
            seen.add(n)
            n = get_next(n)  # 计算下一个数

        return n == 1


# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

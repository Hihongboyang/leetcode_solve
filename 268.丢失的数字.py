#
# @lc app=leetcode.cn id=268 lang=python3
# @lcpr version=30204
#
# [268] 丢失的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 数学公式计算
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        n = len(nums)
        return (n + 1) * n // 2 - sum_nums



# @lc code=end


#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,0]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,0]\n
# @lcpr case=end

#

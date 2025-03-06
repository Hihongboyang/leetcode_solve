#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

#  ┌───┬───┬───┬───┬───┬───┬───┐
#  | 3 | 4 |-1 | 1 | 9 |-5 | 6 |  小于0的数变为n+1
#  └───┴───┴───┴───┴───┴───┴───┘
#            V           V
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  | 3 | 4 | 8 | 1 | 9 | 8 | 6 |  将nums[i]-1位置的数字变成负数, 标记这个位置
#  └───┴───┴───┴───┴───┴───┴───┘
#      ↘  ↘ ↙            ↙
#    ↙    ↘  ↘         ↙
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  |-3 | 4 |-8 |-1 | 9 |-8 | 6 |  遍历数组找出第一"非负"数,就是第一个缺失的数
#  └───┴───┴───┴───┴───┴───┴───┘
# 


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for i in range(length):
            n = abs(nums[i])
            if n <= length:
                nums[n - 1] = -abs(nums[n - 1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1


# @lc code=end


#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

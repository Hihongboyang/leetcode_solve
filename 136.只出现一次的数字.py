#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_len = len(nums)
        for i in range(0, num_len, 2):
            try:
                if nums[i+1] - nums[i] !=0:
                    return nums[i]
            except IndexError:
                return nums[i]

# @lc code=end


#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 0:
                return True

        return False

# @lc code=end


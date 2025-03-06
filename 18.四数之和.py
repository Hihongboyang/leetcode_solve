#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30204
#
# [18] 四数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    while (
                        left < right and left > j + 1 and nums[left] == nums[left - 1]
                    ):
                        left += 1
                    while (
                        left < right
                        and right < n - 1
                        and nums[right + 1] == nums[right]
                    ):
                        right -= 1
                    if (
                        left < right
                        and nums[i] + nums[j] + nums[left] + nums[right] == target
                    ):
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

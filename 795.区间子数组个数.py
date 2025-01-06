#
# @lc app=leetcode.cn id=795 lang=python3
# @lcpr version=30204
#
# [795] 区间子数组个数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        cnt = 0
        lastMidIndex = -1 # i1
        lastMoreIndex = -1 # i2

        for r in range(len(nums)):
            if nums[r] > right:
                lastMoreIndex = r # 遇到 2，更新 i2
            elif nums[r] >= left:
                lastMidIndex = r # 遇到 1，更新 i1

            # i1 > i2 时才累计，可以简化为 cnt += max(0, lastMidIndex - lastMoreIndex)  
            if lastMidIndex > lastMoreIndex:
                cnt += lastMidIndex - lastMoreIndex

        return cnt
# @lc code=end



#
# @lcpr case=start
# [2,1,4,3]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,9,2,5,6]\n2\n8\n
# @lcpr case=end

#


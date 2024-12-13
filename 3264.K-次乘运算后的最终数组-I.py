#
# @lc app=leetcode.cn id=3264 lang=python3
# @lcpr version=30204
#
# [3264] K 次乘运算后的最终数组 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums
        
# @lc code=end



#
# @lcpr case=start
# [2,1,3,5,6]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n3\n4\n
# @lcpr case=end

#


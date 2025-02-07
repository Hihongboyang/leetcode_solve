#
# @lc app=leetcode.cn id=2239 lang=python3
# @lcpr version=30204
#
# [2239] 找到最接近 0 的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return -min((abs(x), -x) for x in nums)[1]
# @lc code=end



#
# @lcpr case=start
# [-4,-2,-1,4,8]\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,1]\n
# @lcpr case=end

#


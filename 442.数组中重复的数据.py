#
# @lc app=leetcode.cn id=442 lang=python3
# @lcpr version=30204
#
# [442] 数组中重复的数据
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 和41题思路相同, 利用数组本身的容量来记录那些位置被访问了
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = set()
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ret.add(abs(n))
            else:
                nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return list(ret)


# @lc code=end


#
# @lcpr case=start
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [2, 2]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 6, 5, 5, 6]\n
# @lcpr case=end

#

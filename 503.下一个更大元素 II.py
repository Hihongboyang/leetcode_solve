#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30204
#
# [503] 下一个更大元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
# 这里的要点是使用两倍的数组长度
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [-1 for _ in range(size)]
        stack = []
        for i in range(size * 2):
            while stack and nums[i % size] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i % size]
            stack.append(i % size)

        return res
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

#


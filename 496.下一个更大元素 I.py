#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30204
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        ret = []

        for n in nums2:
            while stack and stack[-1] < n:
                prev = stack.pop()
                mapping[prev] = n
            stack.append(n)
        
        for n in nums1:
            ret.append(mapping.get(n, -1))

        return ret
# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4]\n
# @lcpr case=end

#


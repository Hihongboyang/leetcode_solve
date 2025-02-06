#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ret = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if stack:
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ret += high * (right - left + 1)
                else:
                    break

            stack.append(i)
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#


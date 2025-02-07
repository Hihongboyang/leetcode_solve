#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ret = 0
        heights.append(0)

        for index in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[index]:
                cur = stack.pop()  # 从index的上一个比他大的元素开始
                left = stack[-1] + 1 if stack else 0  # 不断向左移动边界
                right = index - 1  # right边界在for循环中不变
                ret = max(ret, (right - left + 1) * heights[cur])
            stack.append(index)

        return ret


# @lc code=end


#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

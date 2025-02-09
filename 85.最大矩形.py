#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=30204
#
# [85] 最大矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

""" 单调栈
借用84题的解决思路. 矩阵中每一列可以看作是一个高度为n的柱体, 
一层一层向下遍历, 每一层就可以借用84题的解题思路

   ^
 [[|1, 0, 1, 0, 0],
───└────────────────────>
  [ 1, 0, 1, 1, 1],
  [ 1, 1, 1, 1, 1],
  [ 1, 0, 0, 1, 0]]
-------------------------------
   ^ ┌─┐    ┌─┐
 [[| |1|, 0,|1|, 0, 0 ],
   | | |    | └──────┐
  [| |1|, 0,|1, 1, 1 |],
   | └─┘    └────────┘     
───└────────────────────>
  [   1,  1, 1,  1, 1],
  [   1,  0, 0,  1, 0]]
-------------------------------
   ^ ┌─┐     ┌─┐
 [[| |1|, 0, |1|,0, 0 ],
   | | |     | └─────┐],
  [| |1|, 0, |1, 1, 1|],
   | | └─────┘       |
  [| |1|, 1, |1, 1, 1|],
   | └───────────────┘
───└────────────────────>
  [   1,  0, 0,  1, 0]]
-------------------------------
   ^ ┌─┐
 [[| |1|, 0, 1, 0, 0],
   | | |       ┌─┐
  [| |1|, 0, 1,|1|, 1],
  [| |1|, 1, 1,|1|, 1],
  [| |1|, 0, 0,|1|, 0]]
   | └─┘       └─┘ 
───└────────────────────>
"""
from itertools import takewhile

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        width = len(matrix)
        ret = 0

        while width > 0:
            # col_sum = [0] * len(matrix[0])
            # for i, col in enumerate(zip(*matrix[:width])):  # 将每一列数组合在一起计算
            #     for n in col[::-1]:  # 需要从后向前遍历, 当遇到'0'就停止计数
            #         if n == '0':
            #             break
            #         else:
            #             col_sum[i] += 1  # 统计出的大小就是柱体的高度
            # 用一行代码代替上面的逻辑
            col_sum = [
                sum(1 for _ in takewhile(lambda x: x == "1", col[::-1]))
                for col in zip(*matrix[:width])
            ]
            ret = max(ret, self.largestRectangleArea(col_sum))
            width -= 1

        return ret

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
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ret = [0] * length
        stack = []
        for index in range(length):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                prev = stack.pop()
                ret[prev] = (index - prev)

            stack.append(index)
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#


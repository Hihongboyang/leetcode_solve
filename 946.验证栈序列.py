#
# @lc app=leetcode.cn id=946 lang=python3
# @lcpr version=30204
#
# [946] 验证栈序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return len(stack) == 0


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n[4,5,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n[4,3,5,1,2]\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=402 lang=python3
# @lcpr version=30204
#
# [402] 移掉 K 位数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈
# 这个题需要判断栈顶的元素是不是比当前的元素大(栈顶的元素是前面的元素)
# 如果栈顶的元素比当前元素大, 就将栈顶元素弹出(舍弃)
# 这样就按顺序将所有大的元素都去除了
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remain = len(num) - k
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        return ''.join(stack[:remain]).lstrip('0') or '0'


        
# @lc code=end



#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

# @lcpr case=start
# "1173"\n2\n
# @lcpr case=end

#


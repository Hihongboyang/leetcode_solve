#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_stack = list()


    def push(self, val: int) -> None:
        self.list_stack.append(val)


    def pop(self) -> None:
        self.list_stack.pop()


    def top(self) -> int:
        return self.list_stack[-1]


    def getMin(self) -> int:
        return min(self.list_stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


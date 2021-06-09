"""对栈中的数据进行排序"""
class SortedStack:

    def __init__(self):
        self.stack = list()
        self.point = 0

    def push(self, val: int) -> None:
        temp_stack = list()
        while(self.stack):
            temp = self.stack.pop(-1)
            if temp < val:
                temp_stack.append(temp)
            else:
                self.stack.append(temp)
                break
        
        self.stack.append(val)

        while(temp_stack):
            self.stack.append(temp_stack.pop(-1))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.stack


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
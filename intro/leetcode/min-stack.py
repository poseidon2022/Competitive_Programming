class MinStack:

    def __init__(self):
        self.stack = []
        self.keep_min = []
        
    def push(self, val: int) -> None:
        if not self.keep_min or (self.keep_min and self.keep_min[-1]>= val): self.keep_min.append(val)
        self.stack.append(val)
    def pop(self) -> None:
        if self.keep_min and self.keep_min[-1] == self.stack[-1]: self.keep_min.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack[0] if not self.keep_min else self.keep_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
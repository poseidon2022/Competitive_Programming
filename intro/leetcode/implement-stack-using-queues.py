class MyStack:

    def __init__(self):

        self.queue1 = deque()

    def push(self, x: int) -> None:

        self.queue1.append(x)
        

    def pop(self) -> int:
        queue2 = deque()
        if not self.queue1: return
        while len(self.queue1) > 1:
            queue2.append(self.queue1.popleft())
        
        wan = self.queue1[-1]
        self.queue1 = queue2
        return wan

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
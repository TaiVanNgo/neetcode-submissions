class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        return None

    def pop(self) -> int:
        # pop left and append to the same queue except the last one
        for num in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        # remove and return the number we need to pop
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
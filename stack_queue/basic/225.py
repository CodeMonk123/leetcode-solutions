class MyStack:
    def __init__(self):
        self.queue1, self.queue2 = [], []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        val = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def top(self) -> int:
        if self.empty():
            return -1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        val = self.queue1.pop()
        self.queue2.append(val)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        for _ in range(len(self.q1)):
            self.q2.append(self.q1.pop())
        self.q2.append(x)
        for _ in range(len(self.q2)):
            self.q1.append(self.q2.pop())

    def pop(self) -> int:
        return self.q1.pop()

    def peek(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
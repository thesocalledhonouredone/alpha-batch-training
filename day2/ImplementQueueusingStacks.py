class MyQueue:

    def __init__(self):
        self.st1 = list()
        self.st2 = list()

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        self.st2 = self.st1[::-1]
        temp = self.st2[-1]
        self.st2.pop()
        self.st1 = self.st2[::-1]
        self.st2 = []
        return temp

        
    def peek(self) -> int:
        self.st2 = self.st1[::-1]
        temp = self.st2[-1]
        st2 = []
        return temp

    def empty(self) -> bool:
        return len(self.st1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
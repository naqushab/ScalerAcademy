class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        aux = []
        while self.st:
            aux.append(self.st.pop())
        self.st.append(x)
        while aux:
            self.st.append(aux.pop())

    def pop(self) -> int:
        return self.st.pop()

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
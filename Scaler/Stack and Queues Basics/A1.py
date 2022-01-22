from collections import deque

class MinStack:
    def __init__(self):
        self.st = deque()
        self.min_st = deque()
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.st.append(x)
        self.min_st.append(min(x, self.min_st[-1] if len(self.min_st) > 0 else x))
        return x

    # @return nothing
    def pop(self):
        if len(self.st) > 0:
            self.st.pop()
        if len(self.min_st) > 0:
            self.min_st.pop()

    # @return an integer
    def top(self):
        return self.st[-1] if len(self.st) > 0 else -1

    # @return an integer
    def getMin(self):
        return self.min_st[-1] if len(self.st) > 0 else -1

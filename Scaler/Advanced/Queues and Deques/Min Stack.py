class MinStack:
    def __init__(self):
        self.st = []
        self.min_st = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.min_st) == 0 or self.min_st[-1] >= x:
            self.min_st.append(x)
        self.st.append(x)
        return self.st[-1]

    # @return nothing
    def pop(self):
        if self.st:
            if self.st[-1] == self.min_st[-1]:
                self.min_st.pop()
            self.st.pop()

    # @return an integer
    def top(self):
        return self.st[-1] if len(self.st) > 0 else -1

    # @return an integer
    def getMin(self):
        return self.min_st[-1] if len(self.st) > 0 else -1
class MostFrequentStack:
    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0
        self.stacks = {}

    def push(self, val):
        val_cnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = val_cnt
        if val_cnt > self.max_cnt:
            self.max_cnt = val_cnt
            self.stacks[val_cnt] = []
        self.stacks[val_cnt].append(val)
        return -1

    def pop(self):
        if self.stacks:
            ret = self.stacks[self.max_cnt].pop()
            self.cnt[ret] -= 1
            if not self.stacks[self.max_cnt]:
                del self.stacks[self.max_cnt]
                self.max_cnt -= 1
            return ret
        else:
            return -1

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        mfs = MostFrequentStack()
        ans = []
        for op, val in A:
            if op == 1:
                ret = mfs.push(val)
            else:
                ret = mfs.pop()
            ans.append(ret)
        return ans
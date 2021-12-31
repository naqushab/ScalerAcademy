class Solution:

    def __init__(self, nums: List[int]):
        self.org = list(nums)
        self.ans = nums

    def reset(self) -> List[int]:
        self.ans = self.org
        self.org = list(self.org)
        return self.ans
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.ans)):
            new_i = random.randrange(i, len(self.ans))
            self.ans[i], self.ans[new_i] = self.ans[new_i], self.ans[i]
        return self.ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
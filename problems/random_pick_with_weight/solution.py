class Solution:

    def __init__(self, w: List[int]):
        self.wt = w
        self.prefix_wt = []
        for i in range(len(w)):
            if i == 0:
                self.prefix_wt.append(w[i])
            else:
                self.prefix_wt.append(w[i] + self.prefix_wt[-1])

    def pickIndex(self) -> int:
        rand = random.random() * self.prefix_wt[-1]
        l, r = 0, len(self.prefix_wt)-1
        while l < r:
            m = (l + r)//2
            if self.prefix_wt[m] < rand:
                l = m+1
            else:
                r = m
        return l
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
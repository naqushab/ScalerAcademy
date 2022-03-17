class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = (l+r)//2
            if self.can_eat(piles, h, m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans
    
    def can_eat(self, piles, h, m):
        time = 0
        for i in range(len(piles)):
            time += math.ceil(piles[i]/m)
        return time <= h
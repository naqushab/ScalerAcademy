class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(n):
            return sum([math.ceil(pile/n) for pile in piles]) <= h
        
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l
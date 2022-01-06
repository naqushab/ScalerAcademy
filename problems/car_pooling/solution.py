class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hwy = [0]*1001
        for t in trips:
            hwy[t[1]] += t[0]
            hwy[t[2]] -= t[0]
        
        for p in hwy:
            capacity -= p
            if capacity < 0:
                return False
        
        return True
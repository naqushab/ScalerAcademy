import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return -(p[0]**2 + p[1]**2)
        
        res = []
        for p in points[:k]:
            heapq.heappush(res, (dist(p), p))
        
        for p in points[k:]:
            new_dist = dist(p)
            top_p = res[0]
            if new_dist > top_p[0]:
                heapq.heappop(res)
                heapq.heappush(res, (dist(p), p))
                
        ans = []
        
        while len(res) > 0:
            p = heapq.heappop(res)
            ans.append(p[1])
            
        return ans
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist_to_origin(point):
            x, y = point
            return x*x + y*y
        
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-dist_to_origin(points[i]), points[i]))
        n = len(points)
        for i in range(k, n):
            if dist_to_origin(points[i]) < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist_to_origin(points[i]), points[i]))
        ans = []
        for distance, point in heap:
            ans.append(point)
        return ans
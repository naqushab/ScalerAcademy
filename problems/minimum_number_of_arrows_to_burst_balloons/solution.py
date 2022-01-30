class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        ans = 1
        i = 1
        while i < len(points):
            while i < len(points) and prev_end >= points[i][0]:
                prev_end = min(prev_end, points[i][1])
                i += 1
            else:
                if i < len(points):
                    ans += 1
                    prev_end = points[i][1]
        return ans
            
            
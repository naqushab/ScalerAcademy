class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort()
        
        common = points[0]
        
        i = 1
        while i < len(points):
            while i < len(points) and common[1] >= points[i][0]:
                common[0] = max(common[0], points[i][0])
                common[1] = min(common[1], points[i][1])
                i += 1
            else:
                if i < len(points):
                    res += 1
                    common = points[i]
        return res
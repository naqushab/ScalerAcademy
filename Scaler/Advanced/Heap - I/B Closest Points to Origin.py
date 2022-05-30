import heapq
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        h = []
        n = len(A)
        for point in A:
            x, y = point
            dist = x*x + y*y
            if len(h) < B:
                heapq.heappush(h, (-dist, point))
            else:
                if dist < -h[0][0]:
                    heapq.heappushpop(h, (-dist, point))
        ans = []
        for dist, point in h:
            ans.append(point)
        return ans
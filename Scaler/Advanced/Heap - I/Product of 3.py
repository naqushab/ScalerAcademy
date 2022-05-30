class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = []
        n = len(A)
        if n <= 2:
            return [-1]*n
        else:
            import heapq
            h = []
            for i in range(n):
                heapq.heappush(h, A[i])
                if len(h) < 3:
                    B.append(-1)
                    continue
                while len(h) > 3:
                    heapq.heappop(h)
                p = h[0]*h[1]*h[2]
                B.append(p)                   
            return B
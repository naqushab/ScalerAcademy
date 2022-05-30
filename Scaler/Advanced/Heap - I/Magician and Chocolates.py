class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        import heapq, math
        h = []
        ans = 0
        for n in B:
            heapq.heappush(h, -n)
        for _ in range(A):
            chocolates = -heapq.heappop(h)
            ans += chocolates
            heapq.heappush(h, -math.floor(chocolates//2))
        return ans % (10**9 + 7)
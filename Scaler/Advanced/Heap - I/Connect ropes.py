class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        import heapq
        h = []
        for n in A:
            heapq.heappush(h, n)
        c = 0
        while len(h) != 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            c += a + b
            heapq.heappush(h, a+b)
        return c
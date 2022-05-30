class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import heapq
        n = len(A)
        h = []
        for num in A:
            heapq.heappush(h, num)
        for _ in range(B):
            num = heapq.heappop(h)
            heapq.heappush(h, -num)
        return sum(h)

if __name__ == '__main__':
    A = [ 48, -14, 53, -52, 68, -52 ]
    B = 9
    print(Solution().solve(A, B))
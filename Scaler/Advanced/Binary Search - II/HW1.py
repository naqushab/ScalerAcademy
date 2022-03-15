import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        n = len(A)
        heap = []
        for i in range(B):
            heapq.heappush(heap, A[i])
        for i in range(B, n):
            if A[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, A[i])
        return heap[0]

if __name__ == '__main__':
    s = Solution()
    print(s.kthsmallest([2, 1, 4, 3, 2], 3))
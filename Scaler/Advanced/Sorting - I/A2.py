import heapq

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def kthsmallest(self, A, B):
        heap = []
        n = len(A)
        for i in range(B):
            heapq.heappush(heap, -A[i])
        for i in range(B, n):
            if A[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -A[i])
        return -heap[0]

if __name__ == '__main__':
    A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
    B = 9
    print(sorted(A))
    print(Solution().kthsmallest(A, B))

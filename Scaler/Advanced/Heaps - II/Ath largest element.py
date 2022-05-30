import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        h, ans = [], []
        n = len(B)
        for i in range(n):
            heapq.heappush(h, B[i])
            if i < A-1:
                ans.append(-1)
            elif i == A-1:
                ans.append(h[0])
            else:
                heapq.heappop(h)
                ans.append(h[0])
        return ans

if __name__ == '__main__':
    A = 4
    B = [1,2,3,4,5,6]
    print(Solution().solve(A, B))
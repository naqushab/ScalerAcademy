class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        ans = 0
        for i in range(1, n):
            steps = max(A[i], A[i-1]+1) - A[i]
            A[i] = A[i] + steps
            ans += steps
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solve([ 51, 6, 10, 8, 22, 61, 56, 48, 88, 85, 21, 98, 81, 76, 71, 68, 18, 6, 14, 23, 72, 18, 56, 30, 97, 100, 81, 5, 99, 2, 85, 67, 46, 32, 66, 51, 76, 53, 36, 31, 81, 56, 26, 75, 69, 54, 54, 54, 83, 41, 86, 48, 7, 32, 85, 23, 47, 23, 18, 45, 79, 95, 73, 15, 55, 16, 66, 73, 13, 85, 14, 80, 39, 92, 66, 20, 22, 25, 34, 14, 51, 14, 17, 10, 100, 35, 9, 83, 31, 60, 24, 37, 69, 62 ]))
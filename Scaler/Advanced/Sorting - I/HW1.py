class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        if n == 0 or B == 0:
            return 0
        ans = float('+inf')
        for start in range(n-B+1):
            ans = min(ans, A[start+B-1] - A[start])
        return ans
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l, r = 0, n-1
        count = 0
        while l <= r:
            p = A[l]*A[r]
            if p >= B:
                r -= 1
            else:
                count += (2*(r-l+1) - 1)
                count %= (10**9 + 7)
                l += 1
        return count % (10**9 + 7)
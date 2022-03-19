class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l, r = 0, n-1
        count = 0
        while l < r:
            s = A[l] + A[r]
            if s == B:
                count += 1
                r -= 1
            elif s < B:
                l += 1
            else:
                r -= 1
        return count 
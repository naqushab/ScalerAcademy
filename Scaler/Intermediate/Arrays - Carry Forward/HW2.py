class Solution:
    # @param A : list of integers
    # @return a string
    def solve(self, A):
        return "YES" if len(A)%2 == 0 and A[0]%2==0 and A[-1]%2==0 else "NO"
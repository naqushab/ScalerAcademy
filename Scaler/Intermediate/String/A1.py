class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        return ' '.join(A.strip().split()[::-1])
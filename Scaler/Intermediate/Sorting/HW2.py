class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        A.sort(reverse=True)
        for i, n in enumerate(A):
            ans += (i+1)*n
        return ans
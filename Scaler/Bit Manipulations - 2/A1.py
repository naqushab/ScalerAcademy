class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        while A > 0:
            A = A& A-1
            ans += 1
        return ans
        
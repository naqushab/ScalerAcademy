class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        m = {}
        for n in A:
            if B^n in m:
                ans += 1
            m[n] = 1
        return ans
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        l = len(A)
        for i, s in enumerate(A):
            if s.upper() in ['A', 'E', 'I', 'O', 'U']:
                ans += l-i
        return ans%10003
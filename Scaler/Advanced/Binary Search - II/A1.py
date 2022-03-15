class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A <= 1:
            return A
        l, r = 1, A//2
        ans = float('-inf')
        while l <= r:
            m = (l+r)//2
            if m*m == A:
                return m
            elif m*m < A:
                l = m+1
                ans = max(ans, m)
            else:
                r = m-1
        return ans
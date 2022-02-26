class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans = 0
        for i in range(32, -1, -1):
            if A & (1<<i):
                ans = ans | 1 <<(32-i-1)
        return ans
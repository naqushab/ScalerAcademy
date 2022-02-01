class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_a = 0
        ans = 0
        for n in A:
            if n == 'A':
                count_a += 1
            if n == 'G':
                ans += count_a
        return ans%((10**9) + 7)
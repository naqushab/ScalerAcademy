class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        count_a = 0
        for ch in A:
            if ch == 'A':
                count_a += 1
            if ch == 'G':
                ans += count_a
        return ans
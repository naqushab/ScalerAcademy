from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        running_sum, ans = 0,0
        m = defaultdict(lambda: 0)
        for n in A:
            running_sum += n
            if running_sum == B:
                ans += 1
            if running_sum - B in m:
                ans += m[running_sum - B]
            m[running_sum] += 1
        return ans
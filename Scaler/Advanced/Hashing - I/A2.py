class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        m = {}
        min_dist = len(A)
        for i, v in enumerate(A):
            if v in m:
                min_dist = min(i - m[v], min_dist)
            m[v] = i
        return min_dist if min_dist < len(A) else -1

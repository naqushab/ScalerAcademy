class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if not A:
            return 0
        intervals = list(zip(A, B))
        intervals.sort(key=lambda x: x[1])
        ans = 1
        prev_end = intervals[0][-1]
        for interval in intervals[1:]:
            if prev_end <= interval[0]:
                prev_end = interval[1]
                ans += 1
        return ans
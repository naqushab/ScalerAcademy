from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c = Counter(A)
        odd_count = 0
        for k, v in c.items():
            if v % 2 == 1:
                odd_count += 1
            if odd_count > 1:
                return 0
        return 1
from itertools import accumulate
from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ps = list(accumulate(A))
        if 0 in ps:
            return 1
        else:
            c = Counter(ps)
            for k, v in c.items():
                if v >= 2:
                    return 1
            return 0
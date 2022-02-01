from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c = Counter(A)
        for n in A:
            if c[n] > 1:
                return n
        return -1
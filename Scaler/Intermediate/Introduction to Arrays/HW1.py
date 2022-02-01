class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = 0
        if B not in A:
            return -1
        for n in A:
            if n > B:
                c += 1
        return c
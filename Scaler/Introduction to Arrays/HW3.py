class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_e = float('-inf')
        min_o = float('+inf')
        for i, n in enumerate(A):
            if n % 2 == 0:
                max_e = max(max_e, n)
            else:
                min_o = min(min_o, n)
        return max_e - min_o
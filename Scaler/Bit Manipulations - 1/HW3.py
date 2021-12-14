class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        count_odd = 0
        for n in A:
            if n%2 == 1:
                count_odd += 1
        return "Yes" if count_odd %2 == 0 else "No"
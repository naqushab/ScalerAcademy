class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A%400 == 0:
            return 1
        elif A%100 != 0 and A%4 == 0:
            return 1
        else:
            return 0
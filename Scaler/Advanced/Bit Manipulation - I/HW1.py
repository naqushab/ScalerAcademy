class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        x = 0
        for n in A:
            x ^= n
        if x%2==0:
            return 'Yes'
        else:
            return 'No'
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        x = 0
        for n in A:
            x ^= n
        return x
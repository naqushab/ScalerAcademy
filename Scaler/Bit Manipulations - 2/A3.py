class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        set_bit = 0
        while A > 0:
            A = A&(A-1)
            set_bit += 1
        return set_bit
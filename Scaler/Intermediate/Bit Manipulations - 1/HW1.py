class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        set_bits = 0
        while A:
            if A&1 == 1:
                set_bits += 1
            A //=2
        return set_bits
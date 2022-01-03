class Solution:
    def reverseBits(self, n: int) -> int:
        r, p = 0, 31
        while n>0:
            r = r + ((n&1) << p)
            n = n>>1
            p -= 1
        return r
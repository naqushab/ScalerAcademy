class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l = len(bin(n)) - 2
        for power in range(0, l):
            mask = 1 << power
            n = n ^ (1 << power)
        return n
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        i = 1
        c = 0
        while i*i <= n:
            c += 1
            i += 1
        return c
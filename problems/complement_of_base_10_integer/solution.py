class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        s = ""
        while n > 0:
            lsb = n&1
            compl = lsb^1
            n = n>>1
            s += str(compl)
        s = s[::-1]
        ans = 0
        p = 0
        i = len(s)-1
        while i >= 0:
            ans += int(s[i])*pow(2, p)
            i -= 1
            p += 1
        return ans
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = a[::-1]
        n2 = b[::-1]
        i = 0
        c = 0
        ans = []
        while i < len(n1) or i < len(n2) or c > 0:
            s = c
            if i < len(n1):
                s += int(n1[i])
            if i < len(n2):
                s += int(n2[i])
            d, c = s%2, s//2
            ans.append(str(d))
            i += 1
        return ''.join(ans[::-1])
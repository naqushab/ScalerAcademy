class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        f = s[0]
        r1 = int(s[1])
        sc = s[3]
        r2 = int(s[4])
        ans = []
        for i in range(ord(f), ord(sc)+1):
            for j in range(r1, r2+1):
                s = chr(i) + str(j)
                ans.append(s)
        return ans
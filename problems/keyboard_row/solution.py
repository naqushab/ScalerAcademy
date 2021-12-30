from collections import Counter

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def select(w, m):
            for c in w:
                if c.lower() not in m:
                    return False
            return True
        qw = Counter('qwertyuiop')
        asd = Counter('asdfghjkl')
        zx = Counter('zxcvbnm')
        ans = []
        for w in words:
            sel = False
            if w[0].lower() in qw:
                sel = select(w, qw)
            elif w[0].lower() in asd:
                sel = select(w, asd)
            elif w[0].lower() in zx:
                sel = select(w, zx)
                
            if sel:
                ans.append(w)
                
        return ans
        
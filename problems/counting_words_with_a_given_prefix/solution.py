class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c = 0
        for s in words:
            if s.startswith(pref):
                c+= 1
        return c
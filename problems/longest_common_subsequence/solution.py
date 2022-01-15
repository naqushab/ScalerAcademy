class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @functools.lru_cache(None)
        def lcs(s1, s2, i1, i2):
            if i1 < 0 or i2 < 0:
                return 0
            if s1[i1] == s2[i2]:
                return 1 + lcs(s1, s2, i1-1, i2-1)
            else:
                return max(lcs(s1, s2, i1-1, i2), lcs(s1, s2, i1, i2-1))
        
        return lcs(text1, text2, len(text1)-1, len(text2)-1)
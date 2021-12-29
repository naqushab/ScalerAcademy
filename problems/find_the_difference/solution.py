class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpbt = [0]*26
        for ch in s:
            alpbt[ord(ch)-ord('a')] += 1
        for ch in t:
            alpbt[ord(ch)-ord('a')] -= 1
        for i, a in enumerate(alpbt):
            if a == -1:
                return chr(i+97)
            
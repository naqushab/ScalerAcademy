class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        if n == 0 and h == 0:
            return 0
        elif h == 0:
            return -1
        elif n == 0:
            return 0
        for i in range(h-n+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
        return -1
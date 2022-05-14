class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        l = 0
        odd_len = False
        for k, v in c.items():
            if v % 2 == 0:
                l += v
            else:
                odd_len = True
                l += (v - 1)
        return l + 1 if odd_len else l
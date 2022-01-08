class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        ans = 0
        odd = 0
        for k, v in c.items():
            if v % 2 == 0:
                ans += v
            else:
                odd += 1
                ans += (v-1)
        return ans if odd == 0 else ans+1
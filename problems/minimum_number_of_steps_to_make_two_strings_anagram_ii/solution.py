class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = collections.Counter(s)
        for ch in t:
            if ch in c:
                c[ch] -= 1
            else:
                c[ch] = -1
        ans = 0
        for k, v in c.items():
            ans += abs(v)
        return ans
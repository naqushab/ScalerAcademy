class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hsh = collections.defaultdict(lambda: 0)
        n = len(s)
        k = len(p)
        for ch in p:
            hsh[ch] += 1
        ans = []
        runhsh = collections.defaultdict(lambda: 0)
        window_start = 0
        for window_end in range(n):
            runhsh[s[window_end]] += 1
            if window_end - window_start + 1 == k:
                if runhsh == hsh:
                    ans.append(window_start)
                runhsh[s[window_start]] -= 1
                if runhsh[s[window_start]] == 0:
                    del runhsh[s[window_start]]
                window_start += 1
        return ans
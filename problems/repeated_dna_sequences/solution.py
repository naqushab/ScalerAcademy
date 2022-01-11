class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        m = collections.defaultdict(lambda: 0)
        window_start = 0
        for window_end in range(len(s)):
            if window_end - window_start + 1 == 10:
                m[s[window_start:window_end+1]] += 1
                window_start += 1
        ans = []
        for k, v in m.items():
            if v > 1:
                ans.append(k)
        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        m = {}
        length = 0
        for window_end in range(0, len(s)):
            ch = s[window_end]
            if ch not in m:
                m[ch] = window_end
                length = max(length, window_end-window_start+1)
            else:
                while s[window_start] != ch:
                    del m[s[window_start]]
                    window_start += 1
                window_start += 1
                m[ch] = window_end
        return length
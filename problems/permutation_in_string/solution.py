from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1l = len(s1)
        s1_c = sorted(Counter(s1).items())
        for i in range(len(s2)-s1l+1):
            s2snip = s2[i:i+s1l]
            s2snip_c = sorted(Counter(s2snip).items())
            if s2snip_c == s1_c:
                return True
            
        return False
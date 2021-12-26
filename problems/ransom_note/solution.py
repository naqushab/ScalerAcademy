from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm_rn = Counter(ransomNote)
        hm_mag = Counter(magazine)
        
        for k, v in hm_rn.items():
            if k not in hm_mag or v > hm_mag[k]:
                return False
        return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = collections.Counter(magazine)
        for ch in ransomNote:
            if ch in magazine_counter:
                magazine_counter[ch] -= 1
                if magazine_counter[ch] == 0:
                    del magazine_counter[ch]
            else:
                return False
        return True
                
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word.capitalize() == word or word.lower() == word
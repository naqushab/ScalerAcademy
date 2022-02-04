class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def get_ord(ch):
            return ord(ch) - ord('a')
        n = len(letters)
        l = 0
        r = n - 1
        while l <= r:
            m = (l+r)//2
            if target < letters[m]:
                r = m - 1
            else:
                l = m + 1
        return letters[l%n]
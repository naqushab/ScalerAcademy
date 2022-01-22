class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        possible = [0]*n + [upper]
        for i in range(n-1, -1, -1):
            possible[i] = possible[i+1] - differences[i]
        maxp = max(possible)
        minp = min(possible)
        if maxp > upper and minp < lower:
            return 0
        else:
            count = 0
            for i in range(minp-lower+1):
                if maxp-i <= upper and minp-i >= lower:
                    count += 1
            return count
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = len(columnTitle)
        for i in range(n):
            num = ord(columnTitle[i]) - ord('A') + 1
            ans += num*pow(26, n-i-1)
        return ans
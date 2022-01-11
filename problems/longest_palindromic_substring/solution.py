class Solution:
    def longestPalindrome(self, s: str) -> str:
        st, end = 0, 0
        for i in range(len(s)):
            l1 = self.longest_pal(s, i, i)
            l2 = self.longest_pal(s, i, i+1)
            l = max(l1, l2)
            if l > end-st:
                st = i - ((l-1)//2)
                end = i+ (l//2)
        return s[st:end+1]
    
    def longest_pal(self, s, i, j):
        while i >=0 and j< len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j-i-1
    
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        s = []
        for c in A:
            if c.isalnum():
                s.append(c.lower())
        return 1 if s == s[::-1] else 0
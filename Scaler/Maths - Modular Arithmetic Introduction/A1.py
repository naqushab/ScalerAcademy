class Solution:
	# @param A : string
	# @return an integer
    def titleToNumber(self, A):
        ans = 0
        l = len(A)
        for i in range(l-1, -1, -1):
            num = ord(A[i]) - ord('A') + 1
            ans += num*(26**(l-i-1))
        return ans
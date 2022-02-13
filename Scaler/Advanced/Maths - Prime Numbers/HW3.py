class Solution:
	# @param A : string
	# @return an integer
    def titleToNumber(self, A):
        ans = 0
        for i in range(len(A)):
            val = ord(A[i]) - ord('A') + 1
            ans = (ans * 26) + val
        return ans
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        m = {}
        for n in A:
            if B+n in m or n-B in m:
                return 1
            m[n] = 1
        return 0
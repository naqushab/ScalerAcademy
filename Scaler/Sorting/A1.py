class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		A.sort(reverse=True)
		if A[0] == 0:
			return 1
		for i in range(1, len(A)):
			if A[i] != A[i-1]:
				if A[i] == i:
					return 1
		return -1
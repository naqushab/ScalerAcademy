class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
        if len(A.strip()) == 0:
            return 0
        return len(A.strip().split()[-1])
class Solution:
	# @param A : list of integers
	# @return an integer
    # (x ^ y) == (x | y) - (x & y) >= |y - x|
    def findMinXor(self, A):
        A.sort()
        x = float('+inf')
        for i in range(len(A)-1):
            x = min(x, A[i]^A[i+1])
        return x

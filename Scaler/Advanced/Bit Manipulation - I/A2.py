class Solution:
	# @param A : tuple of integers
	# @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(A)):
                if A[j] & 1<<i:
                    count += 1
            if count % 3 != 0:
                ans = ans | 1<<i
        return ans
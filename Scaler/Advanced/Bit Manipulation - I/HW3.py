class Solution:
	# @param A : list of integers
	# @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0
        for i in range(32):
            set_count = 0
            for j in range(n):
                if A[j] & 1 == 1:
                    set_count += 1
                A[j] >>= 1
            ans += (set_count * (n-set_count)*2)
        return ans % (10**9 + 7)
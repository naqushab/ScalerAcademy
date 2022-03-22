class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
    def solve(self, A, B, C):
        i, j, k = 0, 0, 0
        m, n, o = len(A), len(B), len(C)
        ans = float('+inf')
        while i < m and j < n and k < o:
            d = self.calc(A[i], B[j], C[k])
            ans = min(ans, d)
            min_num = min(A[i], B[j], C[k])
            if min_num == A[i]:
                i += 1
            elif min_num == B[j]:
                j += 1
            else:
                k += 1
        return ans

    def calc(self, a, b, c):
        return abs(max(a, b, c) - min(a, b, c))
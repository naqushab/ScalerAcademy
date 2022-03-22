class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
    def minimize(self, A, B, C):
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
        return max(abs(a - b), abs(b - c), abs(c - a))
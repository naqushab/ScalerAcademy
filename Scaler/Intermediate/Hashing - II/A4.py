class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
        m = {}
        window_start = 0
        ans = []
        for window_end in range(len(A)):
            if A[window_end] not in m:
                m[A[window_end]] = 0
            m[A[window_end]] += 1

            if window_end - window_start + 1 == B:
                ans.append(len(m))
                m[A[window_start]] -= 1
                if m[A[window_start]] == 0:
                    del m[A[window_start]]
                window_start += 1
        return ans
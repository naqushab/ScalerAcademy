class Solution:
	# @param A : list of integers
	# @return an integer
    def maxArea(self, A):
        l, r = 0, len(A)-1
        max_area = 0
        while l < r:
            area = min(A[l], A[r]) * (r-l)
            max_area = max(max_area, area)
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return max_area
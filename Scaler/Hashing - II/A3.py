class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        s = set(A)
        l = 0
        for num in s:
            local_l = 0
            if num-1 not in s:
                while num in s:
                    local_l += 1
                    num = num+1
                l = max(l, local_l)
        return l
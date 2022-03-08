class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self, A):
        A.sort()
        max_sum, min_sum = 0, 0
        n = len(A)
        for i in range(n):
            max_sum += A[i] * (1<<i)
        A.reverse()
        for i in range(n):
            min_sum += A[i] * (1<<i)
        return (max_sum - min_sum) % ((10**9) + 7)
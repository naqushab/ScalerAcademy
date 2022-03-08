class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        n = len(A)
        half_len = n//2
        max_magic_num, min_magic_num = 0, 0
        for i in range(half_len):
            max_magic_num += abs(A[half_len + i] - A[i])
            max_magic_num %= ((10**9) + 7)
        for i in range(0, n-1, 2):
            min_magic_num += abs(A[i+1]-A[i])
            min_magic_num %= ((10**9) + 7)
        return [max_magic_num, min_magic_num]

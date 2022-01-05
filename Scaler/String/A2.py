class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        def get_palindrome_length(i, j):
            l = 0
            while i >= 0 and j < N and A[i] == A[j]:
                j += 1
                i -= 1
                l += 2
            return l
        ans = float('-inf')
        for i in range(N):
            l1 = get_palindrome_length(i, i)-1
            l2 = get_palindrome_length(i, i+1)
            ans = max(ans, l1, l2)
        return ans
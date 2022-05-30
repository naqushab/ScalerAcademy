class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        c_left, c_right = [0]*n, [0]*n
        c_left[0], c_right[n-1] = 1, 1
        for i in range(1, n):
            if A[i] > A[i-1]:
                c_left[i] = c_left[i-1] + 1
            else:
                c_left[i] = 1
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                c_right[i] = c_right[i+1] + 1
            else:
                c_right[i] = 1
        return sum(max(c_left[i], c_right[i]) for i in range(n))
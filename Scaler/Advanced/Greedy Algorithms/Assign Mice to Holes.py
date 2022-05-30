class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        n = len(A)
        time = 0
        for i in range(n):
            time = max(time, abs(B[i]-A[i]))
        return time
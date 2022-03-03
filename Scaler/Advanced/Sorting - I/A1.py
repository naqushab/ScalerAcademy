class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        i, j = 0, 0
        n = len(A)
        m = len(B)
        C = []
        while i < n and j < m:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < n:
            C.append(A[i])
            i += 1
        while j < m:
            C.append(B[j])
            j += 1
        return C

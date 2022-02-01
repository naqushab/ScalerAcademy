class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return 0
        else:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] != B[i][j]:
                        return 0
            return 1
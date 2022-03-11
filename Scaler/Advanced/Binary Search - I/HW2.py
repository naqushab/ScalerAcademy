class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n = len(A)
        m = len(A[0])
        l, r = 0, n*m-1
        while l <= r:
            mid = (l+r)//2
            i = mid//m
            j = mid%m
            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                l = mid + 1
            else:
                r = mid - 1
        return 0
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        l, r = 0, len(A)-1
        while l<=r:
            m = (l+r)//2
            if A[m] == B:
                return m
            elif A[l] <= A[m]:
                if A[l] <= B <= A[m]:
                    r = m-1
                else:
                    l = m+1
            elif A[m] <= A[r]:
                if A[m] <= B <= A[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
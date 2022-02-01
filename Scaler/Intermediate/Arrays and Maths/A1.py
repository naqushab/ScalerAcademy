class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        i=1
        me = A[0]
        c = 1
        while i<len(A):
            if A[i] == me:
                c +=1
            elif A[i] != me and c == 1:
                me = A[i]
            elif A[i] != me and c >= 2:
                c -= 1
            i +=1
        return me

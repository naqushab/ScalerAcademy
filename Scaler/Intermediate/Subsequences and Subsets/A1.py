class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        def id(ch):
            return ord(ch) - ord('a')
        if len(A) <= 2:
            return A
        
        min_indx, min_ch = 0, A[0]
        for i in range(1, len(A)-1):
            if id(A[i]) < id(min_ch):
                min_ch = A[i]
                min_indx = i
        
        next_min = A[min_indx+1]
        for i in range(min_indx+2, len(A)):
            if id(A[i]) < id(next_min):
                next_min = A[i]
        return ''.join([min_ch, next_min])
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        for ch in A:
            if ch in B:
                index = B.index(ch)
                return self.solve(A[1:], B[index+1:])
            else:
                return "NO"
        return "YES"
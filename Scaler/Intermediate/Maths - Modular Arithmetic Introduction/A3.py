class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) > 2:
            num = int(A[-3])*100 + int(A[-2])*10 + int(A[-1])
        elif len(A) == 2:
            num = int(A[-2])*10 + int(A[-1])
        else:
            num = int(A[-1])
        if num%8 == 0:
            return 1
        else:
            return 0
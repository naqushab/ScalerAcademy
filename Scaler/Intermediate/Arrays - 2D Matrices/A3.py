class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        ans = []
        for i in range(c):
            s = 0
            for j in range(r):
                s += A[j][i]
            ans.append(s)
        return ans
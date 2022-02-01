class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        fs, rs = [0]*n, [0]*n
        for i in range(n):
            if i == 0:
                fs[i] = A[i]
            else:
                fs[i] = fs[i-1] + A[i]
        for i in range(n-1, -1, -1):
            if i == n-1:
                rs[n-1-i] = A[i]
            else:
                rs[n-1-i] = rs[n-1-i-1] + A[i]
        rs = rs[::-1]
        #print(fs)
        #print(rs)
        for i in range(0, n-1):
            if fs[i] == rs[i]:
                return i
        return -1
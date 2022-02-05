class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ps, ss = [0]*n, [0]*n
        for i in range(n):
            if i == 0:
                ps[i] = A[i]
            else:
                ps[i] = ps[i-1]+A[i]
        for i in range(n-1, -1, -1):
            if i == n-1:
                ss[i] = A[i]
            else:
                ss[i] = ss[i+1] + A[i]
        
        for i in range(0, n):
            if i == 0:
                if ss[i+1] == 0:
                    return 0
            elif i == n-1:
                if ps[i-1] == 0:
                    return n-1
            elif ps[i-1] == ss[i+1]:
                return i
        return -1
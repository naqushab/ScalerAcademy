class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ps = [0]*n
        ss = [0]*n
        for i in range(n):
            if i == 0:
                ps[i] = A[i]
            else:
                ps[i] = A[i] + ps[i-1]
        for i in range(n-1, -1, -1):
            if i == n-1:
                ss[n-i-1] = A[i]
            else:
                ss[n-i-1] = A[i] + ss[n-i-1-1]
        ss = ss[::-1]
        #print(ps)
        #print(ss)
        mx = ss[n-B]
        l = 0
        while l < B and n-B+1+l < n:
            mx = max(mx, ps[l] + ss[n-B+1+l])
            l += 1
        return mx
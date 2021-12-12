class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def brute(self, A, B):
        n = len(A)
        min_cost = -1
        for i in range(n):
            c = 0
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if A[i] < A[j] < A[k]:
                        c = B[i]+B[j]+B[k]
                        if min_cost == -1:
                            min_cost = c
                        else:
                            min_cost = min(min_cost, c)
        return min_cost
    
    def solve(self, A, B):
        n = len(A)
        min_cost = float('+inf')
        for i in range(n-1):
            l, r = float('+inf'), float('+inf')
            for j in range(0, i):
                if A[j] < A[i] :
                    l = min(l, B[j])
            for j in range(i+1, n):
                if A[i] < A[j]:
                    r = min(r, B[j])
            min_cost = min(min_cost, l + r + B[i])
        return min_cost if min_cost < float('+inf') else -1
        
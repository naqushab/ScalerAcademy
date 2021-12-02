class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        se, so = [0]*n, [0]*n
        for i in range(n):
            if i%2 == 0:
                if i == 0:
                    se[i] = A[i]
                    so[i] = 0
                else:
                    se[i] = se[i-1] + A[i]
                    so[i] = so[i-1]
            else:
                so[i] = so[i-1] + A[i]
                se[i] = se[i-1]
        #print(se)
        #print(so)
        ans = 0
        for i in range(n):
            if i == 0:
                sume = se[i-1] + so[n-1] - so[i]
            else:
                sume = se[i-1] + so[n-1] - so[i]
            sumo = so[i-1] + se[n-1] - se[i]
            if sume == sumo:
                ans += 1
        return ans
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        res = []
        def recur(A):
            if A == 0:
                res.append(0)
                return
            recur(A-1)
            n = len(res)
            mask = 1 << (A-1)
            for i in range(n-1, -1, -1):
                res.append(res[i]|mask)
        recur(A)
        return res
        
    
    def iterative(self, A):
        ans = []
        for i in range(1<<A):
            ans.append(i^(i>>1))
        return ans
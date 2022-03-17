class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l, r = 0, min(A)
        ans = -1
        while l <= r:
            k = (l+r)//2
            if self.check_food_supply(A, B, k):
                ans = k
                l = k+1
            else:
                r = k-1
        return 0 if ans == -1 else ans
    
    def check_food_supply(self, A, B, k):
        centers = 0
        for i in range(len(A)):
            if k == 0:
                centers += A[i]
            else:
                centers += A[i]//k
        return centers >= B

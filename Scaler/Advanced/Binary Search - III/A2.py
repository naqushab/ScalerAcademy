class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        l, r = 0, A[-1]-A[0]
        ans = 0
        while l <= r:
            k = (l+r)//2
            if self.check_if_possible(A, B, k):
                ans = max(ans, k)
                l = k+1
            else:
                r = k-1
        return ans
    
    def check_if_possible(self, A, B, k):
        count = 1
        prev_pos = A[0]
        for i in range(1, len(A)):
            if A[i] - prev_pos >= k:
                count += 1
                prev_pos = A[i]
            if count == B:
                return True
        return False

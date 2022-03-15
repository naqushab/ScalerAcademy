class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l, r = 0, len(A)
        ans = 0
        while l <= r:
            k = (l+r)//2
            if self.check_subarray_sum(A, B, k):
                ans = max(ans, k)
                l = k+1
            else:
                r = k-1
        return ans
    
    def check_subarray_sum(self, A, B, k):
        n = len(A)
        window_start = 0
        window_sum = 0
        for window_end in range(n):
            window_sum += A[window_end]
            if window_end-window_start+1 == k:
                if window_sum > B:
                    return False
                window_sum -= A[window_start]
                window_start += 1
        return True
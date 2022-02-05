class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        gsum = A[0]
        sum = 0
        for n in A:
            sum = max(sum+n, n)
            gsum = max(gsum, sum)
        return gsum
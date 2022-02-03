'''
Q3. Max Sum Contiguous Subarray

Problem Description
Find the contiguous non empty subarray within an array, A of length N which has the largest sum.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        g_sum = A[0]
        l_sum = 0
        for n in A:
            l_sum = max(l_sum+n, n)
            g_sum = max(g_sum, l_sum)
        return g_sum
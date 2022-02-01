class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        l = len(A)
        sum = 0
        for i, n in enumerate(A):
            sum += (i+1)*(l-i)*n
        return sum
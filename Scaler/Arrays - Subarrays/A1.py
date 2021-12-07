class Solution:
    # @param A : tuple of integers
    # @return an integer
    # https://www.youtube.com/watch?v=gwUGDXO5gHU
    def maxSubArray(self, A):
        is_all_neg = True
        min_neg = float('-inf')
        for n in A:
            if n >= 0:
                is_all_neg = False
                break
            min_neg = max(min_neg, n)
        if is_all_neg:
            return min_neg
        else:
            l = len(A)
            ans = A[0]
            sum_local = A[0]
            for i in range(1, l):
                if A[i] + sum_local >= A[i]:
                    sum_local = A[i] + sum_local
                else:
                    sum_local = A[i]
                ans = max(ans, sum_local)
            return ans
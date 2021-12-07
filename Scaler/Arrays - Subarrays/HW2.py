class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                l = j-i+1
                sub_sum += A[j]
                if l%2 == 0:
                    if sub_sum < B:
                        count += 1
                else:
                    if sub_sum > B:
                        count += 1
        return count
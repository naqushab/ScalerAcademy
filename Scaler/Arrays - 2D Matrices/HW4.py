class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += A[i][j]
            ans.append(sum)
        return ans
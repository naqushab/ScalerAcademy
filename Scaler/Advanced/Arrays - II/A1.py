class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = [0] * A
        for beg, end, amount in B:
          ans[beg-1] += amount
          if end-1 != A-1:
            ans[end] -= amount
        for i in range(A):
          if i == 0:
            pass
          else:
            ans[i] = ans[i] + ans[i-1]
        return ans
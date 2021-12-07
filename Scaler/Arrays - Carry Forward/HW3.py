class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        l = len(A)
        if l == 0:
            return ans
        elif l == 1:
            return A
        else:
            ans.append(A[-1])
            max_til_now = A[-1]
            for i in range(l-2, -1, -1):
                if A[i] > max_til_now:
                    ans.append(A[i])
                    max_til_now = A[i]
            return ans
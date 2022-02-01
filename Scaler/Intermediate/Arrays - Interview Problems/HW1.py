class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        s, e, ans = 0, 0, []
        n = len(A)
        while e < n:
            if A[e] > 0:
                e += 1
                if e-s > len(ans):
                    ans = A[s:e]
            else:
                s = e+1
                e += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    s.solve(A = [5, 6, -1, 7, 8])
    s.solve(A = [1, 2, 3, 4, 5, 6])
    s.solve(A=[ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ])
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        p = 1
        for n in A:
            p *= n
        ans = []
        for n in A:
            ans.append(p//n)
        return ans
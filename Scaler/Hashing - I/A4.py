from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        a = Counter(A)
        b = Counter(B)
        ans = []
        for k, v in a.items():
            if k in b:
                ans.extend([k]*min(a[k], b[k]))
        return ans
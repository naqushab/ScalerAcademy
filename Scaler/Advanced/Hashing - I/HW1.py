from collections import Counter

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        aset = Counter(A)
        for n in B:
            if n in aset:
                ans.extend([n]*aset[n])
                del aset[n]
        rem = []
        for n in A:
            if n in aset:
                rem.extend([n]*aset[n])
                del aset[n]
        rem.sort()
        return ans + rem
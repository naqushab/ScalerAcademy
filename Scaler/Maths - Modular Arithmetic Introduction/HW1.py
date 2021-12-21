class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        f = [0] * len(A)
        for n in A:
            f[n-1] += 1
        a, b = -1, -1
        for i, n in enumerate(f):
            if n == 0:
                a = i + 1
            if n == 2:
                b = i + 1
        return [b, a]
        
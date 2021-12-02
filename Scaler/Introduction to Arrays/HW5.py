class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        res = []
        n = len(A)
        for b in B:
            a = A.copy()
            b = n-b%n
            a = self.reverse(a, 0, n-1)
            a= self.reverse(a, 0, b-1)
            a= self.reverse(a, b, n-1)
            res.append(a)
        return res

    def reverse(self, a, s, e):
        while s <= e:
            a[s], a[e] = a[e], a[s]
            s += 1
            e -= 1
        return a

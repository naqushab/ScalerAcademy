class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        c0, c1, c2 = 0, 0, 0
        for n in A:
            if n == 0:
                c0 += 1
            elif n == 1:
                c1 += 1
            elif n == 2:
                c2 += 1
        return [0]*c0 + [1]*c1 + [2]*c2
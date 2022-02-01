class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        m = 0
        i = 1
        while A>0:
            r = A%2
            A = A//2
            m += r*(5**i)
            i+=1
        return m
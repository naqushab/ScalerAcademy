class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        X = 0
        Y = 0
        l = len(bin(A)) - 2
        Y = 1 << (l)
        for i in range(l):
            mask = 1<<i
            if mask & A == 0:
                X = X | mask
        return X ^ Y

if __name__ == '__main__':
    s = Solution()
    print(s.solve(2))
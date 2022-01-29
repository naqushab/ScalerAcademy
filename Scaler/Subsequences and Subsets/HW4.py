class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def checkbit(i, j):
            return i & (1 << (j))
        
        n = len(A)
        for i in range(2**n):
            s = 0
            for j in range(n):
                if checkbit(i, j):
                    s += A[j]
            if s == B:
                return 1
        return 0

if __name__ == "__main__":
    s = Solution()
    print(s.solve(A=[ 53, 33, 66, 44, 91, 75, 28, 47, 88, 56 ], B=362))
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.recursive(A, B)

    # debug later on - why it is failing
    def iterative_bit(self, A, B):
        count_set = 0
        while B > 0:
            B = B & B-1
            count_set += 1
        if count_set % 2 == 0:
            return 1
        else:
            return 0

    def recursive(self, A, B):
        if A == 1:
            return 0
        parent = self.solve(A-1, (B+1)//2)
        if B % 2 == 1:
            return parent
        else:
            return 1^parent

if __name__ == '__main__':
    print(Solution().solve(A=3, B=1))
    print(Solution().solve(A=3, B=2))
    print(Solution().solve(A=3, B=3))
    print(Solution().solve(A=3, B=4))
'''
1# 0
2# 0 1
3# 0 1 1 0
4# 0 1 1 0 1 0 0 1
'''
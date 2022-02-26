class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l = len(bin(A)) - 2
        ans = 0
        for i in range(l, -1, -1):
            mask = 1 << i
            if A & mask and B > 0:
                ans = ans | mask
                B -= 1
            if B == 0:
                return ans
        for i in range(l):
            mask = 1 << i
            if A & mask == 0 and B > 0:
                ans = ans | mask
                B -= 1
            if B == 0:
                return ans
        while B > 0:
            ans = ans << 1
            ans = ans | 1
            B -= 1
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.solve(4, 6))
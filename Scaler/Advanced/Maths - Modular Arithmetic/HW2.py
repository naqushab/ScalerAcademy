import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 1000000007
        # calculate A^B! mod mod
        fact = self.factorial(B, mod)
        return self.pow(A, fact, mod)

    def factorial(self, B, mod):
        ans = B
        while B > 1:
            ans = (ans * (B - 1)) % (mod-1)
            B = B - 1
        return ans

    def pow(self, A, B, mod):
        if A == 0:
            return 0
        if B == 0:
            return 1
        if B == 1:
            return A % mod
        p = self.pow(A%mod, B//2, mod)
        if B%2 == 0:
            return (p% mod * p%mod) % mod
        else:
            return ((p% mod * p% mod) % mod * A%mod) % mod

if __name__ == "__main__":
    s = Solution()
    A = 2
    B = 27
    print(s.solve(A, B))
    A = 15790
    B = 172066
    print(s.solve(A, B)) # expected: 957271226

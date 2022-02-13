class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 1
        for i in range(len(A)):
            gcd = -1
            for j in range(0, len(A)):
                if j == i:
                    continue
                else:
                    if gcd == -1:
                        gcd = A[j]
                    else:
                        gcd = self.gcd(gcd, A[j])
            ans = max(ans, gcd)
        return ans

if __name__ == "__main__":
    s = Solution()
    A = [12, 15, 18]
    print(s.solve(A))
    A = [5, 15, 30]
    print(s.solve(A))
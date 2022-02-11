from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 10**9 + 7
        m = defaultdict(lambda:0)
        for n in A:
            m[n%B] += 1
        ans = 0
        non_zero = 0
        for k,v in m.items():
            if B-k == B or B-k == k:
                ans = ans%mod + (v*(v-1)//2)%mod
            else:
                if B-k in m:
                    non_zero = (non_zero % mod) + (m[k] * m[B-k])%mod
        ans = (ans % mod + (non_zero // 2) % mod) % mod
        return ans

if __name__ == "__main__":
    s = Solution()
    A = [ 1, 2, 3, 4, 5 ]
    B = 2
    print(s.solve(A, B))
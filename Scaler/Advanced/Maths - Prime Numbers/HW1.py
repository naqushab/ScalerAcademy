class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 1:
            return 0
        spf = [i for i in range(A+1)]
        for i in range(2, int(A**0.5)+2):
            for j in range(i, A+1, i):
                if spf[j] > i:
                    spf[j] = i
        ans = 0
        for n in range(2, A+1):
            original_num = n
            divisors = set()
            while n > 1 and n % spf[n] == 0:
                divisors.add(spf[n])
                n = n // spf[n]
            if len(divisors) == 2:
                ans += 1
        return ans
        
if __name__ == "__main__":
    s = Solution()
    A = 12
    print(s.solve(A))
    A = 100
    print(s.solve(A))
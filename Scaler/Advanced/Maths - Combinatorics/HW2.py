import collections

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        # find the lexicographic rank of the string
        mod = 1000003
        n = len(A)
        sortedA = sorted(A)
        c = collections.Counter(sortedA)
        fact = self.factorial(n, mod)
        res = 1
        for i in range(n):
            rank = 0
            for j in range(i+1, n):
                if A[i] > A[j]:
                    rank += 1
            num = fact[n-i-1]%mod
            den = 1
            for k in c:
                den *= fact[c[k]] % mod
            den = self.inverse_num(den, mod)
            res = (res + rank*num*den)%mod
            c[A[i]] -= 1
        return res

    def inverse_num(self, n, mod):
        return pow(n, mod-2, mod)

    def factorial(self, n, mod):
        fact = [1]
        for i in range(1, n+1):
            fact.append(fact[-1]*i%mod)
        return fact

if __name__ == "__main__":
    s = Solution()
    A = "aAAbG"
    print(s.findRank(A))
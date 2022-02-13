class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = max(A)
        fact = [2]*(n+1)
        fact[0] = 0
        fact[1] = 1
        for i in range(2, int(n**0.5)+1):
            for j in range(i*i, n+1, i):
                fact[j] += 2
            fact[i*i] -= 1
        ans = []
        for n in A:
            ans.append(fact[n])
        return ans
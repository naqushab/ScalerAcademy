import math

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # count the number of divisors of each element in A and return the list of counts
        return self.countDivisors(A)
    
    def seive(self, n):
        # get smallest prime factor of each element in n
        seive = [i for i in range(n)]
        i = 2
        while i*i < n:
            if seive[i] == i:
                for j in range(i*i, n, i):
                    seive[j] = i
            i += 1
        return seive

    def countDivisors(self, A):
        seive = self.seive(max(A)+1)
        ans = []
        for n in A:
            count = 1
            while n > 1:
                p = seive[n]
                val = 0
                while n % p == 0:
                    val += 1
                    n = n // p
                count = count * (val + 1)
            ans.append(count)
        return ans

if __name__ == "__main__":
    s = Solution()
    A = [ 289, 38, 392, 476, 462, 320, 383, 335, 244, 358, 133, 448, 291, 46, 490, 104, 493, 41, 83, 429, 82, 278, 142, 290, 391, 401, 487, 402, 206, 53, 376, 427, 483, 13, 227, 418, 126, 369, 380, 418, 53, 324, 52, 39, 337, 366, 447, 214, 390, 346, 113, 177, 373, 42, 135, 77, 378, 499, 4, 347 ]
    print(s.solve(A))
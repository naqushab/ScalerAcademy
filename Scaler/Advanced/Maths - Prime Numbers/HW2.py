class Solution:
	# @param A : integer
	# @return a list of integers
    def primesum(self, A):
        primes = [True]*(A+1)
        primes[0] = False
        primes[1] = False
        for i in range(2, int(A**0.5)+1):
            for j in range(i*i, A, i):
                primes[j] = False
        for i in range (2, (A//2)+1):
            if primes[i] and primes[A-i]:
                return [i, A-i]

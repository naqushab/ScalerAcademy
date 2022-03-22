class Solution:
	# @param A : integer
	# @return an integer
    def colorful(self, A):
        digits = []
        while A>0:
            d, A = A%10, A//10
            digits.insert(0, d)
        prod = set()
        n = len(digits)
        for i in range(n):
            p = 1
            for j in range(i, n):
                p *= digits[j]
                if p in prod:
                    return 0
                prod.add(p)
        return 1
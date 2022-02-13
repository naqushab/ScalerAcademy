class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    def cpFact(self, A, B):
        def gcd_calc(a, b):
            if b == 0:
                return a
            else:
                return gcd_calc(b, a % b)
        ans = A
        gcd = gcd_calc(ans, B)
        while gcd != 1:
            A = A//gcd
            gcd = gcd_calc(A, B)
        return A
            

if __name__ == "__main__":
    s = Solution()
    A = 30
    B = 12
    print(s.cpFact(A, B))
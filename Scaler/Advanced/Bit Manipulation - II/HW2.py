class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    def divide(self, A, B):
        sign = -1 if int(A < 0) ^ int(B < 0) else 1
        A = abs(A)
        B = abs(B)
        q = 0
        total_sum = 0
        for i in range(31, -1, -1):
            if total_sum + (B<<i) <= A:
                total_sum += B << i
                q = q | 1 << i
        q = q * sign
        return q if -2**31 <= q <= 2**31 -1 else 2**31 -1

if __name__ == '__main__':
    s = Solution()
    print(s.divide(5, 2))
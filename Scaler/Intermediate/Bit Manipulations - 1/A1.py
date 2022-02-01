class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def addBinary(self, A, B):
        a = len(A) -1
        b = len(B) -1
        carry = 0
        ans = ""
        while a >=0 or b>= 0 or carry:
            if a >= 0:
                d1 = int(A[a])
            else:
                d1 = 0
            if b >= 0:
                d2 = int(B[b])
            else:
                d2 = 0
            sum_d = d1 + d2 + carry
            d = sum_d % 2
            carry = sum_d // 2
            a -= 1
            b -= 1
            ans += str(d)
        return ans[::-1]
class Solution:
	# @param A : integer
	# @return a strings
    def convertToTitle(self, A):
        # convert excel column to alphabet
        # A = 1, B = 2, C = 3, ..., Z = 26, AA = 27, AB = 28, ...
        ans = ''
        while A > 0:
            A -= 1
            ans = chr(ord('A') + (A % 26)) + ans
            A //= 26
        return ans

if __name__ == "__main__":
    s = Solution()
    A = 943566
    print(s.convertToTitle(A))
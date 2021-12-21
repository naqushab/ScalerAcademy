class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        ans = 0
        r = 1
        for i in range(len(A)-1, -1, -1):
            ans += ( (int(A[i]) % B) * (r % B) ) % B
            r = r*10 % B
        return ans%B
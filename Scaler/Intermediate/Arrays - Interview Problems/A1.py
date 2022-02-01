class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c1 = 0
        for n in A:
            if n == "1":
                c1+=1
        if c1 == len(A):
            return c1
        ans = 0
        for i in range(len(A)):
            if A[i] == "0":
                j = i-1
                l = 0
                while j >=0 and A[j] == "1":
                    l += 1
                    j -= 1
                j = i+1
                r = 0
                while j<len(A) and A[j] == "1":
                    r += 1
                    j += 1
                ans = max(ans, l+r)
        return ans+1 if ans<c1 else ans
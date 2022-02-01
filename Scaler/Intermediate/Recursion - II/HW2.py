import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = []

        def recur():
            if len(ans) == 1<<A:
                return
            num = len(ans)
            num = num ^ (num >> 1)
            ans.append(num)
            recur()

        recur()
        return ans
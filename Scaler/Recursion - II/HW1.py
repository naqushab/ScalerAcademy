class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = [["0"]]
        def recur():
            if len(ans) > A:
                return
            tmp = []
            for ch in ans[-1]:
                if ch == "0":
                    tmp.append("01")
                if ch == "1":
                    tmp.append("10")
            ans.append(''.join(tmp))
            recur()
        recur()
        return ans[A][B-1]
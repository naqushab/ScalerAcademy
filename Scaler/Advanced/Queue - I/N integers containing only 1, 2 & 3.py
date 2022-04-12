import collections
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        ans = []
        q = collections.deque()
        q.append(1)
        q.append(2)
        q.append(3)
        while q:
            d = q.popleft()
            q.append(d*10+1)
            q.append(d*10+2)
            q.append(d*10+3)
            if len(ans) != A:
                ans.append(d)
            else:
                return ans
                
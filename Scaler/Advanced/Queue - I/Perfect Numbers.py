import collections
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        q = collections.deque()
        q.append('11')
        q.append('22')
        count = 0
        while q:
            d = q.popleft()
            count += 1
            if count == A:
                return d
            l = len(d)
            q.append(d[:l//2] + '11' + d[l//2:])
            q.append(d[:l//2] + '22' + d[l//2:])

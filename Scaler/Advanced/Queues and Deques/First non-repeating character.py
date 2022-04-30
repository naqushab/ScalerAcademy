import collections

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = collections.deque()
        freq = collections.defaultdict(lambda : 0)
        ans = ''
        for ch in A:
            q.append(ch)
            freq[ch] += 1
            b_ch = ''
            while q:
                n = q[0]
                if freq[n] == 1:
                    b_ch = n
                    break
                else:
                    q.popleft()
            if b_ch != '':
                ans += b_ch
            else:
                ans += '#'
        return ans
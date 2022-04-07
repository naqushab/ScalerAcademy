import collections

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        st = collections.deque()
        for ch in A:
            if len(st) == 0:
                st.append(ch)
            elif st[-1] == ch:
                st.pop()
            else:
                st.append(ch)
        ans = ''
        while st:
            ans += st.pop()
        return ans[::-1]
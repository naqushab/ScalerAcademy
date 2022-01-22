from collections import deque

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        st = deque()
        m = {'}': '{', ']': '[', ')': '('}
        for s in A:
            if s in m.values():
                st.append(s)
            elif s in m.keys():
                if not st:
                    return 0
                if st[-1] != m[s]:
                    return 0
                else:
                    st.pop()
        return 1 if len(st) == 0 else 0
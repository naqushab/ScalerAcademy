from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        m = { ')': '(', ']': '[', '}': '{' }
        for ch in s:
            if ch in m.values():
                st.append(ch)
            if ch in m.keys():
                if not st:
                    return False
                if st[-1] == m[ch]:
                    st.pop()
                else:
                    return False
        return len(st) == 0
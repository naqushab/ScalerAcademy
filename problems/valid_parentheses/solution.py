from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        st = deque()
        for ch in s:
            if ch in m.values():
                st.append(ch)
            elif ch in m:
                if len(st) == 0:
                    return False
                elif st[-1] != m[ch]:
                    return False
                elif st[-1] == m[ch]:
                    st.pop()
        return len(st) == 0
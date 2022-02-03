from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        st = deque()
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '[':
                if num > 0:
                    st.append(str(num))
                    num = 0
                else:
                    st.append(str(1))
            elif ch.isalpha():
                st.append(ch)
            elif ch == ']':
                temp = ''
                while len(st) > 0:
                    if st[-1].isalpha():
                        temp += st.pop()
                    elif st[-1].isdigit():
                        st.append(temp*int(st.pop()))
                        break
        ans = ''
        while st:
            ans += st.pop()
        return ans[::-1]
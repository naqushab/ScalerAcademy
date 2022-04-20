from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        st = deque()
        ans, last_num, last_op = 0, 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                last_num = last_num*10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s)-1:
                if last_op == '+':
                    st.append(last_num)
                elif last_op == '-':
                    st.append(-last_num)
                elif last_op == '*':
                    st.append(st.pop() * last_num)
                elif last_op == '/':
                    st.append(int(st.pop() / last_num))
                last_op = s[i]
                last_num = 0
        while st:
            ans += st.pop()
        return ans
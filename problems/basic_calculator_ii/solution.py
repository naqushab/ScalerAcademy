from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        st = deque()
        last_num = 0
        last_op = '+'
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
                    temp = st.pop() / last_num
                    if temp < 0 and temp//1.0 != temp:
                        temp = math.floor(temp) + 1
                    else:
                        temp = math.floor(temp)
                    st.append(temp)
                last_op = s[i]
                last_num = 0
        
        ans = 0
        while st:
            ans += st.pop()
        return ans
                
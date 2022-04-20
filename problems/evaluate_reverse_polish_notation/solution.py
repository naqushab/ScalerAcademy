class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for n in tokens:
            if n not in ['+', '-', '*','/']:
                st.append(int(n))
            else:
                b, a = st.pop(), st.pop()
                c = 0
                if n == '+':
                    c = a+b
                elif n == '-':
                    c = a - b
                elif n == '*':
                    c = a*b
                elif n == '/':
                    c = a/b
                    c = int(c)
                st.append(c)
        return st[-1]
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        st = []
        ans = ''
        op = {'(': 4, ')': 4, '^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
        for ch in A:
            if ch not in op.keys():
                ans += ch
            elif ch == '(':
                st.append(ch)
            elif ch == ')':
                s = ''
                while st[-1] != '(':
                    s += st.pop()
                else:
                    st.pop()
                ans += s
            else:
                s = ''
                while st and st[-1] != '(' and op[ch] <= op[st[-1]]:
                    s += st.pop()
                else:
                    st.append(ch)
                ans += s
        while st:
            ans += st.pop()
        return ans
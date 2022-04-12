class Solution:
	# @param A : list of strings
	# @return an integer
    def evalRPN(self, A):
        st = []
        op = {'*', '/', '+', '-'}
        for ch in A:
            if ch in op:
                b = st.pop()
                a = st.pop()
                if ch == '*':
                    st.append(a*b)
                elif ch == '/':
                    st.append(a//b)
                elif ch == '+':
                    st.append(a+b)
                elif ch == '-':
                    st.append(a-b)
            else:
                st.append(int(ch))
        return st[-1]
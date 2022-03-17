class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = collections.deque()
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append('(')
            else:
                if st[-1] == '(':
                    st.pop()
                    st.append(1)
                else:
                    val = 0
                    while st[-1] != '(':
                        val += st.pop()
                    st.pop()
                    st.append(2*val)
        while st:
            score += st.pop()
        return score
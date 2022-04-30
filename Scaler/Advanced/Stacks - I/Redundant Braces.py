class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        # check if braces are redundant
        # if not, return 0
        # if yes, return 1
        st = []
        for ch in A:
            if ch == '(':
                st.append(ch)
            elif ch == ')':
                if len(st) == 0:
                    return 0
                else:
                    st.pop()
        return int(len(st) == 0)
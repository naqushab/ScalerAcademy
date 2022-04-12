class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        st = []
        for ch in A:
            if not st:
                st.append(ch)
                continue
            if st[-1] != ch:
                st.append(ch)
            else:
                st.pop()
        ans = ''
        while st:
            ans += st.pop()
        return ans[::-1]

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        st = [B]
        for n in C:
            if n != 0:
                st.append(n)
            else:
                st.pop()
        return st[-1]
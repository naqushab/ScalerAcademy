class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        st = []
        ans = []
        for n in A[::-1]:
            while st and st[-1] <= n:
                st.pop()
            if st:
                ans.insert(0, st[-1])
            else:
                ans.insert(0, -1)
            st.append(n)
        return ans
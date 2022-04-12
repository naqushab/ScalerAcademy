class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        st = []
        ans = []
        for n in A:
            while st and st[-1] >= n:
                st.pop()
            if st:
                ans.append(st[-1])
            else:
                ans.append(-1)
            st.append(n)
        return ans
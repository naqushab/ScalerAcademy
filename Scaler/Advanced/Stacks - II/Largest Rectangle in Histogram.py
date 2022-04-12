class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        n = len(A)
        nsl, nsr = [0]*n, [0]*n
        
        st = []
        for i in range(n):
            while st and A[st[-1]] >= A[i]:
                st.pop()
            if st:
                nsl[i] = st[-1] + 1
            else:
                nsl[i] = 0
            st.append(i)
        st = []
        for i in range(n-1, -1, -1):
            while st and A[st[-1]] >= A[i]:
                st.pop()
            if st:
                nsr[i] = st[-1] - 1
            else:
                nsr[i] = n - 1
            st.append(i)
        
        area = 0
        for i in range(n):
            area = max(area, (nsr[i]-nsl[i]+1)*A[i])
        
        return area
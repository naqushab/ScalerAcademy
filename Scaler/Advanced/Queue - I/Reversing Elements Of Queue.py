import collections

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        q = collections.deque()
        st = collections.deque()
        ans = collections.deque()
        for i in range(len(A)):
            q.append(A[i])
        for _ in range(B):
            st.append(q.popleft())
        while st:
            ans.append(st.pop())
        while q:
            ans.append(q.popleft())
        return ans
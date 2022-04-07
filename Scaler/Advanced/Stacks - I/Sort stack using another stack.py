import collections

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = self.merge_sort(A)
        return ans[::-1]

    def merge_sort(self, st):
        # base case
        if len(st) <= 1:
            return st
        st1, st2 = st, []
        n = len(st1)//2
        for _ in range(n):
            val = st1.pop()
            st2.append(val)
        st1 = self.merge_sort(st1)
        st2 = self.merge_sort(st2)
        return self.merge(st1, st2)

    def merge(self, s1, s2):
        s3 = []
        while s1 and s2:
            if s1[-1] <= s2[-1]:
                s3.append(s1[-1])
                s1.pop()
            else:
                s3.append(s2[-1])
                s2.pop()
        while s1:
            s3.append(s1[-1])
            s1.pop()
        while s2:
            s3.append(s2[-1])
            s2.pop()
        return s3[::-1]
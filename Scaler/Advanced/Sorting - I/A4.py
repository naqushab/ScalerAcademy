class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_elem = max(A)
        count_max = A.count(max_elem)
        if count_max == len(A):
            return 0
        else:
            for i in range(len(A)):
                if A[i] == max_elem:
                    A[i] = -1
            sec_max_elem = max(A)
            return sec_max_elem
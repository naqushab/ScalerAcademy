class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a_min_index = -1
        a_max_index = -1
        len_min = len(A) + 1
        a_min, a_max = min(A), max(A)
        for i, n in enumerate(A):
            if n == a_max:
                a_max_index = i
                if a_min_index != -1:
                    len_min = min(len_min, a_max_index - a_min_index+1)
            if n == a_min:
                a_min_index = i
                if a_max_index != -1:
                    len_min = min(len_min, a_min_index-a_max_index+1)
        return len_min

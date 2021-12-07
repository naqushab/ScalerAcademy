class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        window_start = 0
        global_max = 0
        local_max = 0
        for window_end in range(A):
            local_max += C[window_end]
            while local_max > B:
                local_max -= C[window_start]
                window_start += 1
            else:
                global_max = max(global_max, local_max)
        return global_max
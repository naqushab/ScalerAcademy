class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        window_start = 0
        current_sum = 0
        for window_end in range(len(A)):
            current_sum += A[window_end]
            while current_sum > B:
                current_sum -= A[window_start]
                window_start += 1
            if current_sum == B:
                return A[window_start:window_end+1]
        return [-1]
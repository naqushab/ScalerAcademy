class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B > len(A):
            return 0
        window_start = 0
        min_sum = float('+inf')
        local_min_sum = 0
        index_ans = 0
        for window_end in range(len(A)):
            local_min_sum += A[window_end]
            if window_end - window_start + 1 == B:
                if local_min_sum < min_sum:
                    min_sum = local_min_sum
                    index_ans = window_start
                local_min_sum -= A[window_start]
                window_start += 1
        print(index_ans)
        return index_ans

if __name__ == "__main__":
    s = Solution()
    s.solve(A=[0, 7, 8, 1, 10], B = 1)
    s.solve(A=[7, 8, 1, 10], B = 1)
    s.solve(A=[ 15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18 ], B=6)

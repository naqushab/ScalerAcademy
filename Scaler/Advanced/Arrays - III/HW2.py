class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        less_count = 0
        for n in A:
            if n <= B:
                less_count += 1
        
        window_start = 0
        n = len(A)
        max_occurences = 0
        cur_occurences = 0
        for window_end in range(n):
            if A[window_end] <= B:
                cur_occurences += 1
            if window_end - window_start + 1 == less_count:
                max_occurences = max(max_occurences, cur_occurences)
                if A[window_start] <= B:
                    cur_occurences -= 1
                window_start += 1
        return less_count-max_occurences

if __name__ == "__main__":
    s = Solution()
    A = [ 1, 12, 10, 3, 14, 10, 5 ]
    B = 8
    print(s.solve(A, B))
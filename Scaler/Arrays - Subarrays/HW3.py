class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        k = 2*B + 1
        window_start = 0
        window_end = 0
        index_array = []
        alternating_len = 0
        if k == 1:
            for i in range(len(A)):
                index_array.append(i)
            return index_array
        
        while window_end < len(A)-1:
            if A[window_end] ^ A[window_end+1] == 1:
                alternating_len = window_end+1-window_start+1
            else:
                while alternating_len >= k:
                    index_array.append(window_start+B)
                    window_start += 1
                    alternating_len -= 1
                window_start = window_end + 1
            window_end += 1
        while alternating_len >= k:
            index_array.append(window_start+B)
            window_start += 1
            alternating_len -= 1
        return index_array

if __name__ == "__main__":
    s = Solution()
    s.solve(A=[1, 0, 1, 0, 1], B = 1)
    s.solve(A=[1, 0, 1, 0, 1, 1, 0, 1], B = 1)
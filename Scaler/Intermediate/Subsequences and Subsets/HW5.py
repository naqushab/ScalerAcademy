class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        odd_start = 0
        even_start = 0
        n = len(A)

        # if starts with odd
        pos = 0
        while pos < n and A[pos] % 2 == 0:
            pos += 1
        odd_start = self.get_remaining_length(A, pos, 1, True)

        pos = 0
        while pos < n and A[pos]%2 == 1:
            pos += 1
        even_start = self.get_remaining_length(A, pos, 1, False)
        return max(even_start, odd_start)
        
    def get_remaining_length(self, A, pos, max_l, even_reqd):
        for i in range(pos+1, len(A)):
            if even_reqd:
                if A[i] % 2 == 0:
                    max_l += 1
                    even_reqd = False
            else:
                if A[i] %2 != 0:
                    max_l += 1
                    even_reqd = True
        return max_l 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        x = 0
        for n in A:
            x ^= n
        
        m = (x & x-1) ^ x

        a, b = 0, 0

        for n in A:
            if n & m:
                a ^= n
            else:
                b ^= n
        
        return [a, b] if a <= b else [b, a]
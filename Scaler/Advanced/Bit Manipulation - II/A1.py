class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        x = 0
        for n in A:
            x ^= n

        mask = (x & x-1) ^ x # 1110 -> 1110 & 1101 -> 1100 ^ 1110 -> 0010

        a, b = 0, 0
        for n in A:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        return sorted([a, b])

if __name__ == "__main__":
    s = Solution()
    A = [ 186, 256, 102, 377, 186, 377 ]
    print(s.solve(A))
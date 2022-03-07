class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        return sorted(A, key=lambda x: x[0]*x[0] + x[1]*x[1])[:B]

if __name__ == '__main__':
    s = Solution()
    A = [ 
       [1, 3],
       [-2, 2] 
     ]
    B = 1
    print(s.solve(A, B))
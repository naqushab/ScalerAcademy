class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        n = len(A) # row
        m = len(A[0]) # col
        mod = (10**9) + 7
        PS = [[0 for _ in range(m)] for _ in range(n)]
        ans = []
        for i in range(n):
            for j in range(m):
                if j == 0:
                    PS[i][j] = A[i][j] % mod
                else:
                    PS[i][j] = (PS[i][j-1] % mod + A[i][j] % mod) % mod
        for i in range(m):
            for j in range(n):
                if j == 0:
                    pass
                else:
                    PS[j][i] = (PS[j-1][i] % mod + PS[j][i] % mod) % mod
        q = len(B)
        for _ in range(q):
            i, j = B[_]-1, C[_]-1
            p, q = D[_]-1, E[_]-1
            if i == 0 and j == 0:
                ans.append((PS[p][q]) % mod)
            elif i == 0:
                ans.append((PS[p][q] - PS[p][j-1]) % mod)
            elif j == 0:
                ans.append((PS[p][q] - PS[i-1][q]) % mod)
            else:
                ans.append((PS[p][q] % mod - PS[i-1][q] % mod - PS[p][j-1] % mod + PS[i-1][j-1] % mod) % mod)
        return ans
        
if __name__ == "__main__":
    s = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [1, 2]
    C = [1, 2]
    D = [2, 3]
    E = [2, 3]
    print(s.solve(A, B, C, D, E))
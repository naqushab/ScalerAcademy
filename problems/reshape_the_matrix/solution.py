class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(mat[i][j])
        ans = []
        ptr = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(arr[ptr])
                ptr += 1
            ans.append(row)
        
        return ans
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r = n = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            s = set()
            for j in range(c):
                s.add(matrix[i][j])
            if len(s) != n:
                return False
        for i in range(r):
            s = set()
            for j in range(c):
                s.add(matrix[j][i])
            if len(s) != n:
                return False
        return True
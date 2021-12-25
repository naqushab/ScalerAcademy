class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            num = matrix[mid//n][mid%n]
            if num == target:
                return True
            elif num > target:
                r = mid -1
            else:
                l = mid +1
        return False
            
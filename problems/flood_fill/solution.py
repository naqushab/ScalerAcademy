class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        clr = image[sr][sc]
        if clr == newColor:
            return image
        
        def dfs(image, i, j):
            if image[i][j] == clr:
                image[i][j] = newColor
                if 0<=i-1<r and 0<=j<c:
                    dfs(image, i-1, j)
                if 0<=i+1<r and 0<=j<c:
                    dfs(image, i+1, j)
                if 0<=i<r and 0<=j-1<c:
                    dfs(image, i, j-1)
                if 0<=i<r and 0<=j+1<c:
                    dfs(image, i, j+1)
        
        dfs(image, sr, sc)
        return image
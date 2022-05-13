class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        if sr >= r or sr < 0 or sc >= c or sc < 0 or image[sr][sc] == newColor:
            return image
        
        def flood_fill(orig_color, new_color, sr, sc):
            if sr >= r or sr < 0 or sc >= c or sc < 0:
                return
            if image[sr][sc] == orig_color:
                image[sr][sc] = new_color
            else:
                return
            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_sr, new_sc = sr + x, sc + y
                flood_fill(orig_color, new_color, new_sr, new_sc)
        
        orig_color = image[sr][sc]
        flood_fill(orig_color, newColor, sr, sc)
        return image
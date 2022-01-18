class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = 0
        c = 0
        al = len(flowerbed)
        if al == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0
            
        for i in range(al):
            if flowerbed[i] == 0:
                if i == 0 and i < al -1:
                    if flowerbed[i+1] != 1:
                        c += 1
                        flowerbed[i] = 1
                elif i > 0 and i < al-1:
                    if flowerbed[i+1] != 1 and flowerbed[i-1] != 1:
                        c += 1
                        flowerbed[i] = 1
                elif i > 0 and i == al-1:
                    if flowerbed[i-1] != 1:
                        c += 1
                        flowerbed[i] = 1
        return n<=c
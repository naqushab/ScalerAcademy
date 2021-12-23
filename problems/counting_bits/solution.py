class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            c1 = 0
            while i > 0:
                c1 += 1
                i = i&i-1
            ans.append(c1)
        return ans
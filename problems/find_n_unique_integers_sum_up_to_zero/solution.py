class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        i = 1
        while n >= 2:
            ans.extend([-i, i])
            i += 1
            n -= 2
        if n%2 == 1:
            ans.append(0)
        return ans
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for n in encoded:
            ans.append(ans[-1]^n)
        return ans
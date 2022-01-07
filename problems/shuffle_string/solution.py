class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None]*len(s)
        for i, n in enumerate(indices):
            ans[n] = s[i]
        return ''.join(ans)
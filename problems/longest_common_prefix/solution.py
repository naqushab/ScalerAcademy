class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i > len(s) - 1:
                    return strs[0][:i]
                elif s[i] != c:
                    return strs[0][:i]
        return strs[0]
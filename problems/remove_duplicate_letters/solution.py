class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        ans = []
        seen = [False]*26
        for i in range(len(s)):
            c[s[i]] -= 1
            if seen[ord(s[i]) - ord('a')]:
                continue
            while len(ans) > 0 and ans[-1] > s[i] and c[ans[-1]] > 0:
                ch = ans.pop()
                seen[ord(ch) - ord('a')] = False
            ans.append(s[i])
            seen[ord(s[i]) - ord('a')] = True
        return ''.join(ans)
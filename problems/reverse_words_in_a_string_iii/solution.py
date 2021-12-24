class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        ans = []
        for w in s_list:
            ans.append(w[::-1])
        return ' '.join(ans)
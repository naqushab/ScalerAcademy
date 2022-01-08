class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for w in title.split():
            if len(w) <= 2:
                ans.append(w.lower())
            else:
                ans.append(w.title())
        return ' '.join(ans)
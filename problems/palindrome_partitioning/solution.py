class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def pal(st):
            return st == st[::-1]

        def backtrack(start, tmp):
            if start >= len(s):
                ans.append(tmp[:])
                return
            else:
                for i in range(start, len(s)):
                    if pal(s[start:i+1]):
                        tmp.append(s[start:i+1])
                        backtrack(i + 1, tmp)
                        tmp.pop()
        backtrack(0, [])
        return ans
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        l, r = 0, len(s)-1
        while l<=r and s[l] == ' ':
            l += 1
        while l<=r and s[r] == ' ':
            r -= 1
        w, d = [], deque()
        while l<=r:
            if s[l] != ' ':
                w.append(s[l])
            if s[l] == ' ' and w:
                d.appendleft(''.join(w))
                w = []
            l += 1
        if w:
            d.appendleft(''.join(w))
        return ' '.join(d)
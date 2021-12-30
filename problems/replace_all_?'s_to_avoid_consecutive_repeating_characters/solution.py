import string

class Solution:
    def modifyString(self, s: str) -> str:
        def get_char(l_char=None, r_char=None):
            if l_char and r_char:
                for ch in string.ascii_lowercase:
                    if ch != l_char and ch!= r_char:
                        return ch
            elif l_char:
                for ch in string.ascii_lowercase:
                    if ch != l_char:
                        return ch
            elif r_char:
                for ch in string.ascii_lowercase:
                    if ch != r_char:
                        return ch
        
        if not s:
            return s
        if s == '?':
            return 'n'
        ans = ['a'] * len(s)
        for i, c in enumerate(s):
            if c == '?' and i == 0:
                ans[i] = get_char(r_char=s[i+1])
            elif c == '?' and 0 < i < len(s)-1:
                ans[i] = get_char(l_char=ans[i-1], r_char=s[i+1])
            elif c == '?' and i == len(s) -1:
                ans[i] = get_char(l_char=ans[i-1])
            else:
                ans[i] = s[i]
        
        return ''.join(ans)
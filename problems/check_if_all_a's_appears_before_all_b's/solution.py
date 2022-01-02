class Solution:
    def checkString(self, s: str) -> bool:
        b_come = False
        a_count = 0
        for i, c in enumerate(s):
            if c == 'b':
                b_come = True
                break
            elif c == 'a':
                a_count += 1
        if b_come:
            if 'a' in s[i+1:]:
                return False
            else:
                return True
        else:
            return True
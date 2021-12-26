from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = OrderedDict()
        for i, c in enumerate(s):
            if c not in m:
                m[c] = (0, i)
            m[c] = (m[c][0]+1, i)
        for v in m.values():
            f, index = v
            if f == 1:
                return index
        return -1
from collections import Counter

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c = Counter(A)
        if len(A) % 2 == 0:
            for k, v in c.items():
                if v%2 != 0:
                    return 0
            return 1
        else:
            one_allowed = 1
            for k, v in c.items():
                if v%2 == 0:
                    continue
                if v%2 != 0 and one_allowed == 1:
                    one_allowed -= 1
                else:
                    return 0
            return 1
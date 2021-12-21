class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        a, b, c = 0, 0, 0
        if A >= B:
            if A >= C:
                a = A
                if B >= C:
                    b = B
                    c = C
                else:
                    b = C
                    c = B
            else:
                a = C
                if B >= A:
                    b = B
                    c = A
                else:
                    b = A
                    c = B
        else:
            if B>=C:
                a = B
                if A>=C:
                    b = A
                    c = C
                else:
                    b = C
                    c = A
            else:
                a = C
                if A>=B:
                    b = A
                    c = B
                else:
                    b = B
                    c = A
        return c*10000+b*100+a
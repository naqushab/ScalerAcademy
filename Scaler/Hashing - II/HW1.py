class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if len(A) <= 1:
            return 1
        m = {}
        for i, c in enumerate(B):
            m[c] = i
        
        for i in range(len(A)-1):
            s1, s2 = A[i], A[i+1]
            l1, l2 = len(s1), len(s2)
            c = 0
            while c < min(l1, l2):
                if m[s1[c]] > m[s2[c]]:
                    return 0
                if m[s1[c]] < m[s2[c]]:
                    break
                c += 1
            if c == min(l1, l2) and l1 > l2:
                return 0
        return 1
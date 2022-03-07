class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.merge_sort(A)
    
    def merge_sort(self, A):
        n = len(A)
        if n == 1:
            return A
        m = n//2
        l = self.merge_sort(A[:m])
        r = self.merge_sort(A[m:])
        s = self.merge(l, r)
        return s
    
    def merge(self, l, r):
        t = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                t.append(l[i])
                i += 1
            else:
                t.append(r[j])
                j += 1
        while i < len(l):
            t.append(l[i])
            i += 1
        while j < len(r):
            t.append(r[j])
            j += 1
        return t

if __name__ == '__main__':
    s = Solution()
    A = [3, 2, 1]
    print(s.solve(A))
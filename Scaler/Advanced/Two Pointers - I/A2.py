from collections import Counter

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.two_pointers(A, B)
    
    def two_pointers(self, A, B):
        n = len(A)
        i, j = 0, 1
        A.sort()
        count = 0
        while j < n:
            if j == i:
                j += 1
                continue
            x, y = A[i], A[j]
            if y - x == B:
                count += 1
                while j < n and A[j] == y:
                    j += 1
                while i < n and A[i] == x:
                    i += 1
            elif y - x > B:
                i += 1
            else:
                j += 1
        return count

    def hashing(self, A, B):
        n = len(A)
        pairs = set()
        m = Counter(A)
        for i in range(n):
            if B == 0:
                if m[A[i]] > 1:
                    pairs.add((A[i], A[i]))
            else:
                if B + A[i] in m:
                    pairs.add((min(A[i], B+A[i]), max(A[i], B+A[i])))
        return len(pairs)

if __name__ == '__main__':
    print(Solution().solve([ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ], 3))
    print(Solution().solve([1, 5, 3, 4, 2], 3))
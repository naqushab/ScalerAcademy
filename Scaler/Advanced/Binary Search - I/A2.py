class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        l = self.search_lower_end(A, B)
        r = self.search_higher_end(A, B)
        if A[l] == B:
            return [l, r]
        else:
            return [-1, -1]
    
    def search_lower_end(self, A, B):
        pos, l, r = 0, 0, len(A)-1
        while l <= r:
            mid = (l+r)//2
            if A[mid] == B:
                pos = mid
                r = mid - 1
            elif A[mid] < B:
                l = mid + 1
            else:
                r = mid - 1
        return pos

    def search_higher_end(self, A, B):
        pos, l, r = 0, 0, len(A)-1
        while l <= r:
            mid = (l+r)//2
            if A[mid] == B:
                pos = mid
                l = mid + 1
            elif A[mid] < B:
                l = mid + 1
            else:
                r = mid - 1
        return pos
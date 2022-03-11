class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        left, right = 0, len(A) -1
        while left <= right:
            mid = (left + right)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1
        return left
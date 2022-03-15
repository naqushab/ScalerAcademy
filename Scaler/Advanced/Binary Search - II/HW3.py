class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        pivot = self.get_bitonic_pivot(A)
        left = self.binary_search_increasing(A, B, 0, pivot)
        if left == -1:
            return self.binary_search_decreasing(A, B, pivot + 1, len(A) - 1)
        return left
    
    def binary_search_increasing(self, A, B, left, right):
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def binary_search_decreasing(self, A, B, left, right):
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get_bitonic_pivot(self, A):
        left = 0
        right = len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    s = Solution()
    A = [ 3, 5, 7, 101, 18, 15, 10 ]
    B = 18
    print(s.solve(A, B)) # 135
    print(s.solve([ 1, 2, 3, 12, 60, 50, 49, 42, 45, 47, 38, 20, 9 ], 45))

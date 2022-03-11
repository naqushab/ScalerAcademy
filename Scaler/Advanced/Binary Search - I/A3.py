class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l, r = 0, len(A)-1
        if len(A) == 1:
            return A[0]
        while l <= r:
            mid = (l+r)//2
            if mid > 0 and mid < len(A)-1:
                if A[mid-1] < A[mid] > A[mid+1]:
                    return A[mid]
                elif A[mid-1] >= A[mid] and A[mid] >= A[mid+1]:
                    r = mid - 1
                elif A[mid+1] >= A[mid] and A[mid] > A[mid-1]:
                    l = mid + 1
            elif mid == 0:
                if A[mid] >= A[mid+1]:
                    return A[mid]
                else:
                    l = mid + 1
            elif mid == len(A) -1:
                if A[mid] >= A[mid-1]:
                    return A[mid]
                else:
                    r = mid - 1

if __name__ == '__main__':
    print(Solution().solve([1,100, 100]))
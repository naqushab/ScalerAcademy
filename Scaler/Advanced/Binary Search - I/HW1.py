class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l, r = 0, len(A) -1
        while l <= r:
            mid = (l+r)//2
            if mid > 0 and mid < len(A)-1:
                if A[mid-1] != A[mid] and A[mid] != A[mid+1]:
                    return A[mid]
                elif A[mid] == A[mid+1]:
                    if mid % 2 == 0: # if mid is even then only pairs can happen before it
                        l = mid + 2
                    else:
                        r = mid - 1
                elif A[mid-1] == A[mid]:
                    if mid % 2 == 0:
                        r = mid - 2
                    else:
                        l = mid + 1
            elif mid == 0:
                if A[mid] != A[mid+1]:
                    return A[mid]
                else:
                    l = mid + 2
            elif mid == len(A) -1:
                if A[mid] != A[mid-1]:
                    return A[mid]
                else:
                    r = mid - 2
        return -1

if __name__ == '__main__':
    print(Solution().solve([ 106, 106, 248, 248, 286, 286, 344, 357, 357 ]))
    print(Solution().solve([ 1, 1, 2, 2, 3 ]))
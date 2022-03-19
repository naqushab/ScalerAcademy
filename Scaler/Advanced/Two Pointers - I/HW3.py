class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        n = len(A)
        low, med, high = 0, 0, n-1
        while med <= high:
            if A[med] == 0:
                A[low], A[med] = A[med], A[low]
                low += 1
                med += 1
            elif A[med] == 2:
                A[med], A[high] = A[high], A[med]
                high -= 1
            else:
                med += 1
        return A

if __name__ == '__main__':
    print(Solution().sortColors([2,0,2,1,1,0]))
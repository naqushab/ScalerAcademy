class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        min_incorrect = float('inf')
        max_incorrect = float('-inf')
        n = len(A)
        for i in range(n):
            if i == n-1:
                return [-1]
            if A[i] <= A[i+1]:
                continue
            else:
                break
        
        for i in range(n-1):
            if A[i] <= A[i+1]:
                continue
            else:
                min_incorrect = min(A[i+1], min_incorrect)
        for i in range(n-1, 0, -1):
            if A[i-1] <= A[i]:
                continue
            else:
                max_incorrect = max(A[i-1], max_incorrect)
        
        min_index, max_index = -1, -1
        for i in range(n):
            if A[i] <= min_incorrect:
                continue
            else:
                min_index = i
                break
        for i in range(n-1, -1, -1):
            if A[i] >= max_incorrect:
                continue
            else:
                max_index = i
                break
        return [min_index, max_index]

if __name__ == '__main__':
    s = Solution()
    print(s.subUnsort([1, 3, 2, 4, 5]))
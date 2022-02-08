class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        arr = []
        for i in range(n):
            arr.append((A[i], i))
        arr.sort()
        max_gap = 0
        min = arr[0][1]
        for i in range(n):
            if arr[i][1] - min > max_gap:
                max_gap = arr[i][1] - min
            min = min if min < arr[i][1] else arr[i][1] 
        return max_gap

if __name__ == "__main__":
    s = Solution()
    A = [3, 5, 4, 2]
    print(s.maximumGap(A))
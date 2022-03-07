class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.merge_sort(A, 0, len(A)-1) % (10**9 +7)
    
    def merge_sort(self, A, s, e):
        # return inversion count of array A
        if s >= e:
            return 0
        mid = (s + e) // 2
        left = self.merge_sort(A, s, mid) % (10**9 +7)
        right = self.merge_sort(A, mid+1, e) % (10**9 +7)
        return (left + right + self.merge(A, s, mid, e)) % (10**9 +7)

    def merge(self, A, left, mid, right):
        # merge two sorted arrays
        temp = []
        i, j = left, mid+1
        count = 0
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                temp.append(A[i])
                i += 1
            else:
                temp.append(A[j])
                j += 1
                count += mid - i + 1 # +1 because mid is inclusive, A[i] > A[j]
        while i <= mid:
            temp.append(A[i])
            i += 1
        while j <= right:
            temp.append(A[j])
            j += 1
        for i in range(left, right+1):
            A[i] = temp[i-left]
        return count % (10**9 +7)

if __name__ == '__main__':
    s = Solution()
    A =  [ 45, 10, 15, 25, 50 ]
    print(s.solve(A))
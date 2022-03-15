class Solution:
	# @param A : list of list of integers
	# @return an integer
    def findMedian(self, A):
        n = len(A)
        m = len(A[0])
        l, r = 0, n*m-1
        while l <= r:
            mid = (l+r)//2

if __name__ == '__main__':
    s = Solution()
    print(s.findMedian([[1, 3, 5],[2, 6, 9],[3, 6, 9]]))
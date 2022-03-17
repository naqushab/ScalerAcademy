class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def books(self, A, B):
        l, r = max(A), sum(A)
        ans = 0
        if len(A) < B:
            return -1
        while l <= r:
            k = (l+r)//2
            if self.check_if_reading_possible(A, B, k):
                ans = k
                r = k-1
            else:
                l = k+1
        return ans
    
    def check_if_reading_possible(self, A, B, k):
        pages = 0
        student_count = 1
        for i in range(len(A)):
            if pages + A[i] <= k:
                pages += A[i]
            elif student_count < B:
                student_count += 1
                pages = A[i]
            else:
                return False
        return True
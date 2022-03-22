class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        min_d, d = float('+inf'), float('+inf')
        for i in range(n-1, -1, -1):
            d, s = self.two_sum_diff(A, 0, i-1, B-A[i])
            if abs(d) < min_d:
                ans = s + A[i]
                min_d = abs(d)
        return ans

    def two_sum_diff(self, A, l, r, target):
        min_d, total = float('+inf'), 0
        while l < r:
            s = A[l] + A[r]
            if s == target:
                return target-s, s
            elif s > target:
                if abs(target - s) < min_d:
                    min_d = abs(target - s)
                    total = s
                r -= 1
            else:
                if abs(target - s) < min_d:
                    min_d = abs(target - s)
                    total = s
                l += 1
        return min_d, total

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ], -1))
    print(s.threeSumClosest([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ], -1))
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        n = len(A)
        ans = []
        for i in range(n):
            if i > 0 and A[i] == A[i-1]:
                continue
            triplets = self.find_two_sum(A, i+1, n-1, -A[i])
            if len(triplets) > 0:
                ans.extend(triplets)
        return ans

    def find_two_sum(self, A, l, r, target):
        triplets = []
        while l < r:
            if A[l] + A[r] == target:
                triplets.append([-target, A[l], A[r]])
                l += 1
                r -= 1
                while l < r and A[l] == A[l-1]:
                    l += 1
                while l < r and A[r] == A[r+1]:
                    r -= 1
            elif A[l] + A[r] < target:
                l += 1
            else:
                r -= 1
        return triplets

if __name__ == '__main__':
    print(Solution().threeSum([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]))
    print("[[-5, 0, 5], [-5, 1, 4], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-2, -1, 3], [-2, 1, 1], [-1, 0, 1], [0, 0, 0]")
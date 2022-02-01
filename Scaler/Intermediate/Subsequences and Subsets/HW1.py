class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self, A):
        A.sort()
        max_sum, min_sum = 0, 0
        for i in range(len(A)):
            max_sum += (A[i]* 1<<i) % (10**9+7)
        A.reverse()
        for i in range(len(A)):
            min_sum += (A[i]* 1<<i) % (10**9+7)
        return (max_sum-min_sum) % (10**9+7)

if __name__ == "__main__":
    s = Solution()
    print(s.solve(A=[3,7,9]))
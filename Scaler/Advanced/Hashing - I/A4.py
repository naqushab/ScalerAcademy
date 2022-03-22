class Solution:
	# @param A : list of integers
	# @return a list of integers
    def lszero(self, A):
        max_dist, dist = 0, 0
        running_sum = 0
        index_map = {0:-1}
        ans = []
        for i in range(len(A)):
            running_sum += A[i]
            if running_sum not in index_map:
                index_map[running_sum] = i
            else:
                dist = i - index_map[running_sum] + 1
                if dist > max_dist:
                    max_dist = dist
                    ans = A[index_map[running_sum]+1:i+1]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lszero([ 1, 2, -2, 4, -4 ]))
    print(s.lszero([ 1, 2, -3, 4, -4 ]))
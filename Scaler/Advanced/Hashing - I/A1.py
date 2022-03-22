class Solution:
	# @param A : tuple of integers
	# @return an integer
    def longestConsecutive(self, A):
        if len(A) == 0:
            return 0
        A = set(A)
        max_len = 1
        for n in A:
            if n-1 not in A:
                curr_len = 1
                while n+1 in A:
                    n += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
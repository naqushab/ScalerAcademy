class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l, r = 0, n-1
        count = 0
        while l < r:
            s = A[l] + A[r]
            if s == B:
                if A[l] == A[r]:
                    num = (r - l + 1)
                    count += (num * (num - 1) // 2)
                    l += num
                    r -= num
                else:
                    local_l_count = 1
                    local_r_count = 1
                    r -= 1
                    l += 1
                    while r >= 0 and A[r] == A[r+1]:
                        local_r_count += 1
                        r -= 1
                    while l < n and A[l] == A[l-1]:
                        local_l_count += 1
                        l += 1
                    count += (local_l_count*local_r_count)
            elif s < B:
                l += 1
            else:
                r -= 1
        return count % (10**9 + 7)

if __name__ == '__main__':
    print(Solution().solve([ 2, 2, 3, 4, 4, 5, 6, 7, 10 ], 8))
    print(Solution().solve([ 1, 2, 6, 6, 7, 9, 9 ], 13))
import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        ans = []
        A.sort()
        def recurse(index, cur_arr, cur_sum):
            if cur_sum > B:
                return
            if index == len(A) or cur_sum == B:
                if cur_sum == B:
                    ans.append(cur_arr[:])
                return
            for i in range(index, len(A)):
                if i > 0 and A[i] == A[i-1]:
                    continue
                cur_arr.append(A[i])
                cur_sum += A[i]
                recurse(i, cur_arr, cur_sum)
                cur_arr.pop()
                cur_sum -= A[i]

        recurse(0, [], 0)
        return ans

if __name__ == '__main__':
    A = [ 1, 2, 3 ]
    B = 4
    print(Solution().combinationSum(A, B))
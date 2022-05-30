class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        def recurse(cur_arr, index, cur_sum):
            if cur_sum > 1000:
                return 0
            if index == len(A):
                if len(cur_arr) == B and cur_sum <= 1000:
                    return 1
                else:
                    return 0
            cur_sum += A[index]
            cur_arr.append(A[index])
            add = recurse(cur_arr, index+1, cur_sum)
            cur_arr.pop()
            cur_sum -= A[index]
            not_add = recurse(cur_arr, index+1, cur_sum)
            return add + not_add

        count = recurse([], 0, 0)
        return count
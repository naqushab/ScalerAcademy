class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        ans = []

        def recurse(cur_list):
            if len(cur_list) == len(A):
                ans.append(cur_list[:])
                return
            for i in range(len(A)):
                if A[i] in cur_list:
                    continue
                cur_list.append(A[i])
                recurse(cur_list)
                cur_list.pop()

        recurse([])
        return ans
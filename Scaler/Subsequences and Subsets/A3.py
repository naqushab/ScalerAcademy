class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def subsets(self, A):
        self.ans = []
        def backtrack(A, temp):
            if len(A) == 0:
                self.ans.append(sorted(temp[:]))
                return
            temp1 = temp
            temp2 = temp + [A[0]]
            backtrack(A[1:], temp1)
            backtrack(A[1:], temp2)

        backtrack(A, [])
        return sorted(self.ans)
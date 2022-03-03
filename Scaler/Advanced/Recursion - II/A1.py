class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi_util(self, A, frm, to, aux):
        if A == 0:
            return
        self.towerOfHanoi_util(A-1, frm, aux, to)
        self.ans.append([A, frm, to])
        self.towerOfHanoi_util(A-1, aux, to, frm)
    
    def towerOfHanoi(self, A):
        self.ans = []
        self.towerOfHanoi_util(A, 1, 3, 2)
        return self.ans
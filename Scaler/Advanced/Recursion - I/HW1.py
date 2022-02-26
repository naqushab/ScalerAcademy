class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        
        a, b = 0, 1
        return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):
        x = max(A, B)
        y = min(A, B)

        while y!=0:
            temp = x
            x = y
            y = temp%y
        
        return (A*B)//x
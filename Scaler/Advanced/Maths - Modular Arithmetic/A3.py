class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        # A = [ 4, 0, 2, 1, 3 ] then A = [3, 4, 2, 0, 1]
        

if __name__ == "__main__":
    s = Solution()
    A = [ 4, 0, 2, 1, 3 ]
    print(s.arrange(A))
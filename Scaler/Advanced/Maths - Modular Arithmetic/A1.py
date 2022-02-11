class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] = (A[i] % n) + (A[A[i]]) * n
        for i in range(n):
            A[i] = A[i] // n
        return A
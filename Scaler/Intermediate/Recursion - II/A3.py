class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def sum_digits(num):
            if num == 0:
                return 0
            return (num//10)+(num%10)
        
        def magic_number(A):
            if A < 10:
                if A == 1:
                    return True
                else:
                    return False
            else:
                return magic_number(sum_digits(A))
            

        return 1 if magic_number(A) else 0
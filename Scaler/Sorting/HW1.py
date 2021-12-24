from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def custom_sort(a, b):
            s1 = str(a)
            s2 = str(b)
            if s1 == s2:
                return 0
            elif int(s1+s2) > int(s2+s1):
                return -1
            else:
                return 1
        
        A = list(A)
        A.sort(key=cmp_to_key(custom_sort))
        s = ''
        for n in A:
            s += str(n)
        z = ['0']*len(s)
        if s == ''.join(z):
            return 0
        return s
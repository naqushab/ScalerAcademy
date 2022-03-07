from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def cmp_str(x, y):
            a, b = str(x), str(y)
            if a == b:
                return 0
            elif int(a+b) > int(b+a):
                return -1
            else:
                return 1
        arr = list(A)
        arr.sort(key=cmp_to_key(cmp_str))
        s = ''
        for n in arr:
            s += str(n)
        num = int(s)
        return str(num)
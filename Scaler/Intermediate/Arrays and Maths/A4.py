class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        a, b = -1, -1
        count1, count2 = 0, 0
        for n in A:
            if n == a:
                count1 += 1
            elif n == b:
                count2 += 1
            elif count1 == 0:
                count1+= 1
                a = n
            elif count2 == 0:
                count2+= 1
                b = n
            else:
                count1-= 1
                count2-= 1
        counta, countb = 0, 0
        for n in A:
            if n == a:
                counta += 1
            elif n == b:
                countb += 1
        if counta > len(A)//3:
            return a
        if countb > len(A)//3:
            return b
        return -1
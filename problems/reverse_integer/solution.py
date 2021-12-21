class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            s = -1
        else:
            s = 1
        n = 0
        lr = -(2**31)//10
        hr = ((2**31)-1)//10
        while x > 0:
            r = x%10
            x = x//10
            if (lr - r) > n or n >= (hr + r) :
                return 0
            n = n*10 + r
        return n*s
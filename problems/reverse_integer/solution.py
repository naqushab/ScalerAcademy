class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x == -0:
            return 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        num = 0
        l_range = -2**31
        r_range = (2**31)-1
        while x > 0:
            d = x % 10
            if (l_range - d)//10 > num or (r_range+d)//10 < num:
                return 0
            num = num*10 + d
            x =  x//10
        num = num*sign
        return num
            
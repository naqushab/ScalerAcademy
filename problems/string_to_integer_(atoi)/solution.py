class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)
        i = 0
        num = 0
        sign = 1
        
        while i<len(s) and s[i] == ' ':
            i+=1
            
        if i<len(s) and s[i] == '+':
            sign = 1
            i += 1
        elif i <len(s) and s[i] == '-':
            sign = -1
            i += 1
            
        while i<len(s) and s[i].isdigit():
            d = int(s[i])
            if num > int_max//10 or (num == int_max//10 and d > int_max%10):
                return int_max if sign == 1 else int_min
            
            num = num*10 + d
            i += 1
        
        return sign*num
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        c = 0
        n1, n2 = len(num1)-1, len(num2)-1
        while n1>=0 or n2>=0 or c>0:
            if n1 >= 0:
                c += int(num1[n1])
            if n2 >= 0:
                c += int(num2[n2])
            ans.append(str(c%10))
            c = c//10
            n1-=1
            n2-=1
        return ''.join(ans[::-1])
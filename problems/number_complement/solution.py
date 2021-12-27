class Solution:
    def findComplement(self, num: int) -> int:
        n = str(bin(num))[2:]
        ans = 0
        pow = 0
        for i in range(len(n)-1, -1, -1):
            ans += (1-int(n[i]))*2**pow
            pow +=1
        return ans
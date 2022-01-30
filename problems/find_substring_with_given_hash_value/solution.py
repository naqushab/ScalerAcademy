class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(ch):
            return (ord(ch) - ord('a') + 1)
        
        n = len(s)
        ans = 0
        pwr = 1
        
        for i in range(0, k):
            ans += val(s[i]) * pwr
            pwr = pwr * power
            
        if ans % modulo == hashValue:
            return s[:k]
        
        pwr = pwr//power
        for i in range(1, n-k+1):
            ans = ((ans - val(s[i-1]))//power) + (val(s[i+k-1])*pwr)
            if ans % modulo == hashValue:
                return s[i:i+k]
        return ""
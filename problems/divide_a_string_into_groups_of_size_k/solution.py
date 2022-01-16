class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        rem = n%k
        s = s + fill*(k-rem)
        return [ s[i:i+k] for i in range(0, n, k) ]
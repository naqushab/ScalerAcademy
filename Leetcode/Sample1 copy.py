class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        pow = [1]*k
        for i in range(1, k):
            pow[i] = (pow[i-1]*power) % modulo
        ans = 0
        hash = 0
        for i in range(n-1, n-k-1, -1):
            val = (ord(s[i])-ord('a')+1) * (pow[k-n+i])
            val = val + hash
            hash = hash % modulo
        if hash == hashValue:
            ans = n-k
        for i in range(n-k-1, -1, -1):
            rem = (ord(s[i+k])-ord('a')+1) * (pow[k-1])
            hash -= rem
            hash += modulo
            hash = hash % modulo
            hash *= power
            hash += (ord(s[i])-ord('a')+1)
            hash %= modulo
            if hash == hashValue:
                ans = i
        return s[ans:ans+k]



if __name__ == "__main__":
    s = Solution()
    print(s.subStrHash(s='xxterzixjqrghqyeketqeynekvqhc', power=15, modulo=94, k=4, hashValue=16))
    print(s.subStrHash(s='xmmhdakfursinye', power=96, modulo=45, k=15, hashValue=21))
    print(s.subStrHash(s='aadfbxz', power=31, modulo=100, k=3, hashValue=32))
    print(s.subStrHash(s='leetcode', power=7, modulo=20, k=2, hashValue=0))
'''
"xxterzixjqrghqyeketqeynekvqhc"
15
94
4
16
nekv
'''
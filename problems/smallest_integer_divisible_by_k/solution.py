class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0:
            return -1
        else:
            m = {}
            num = 1
            l = 0
            while True:
                l += 1
                r = num % k
                if r == 0:
                    return l
                if r in m:
                    return -1
                else:
                    m[r] = 1
                num = r*10+1
            return -1
                
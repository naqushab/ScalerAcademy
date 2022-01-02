class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = collections.defaultdict(lambda: 0)
        for n in time:
            mod[n%60] += 1
        p = 0
        if mod[0] > 1:
            p += math.factorial(mod[0])//(math.factorial(mod[0]-2)*2)
        if mod[30] > 1:
            p += math.factorial(mod[30])//(math.factorial(mod[30]-2)*2)
        o = 0
        for i in range(1, 30):
            o += (mod[i] * mod[60-i])
        
        return (p + o)
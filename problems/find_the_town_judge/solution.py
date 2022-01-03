class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        m, o = collections.defaultdict(list), collections.defaultdict(list)
        for t in trust:
            m[t[1]].append(t[0])
            o[t[0]].append(t[1])
        
        for k,v in m.items():
            if len(m[k]) == n-1 and len(o[k]) == 0:
                return k
            
        return 1 if n == 1 and not m else -1
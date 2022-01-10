class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sp = s.split()
        sm = {}
        sid = 0
        for st in sp:
            if st not in sm:
                sm[st] = str(sid)
                sid += 1
        
        cm = {}
        cid = 0
        for ch in pattern:
            if ch not in cm:
                cm[ch] = str(cid)
                cid += 1
                
        normal_p = ''
        for ch in pattern:
            normal_p += cm[ch]
            
        normal_s = ''
        for st in sp:
            normal_s += sm[st]
            
        return normal_p == normal_s
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(tmp, s, e, trgt):
            if trgt == 0:
                res.append(tmp[:])
            elif trgt > 0:
                for i in range(s, e):
                    if i > s and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(tmp, i+1, e, trgt-candidates[i])
                    tmp.pop()
                    
        
        candidates.sort(reverse=True)
        backtrack([], 0, len(candidates), target)
        return list(res)